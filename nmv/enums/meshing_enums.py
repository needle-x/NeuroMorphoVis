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


####################################################################################################
# @Meshing
####################################################################################################
class Meshing:
    """Meshing enumerators
    """

    ############################################################################################
    # @__init__
    ############################################################################################
    def __init__(self):
        pass

    ################################################################################################
    # @Technique
    ################################################################################################
    class Technique:
        """Meshing techniques
        """

        # Piecewise watertight meshing
        PIECEWISE_WATERTIGHT = 'MESHING_TECHNIQUE_PIECEWISE_WATERTIGHT'

        # Union meshing
        UNION = 'MESHING_TECHNIQUE_UNION'

        # Skinning
        SKINNING = 'MESHING_TECHNIQUE_SKINNING'

        # Meta objects-based meshing
        META_OBJECTS = 'MESHING_TECHNIQUE_META_OBJECTS'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # Piecewise-watertight
            if argument == 'piecewise-watertight':
                return Meshing.Technique.PIECEWISE_WATERTIGHT

            # Union
            elif argument == 'union':
                return Meshing.Technique.UNION

            # Skinning
            elif argument == 'skinning':
                return Meshing.Technique.SKINNING

            # Meta objects
            elif argument == 'meta-balls':
                return Meshing.Technique.META_OBJECTS

            # By default use piecewise-watertight
            else:
                return Meshing.Technique.PIECEWISE_WATERTIGHT

    ################################################################################################
    # @PiecewiseFilling
    ################################################################################################
    class PiecewiseFilling:
        """The filling of the piecewise meshing.
        """

        # Fill the skeleton using one mesh per path from a root to a leaf section
        PATHS = 'PIECEWISE_FILLING_PATHS'

        # Fill the skeleton using sections and articulations at the bifurcation points
        SECTIONS = 'PIECEWISE_FILLING_SECTIONS'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # Paths
            if argument == 'paths':
                return Meshing.PiecewiseFilling.PATHS

            # Sections
            elif argument == 'sections':
                return Meshing.PiecewiseFilling.SECTIONS

            # By default, use the paths
            else:
                return Meshing.PiecewiseFilling.PATHS

    ################################################################################################
    # @Technique
    ################################################################################################
    class SomaConnection:
        """Soma connection to the arbors
        """

        # Connected
        CONNECTED = 'SOMA_CONNECTED_TO_ARBORS'

        # Disconnected
        DISCONNECTED = 'SOMA_DISCONNECTED_FROM_ARBORS'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # Soma is connected to the arbors
            if argument == 'connected':
                return Meshing.SomaConnection.CONNECTED

            # Soma is disconnected from the arbors
            elif argument == 'disconnected':
                return Meshing.SomaConnection.DISCONNECTED

            # By default use the soma disconnected mode
            else:
                return Meshing.SomaConnection.DISCONNECTED

    ################################################################################################
    # @ArborsConnection
    ################################################################################################
    class ObjectsConnection:
        """Objects connected to each others via joint operation
        """

        # Connected
        CONNECTED = 'CONNECTED_OBJECTS'

        # Disconnected
        DISCONNECTED = 'DISCONNECTED_OBJECTS'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # All the objects are connected to a single mesh object
            if argument == 'connected':
                return Meshing.ObjectsConnection.CONNECTED

            # The objects are disconnected from each others
            elif argument == 'disconnected':
                return Meshing.ObjectsConnection.DISCONNECTED

            # By default use the mesh objects are disconnected
            else:
                return Meshing.ObjectsConnection.DISCONNECTED

    ################################################################################################
    # @Edges
    ################################################################################################
    class Edges:
        """Arbors edges
        """

        # Smooth edges
        SMOOTH = 'ARBORS_SMOOTH_EDGES'

        # Hard edges
        HARD = 'ARBORS_HARD_EDGES'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # Use smooth edges
            if argument == 'smooth':
                return Meshing.Edges.SMOOTH

            # Use hard edges
            elif argument == 'hard':
                return Meshing.Edges.HARD

            # By default use hard edges
            else:
                return Meshing.Edges.HARD

    ################################################################################################
    # @Model
    ################################################################################################
    class Surface:
        """Reconstructed model quality, is it realistic quality or beauty
        """

        # Smooth surface
        SMOOTH = 'SURFACE_SMOOTH'

        # Add noise to the surface to make it rough
        ROUGH = 'SURFACE_ROUGH'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @get_enum
        ############################################################################################
        @staticmethod
        def get_enum(argument):

            # Rough surface
            if argument == 'rough':
                return Meshing.Surface.ROUGH

            # Smooth surface
            elif argument == 'smooth':
                return Meshing.Surface.SMOOTH

            # By default construct a smooth surface
            else:
                return Meshing.Surface.SMOOTH

    ################################################################################################
    # @UnionMeshing
    ################################################################################################
    class UnionMeshing:
        """Union meshing technique options
        """

        # Quad skeleton
        QUAD_SKELETON = 'UNION_QUAD_SKELETON'

        # Circular skeleton
        CIRCULAR_SKELETON = 'UNION_CIRCULAR_SKELETON'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

    ################################################################################################
    # @Spines
    ################################################################################################
    class Spines:
        """Spines options
        """

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @Source
        ############################################################################################
        class Source:
            """Spines source
            """

            # Ignore spines
            IGNORE = 'IGNORE_SPINES'

            # Randomly generated spines
            RANDOM = 'RANDOM_SPINES'

            # Spines integrated in a BBP circuit
            CIRCUIT = 'CIRCUIT_SPINES'

            ########################################################################################
            # @__init__
            ########################################################################################
            def __init__(self):
                pass

            ########################################################################################
            # @get_enum
            ########################################################################################
            @staticmethod
            def get_enum(argument):

                # Ignore spines
                if argument == 'random':
                    return Meshing.Spines.Source.RANDOM

                # Circuit spines
                elif argument == 'circuit':
                    return Meshing.Spines.Source.CIRCUIT

                # By default, ignore loading the spines
                else:
                    return Meshing.Spines.Source.IGNORE

        ############################################################################################
        # @__init__
        ############################################################################################
        class Quality:
            """Spines quality
            """

            # High quality
            HQ = 'SPINES_HQ'

            # Low quality
            LQ = 'SPINES_LQ'

            ########################################################################################
            # @__init__
            ########################################################################################
            def __init__(self):
                pass

            ########################################################################################
            # @get_enum
            ########################################################################################
            @staticmethod
            def get_enum(argument):

                # High quality
                if argument == 'hq':
                    return Meshing.Spines.Quality.HQ

                # By default, use low quality spines
                else:
                    return Meshing.Spines.Quality.LQ

    ################################################################################################
    # @Nucleus
    ################################################################################################
    class Nucleus:
        """Nucleus options
        """

        # Ignore
        IGNORE = 'IGNORE_NUCLEUS'

        # Integrated
        INTEGRATED = 'INTEGRATED_NUCLEUS'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass

        ############################################################################################
        # @__init__
        ############################################################################################
        class Quality:
            """Nucleus mesh quality
            """

            # High quality
            HQ = 'NUCLEUS_HQ'

            # Low quality
            LQ = 'NUCLEUS_LQ'

            ########################################################################################
            # @__init__
            ########################################################################################
            def __init__(self):
                pass

            ########################################################################################
            # @get_enum
            ########################################################################################
            @staticmethod
            def get_enum(argument):

                # High quality
                if argument == 'hq':
                    return Meshing.Nucleus.Quality.HQ

                # By default, use low quality nucleus
                else:
                    return Meshing.Nucleus.Quality.LQ

    ################################################################################################
    # @ExportFormat
    ################################################################################################
    class ExportFormat:
        """The file format of the exported meshes
        """

        # .ply
        PLY = 'EXPORT_FORMAT_PLY'

        # .stl
        STL = 'EXPORT_FORMAT_STL'

        # .obj
        OBJ = 'EXPORT_FORMAT_OBJ'

        # .off
        OFF = 'EXPORT_FORMAT_OFF'

        # .blend
        BLEND = 'EXPORT_FORMAT_BLEND'

        ############################################################################################
        # @__init__
        ############################################################################################
        def __init__(self):
            pass
