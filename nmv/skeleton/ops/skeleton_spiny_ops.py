####################################################################################################
# Copyright (c) 2016 - 2020, EPFL / Blue Brain Project
#               Marwan Abdellah <marwan.abdellah@epfl.ch>
#
# This file is part of NeuroMorphoVis <https://github.com/BlueBrain/NeuroMorphoVis>
#
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This Blender-based tool is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
####################################################################################################

# System imports
import copy
import random

# Blender imports
from mathutils import Vector, Matrix

# Internal modules
import nmv.builders
import nmv.enums
import nmv.mesh
import nmv.shading
import nmv.skeleton
import nmv.utilities
import nmv.scene
import nmv.geometry
import nmv.physics


####################################################################################################
# @get_random_spines_locations_and_normals_across_segments
####################################################################################################
def get_random_spines_across_segments(section,
                                      number_of_spines,
                                      result=[]):
    """Gets a list of random spine morphologies that are correctly aligned along the surface of
    a given morphology section.

    :param section:
        The section where we need to get the spines.
    :param number_of_spines:
        The number of spines requested.
    """

    # A list of all the spines locations and normals
    spines_locations_and_normals = list()

    # Segment by segment
    for i in range(len(section.samples) - 1):

        # Construct a line tube geometry from these two samples
        # NOTE: Make sure that you set the fill_caps to False to avoid having normal faces
        segment_tube = nmv.geometry.draw_cone_line(
            point1=section.samples[i].point, point2=section.samples[i + 1].point,
            point1_radius=section.samples[i].radius, point2_radius=section.samples[i + 1].radius,
            fill_caps=False)

        # Convert the segment tube to a mesh object
        segment_mesh = nmv.scene.ops.convert_object_to_mesh(segment_tube)

        # Get all the faces along the segment mesh
        segment_mesh_faces = list(segment_mesh.data.polygons)

        # Randomly selected faces
        randomly_selected_faces = random.sample(segment_mesh_faces, number_of_spines)

        for face in randomly_selected_faces:
            face_center = face.center
            face_normal = face.normal
            spines_locations_and_normals.append([copy.deepcopy(face_center), copy.deepcopy(face_normal)])

        # Delete the segment mesh
        nmv.scene.delete_object_in_scene(segment_mesh)

    # Extend the results with the the constructed list
    result.extend(spines_locations_and_normals)


####################################################################################################
# @get_random_spines_across_section
####################################################################################################
def get_random_spines_across_section(section,
                                     template_spine_structures,
                                     number_of_spines_per_micron,
                                     max_branching_order,
                                     result=[],
                                     use_skinning_to_build_proxy=False):
    """Gets a list of random spine morphologies that are correctly aligned along the surface of
    a given morphology section.

    :param section:
        The section where we need to get the spines.
    :param template_spine_structures:
        A list of template spine structures that will be used to construct the final spines.
    :param number_of_spines_per_micron:
        The number of spines per micro meter.
    :param max_branching_order:
        The maximum branching order of the arbor.
    :param result:
        A given array to collect the results.
    :param use_skinning_to_build_proxy:
        If this flag is set to True, we will use the Skinning modifiers to build the proxy
        meshes instead of the poly-lines.
    :return:
        The results are generated in the results collecting list.
    """

    # Check the branching order
    if section.branching_order > max_branching_order:
        return

    # Compute the section length
    section_length = nmv.skeleton.ops.compute_section_length(section=section)

    # Compute the number spines required to satisfy the distribution
    number_spines = int(section_length * number_of_spines_per_micron)

    print(number_spines)
    # Ensure that the number of spines > 1
    if number_spines < 1:
        number_spines = 1

    # If we use the skinning modifier to build the proxy mesh, it will give better results, but
    # it is slower
    if use_skinning_to_build_proxy:
        proxy_section_mesh = nmv.skeleton.ops.skin_section_into_mesh(section=section)

    # Otherwise, we can use the normal poly-line, but the results will be less accurate
    else:

        # Reconstruct the polyline from the section points
        section_polyline_data = nmv.skeleton.ops.get_section_poly_line(section=section)

        # Construct a proxy poly-line
        bevel_object = nmv.mesh.create_bezier_circle(radius=1.0, vertices=16,
                                                     name='arbors_bevel')
        proxy_section_polyline = nmv.geometry.draw_poly_line(
            poly_line_data=section_polyline_data, bevel_object=bevel_object, caps=False)

        # Convert the section polyline into a mesh
        proxy_section_mesh = nmv.scene.ops.convert_object_to_mesh(proxy_section_polyline)

    # Get all the faces along the section mesh
    proxy_mesh_faces = list(proxy_section_mesh.data.polygons)

    # Ensure that the number of spines is less than the number of faces
    if number_spines > len(proxy_mesh_faces):
        number_spines = int(len(proxy_mesh_faces) * 0.5)

    # Randomly selected faces
    randomly_selected_faces = random.sample(proxy_mesh_faces, number_spines)

    # Get the radii
    for face in randomly_selected_faces:

        # Get the face normal and center
        face_normal = face.normal.normalized()
        face_center = face.center

        # Compute the spine target point - to be able to orient it correctly
        spine_target = face_center + (face_normal * 1.0)

        # Get the segment radius to determine the spine size
        segment_radius = nmv.skeleton.ops.find_section_radius_near_point(section=section,
                                                                         point=face_center)

        # Compute the spine location, from the center-line of the morphology instead of face center
        spine_location = copy.deepcopy(face.center - (0.5 * segment_radius * face.normal))

        # Select a random spine structure from the templates
        template_spine_structure = random.choice(template_spine_structures)

        # Scale the spine
        nmv.scene.scale_object_uniformly(
            scene_object=template_spine_structure, scale_factor=0.5 * segment_radius)

        # Translate the template spine structure to the spine location
        template_spine_structure.location = spine_location

        # Rotate the spine towards the normal
        nmv.scene.rotate_object_towards_target(
            template_spine_structure, Vector((0, 1, 0)), spine_target)

        # Update the scene
        nmv.scene.update_scene()

        # Get the transformation matrix of the current spine
        transformation_matrix = copy.deepcopy(template_spine_structure.matrix_local)

        # Construct the final spine morphology
        reconstructed_spine_sections = list()
        spine_sample_index = 0

        for spline in template_spine_structure.data.splines:

            spine_samples = list()
            for point in spline.points:
                # Compute the transformed point
                transformed_point = transformation_matrix @ point.co

                # Construct the sample, and append it to the list
                spine_samples.append(nmv.skeleton.Sample(
                    point=transformed_point, radius=point.radius, index=spine_sample_index))

                # Next sample
                spine_sample_index += 1

            # Append it to the final list of the reconstructed spine
            reconstructed_spine_sections.append(
                nmv.skeleton.SpineSection(samples=spine_samples))

        # Add the result to the collecting list
        result.extend(reconstructed_spine_sections)

    # Delete the proxy objects of the section
    if use_skinning_to_build_proxy:
        nmv.scene.delete_object_in_scene(proxy_section_mesh)
    else:
        nmv.scene.delete_list_objects(
            [proxy_section_mesh, proxy_section_polyline, bevel_object])
