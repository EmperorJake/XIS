# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/spritelayouts.pynml'
__tokens = {625: ('global_constants.temp_storage_graphics_chain', 7, 32), 899: ('python:industry.spritelayouts', 9, 44), 939: ('spritelayout ${spritelayout.id} {', 10, 8), 954: ('spritelayout.id', 10, 23), 1031: ('spritelayout.terrain_aware_ground', 11, 58), 4516: ("// Industry-specific ground (snow aware)\n            // non-snow\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite)};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay)};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            // snow\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite, terrain_type='snow')};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay, terrain_type='snow')};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }", 66, 12), 4633: ('industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite)', 69, 26), 4834: ('temp_storage.var_terrain_is_snow', 72, 42), 4969: ('industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay)', 76, 26), 5171: ('temp_storage.var_terrain_is_snow', 79, 42), 5326: ("industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite, terrain_type='snow')", 84, 26), 5549: ('temp_storage.var_terrain_is_snow', 87, 43), 5684: ("industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay, terrain_type='snow')", 91, 26), 5908: ('temp_storage.var_terrain_is_snow', 94, 43), 6034: ("'ne' in spritelayout.fences", 97, 43), 6080: ('// fences NE\n                building {\n                    sprite: 1302 + LOAD_TEMP(${temp_storage.var_fencesprite_ne});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_ne}) == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_ne}) * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }', 98, 16), 6167: ('temp_storage.var_fencesprite_ne', 100, 47), 6248: ('temp_storage.var_use_fence_ne', 101, 46), 6395: ('temp_storage.var_fence_offset_ne', 104, 42), 6734: ("'nw' in spritelayout.fences", 112, 43), 6780: ('// fences NW\n                building {\n                    sprite: 1301 + LOAD_TEMP(${temp_storage.var_fencesprite_nw});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_nw}) == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_nw}) * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }', 113, 16), 6867: ('temp_storage.var_fencesprite_nw', 115, 47), 6948: ('temp_storage.var_use_fence_nw', 116, 46), 7095: ('temp_storage.var_fence_offset_nw', 119, 42), 7450: ('industry.default_industry_properties.override_default_construction_states', 128, 58), 7596: ('spritelayout.building_sprites', 129, 71), 7644: ('// construction states - optional (no snow awareness)\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=0)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 0);\n                }\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=1)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 1);\n                }\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=2)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 2);\n                }', 130, 16), 7755: ('industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=0)', 132, 30), 7968: ('building_sprite.xoffset', 135, 31), 8025: ('building_sprite.yoffset', 136, 31), 8082: ('building_sprite.zoffset', 137, 31), 8139: ('building_sprite.xextent', 138, 31), 8196: ('building_sprite.yextent', 139, 31), 8253: ('building_sprite.zextent', 140, 31), 8314: ('building_sprite.always_draw', 141, 35), 8479: ('industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=1)', 145, 30), 8692: ('building_sprite.xoffset', 148, 31), 8749: ('building_sprite.yoffset', 149, 31), 8806: ('building_sprite.zoffset', 150, 31), 8863: ('building_sprite.xextent', 151, 31), 8920: ('building_sprite.yextent', 152, 31), 8977: ('building_sprite.zextent', 153, 31), 9038: ('building_sprite.always_draw', 154, 35), 9203: ('industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=2)', 158, 30), 9416: ('building_sprite.xoffset', 161, 31), 9473: ('building_sprite.yoffset', 162, 31), 9530: ('building_sprite.zoffset', 163, 31), 9587: ('building_sprite.xextent', 164, 31), 9644: ('building_sprite.yextent', 165, 31), 9701: ('building_sprite.zextent', 166, 31), 9762: ('building_sprite.always_draw', 167, 35), 9979: ('range(len(industry.graphics_change_dates)+1)', 171, 60), 10150: ('spritelayout.building_sprites', 172, 68), 10202: ("// buildings (snow aware)\n                    building {\n                        sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, date_variation_num=date_variation_num)};\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ${building_sprite.xoffset};\n                        yoffset: ${building_sprite.yoffset};\n                        zoffset: ${building_sprite.zoffset};\n                        xextent: ${building_sprite.xextent};\n                        yextent: ${building_sprite.yextent};\n                        zextent: ${building_sprite.zextent};\n                        always_draw: ${building_sprite.always_draw};\n                        hide_sprite: (LOAD_TEMP(${255 - date_variation_num}));\n                    }\n                    building {\n                        sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, terrain_type='snow', date_variation_num=date_variation_num)};\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ${building_sprite.xoffset};\n                        yoffset: ${building_sprite.yoffset};\n                        zoffset: ${building_sprite.zoffset};\n                        xextent: ${building_sprite.xextent};\n                        yextent: ${building_sprite.yextent};\n                        zextent: ${building_sprite.zextent};\n                        always_draw: ${building_sprite.always_draw};\n                        hide_sprite: (LOAD_TEMP(${245 - date_variation_num}));\n                    }", 173, 20), 10293: ('industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, date_variation_num=date_variation_num)', 175, 34), 10557: ('building_sprite.xoffset', 178, 35), 10618: ('building_sprite.yoffset', 179, 35), 10679: ('building_sprite.zoffset', 180, 35), 10740: ('building_sprite.xextent', 181, 35), 10801: ('building_sprite.yextent', 182, 35), 10862: ('building_sprite.zextent', 183, 35), 10927: ('building_sprite.always_draw', 184, 39), 11007: ('255 - date_variation_num', 185, 50), 11123: ("industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, terrain_type='snow', date_variation_num=date_variation_num)", 188, 34), 11408: ('building_sprite.xoffset', 191, 35), 11469: ('building_sprite.yoffset', 192, 35), 11530: ('building_sprite.zoffset', 193, 35), 11591: ('building_sprite.xextent', 194, 35), 11652: ('building_sprite.yextent', 195, 35), 11713: ('building_sprite.zextent', 196, 35), 11778: ('building_sprite.always_draw', 197, 39), 11858: ('245 - date_variation_num', 198, 50), 12031: ('len(spritelayout.magic_trees) > 0', 203, 40), 12085: ('spritelayout.magic_trees', 203, 94), 12128: ('// magic trees, magically added by industry.add_magic_spritelayout()\n                building {\n                    sprite: ${magic_tree.default};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};', 204, 16), 12254: ('magic_tree.default', 206, 30), 12407: ('magic_tree.xoffset', 209, 31), 12459: ('magic_tree.yoffset', 210, 31), 12662: ('xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate == CLIMATE_TROPIC || nearby_tile_height(0, 0) >= snowline_height || construction_state == 0;\n                }\n                building {\n                    sprite: ${magic_tree.tropic};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};', 213, 20), 12948: ('magic_tree.tropic', 219, 30), 13100: ('magic_tree.xoffset', 222, 31), 13152: ('magic_tree.yoffset', 223, 31), 13258: ('xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate != CLIMATE_TROPIC || construction_state == 0;\n                }\n                building {\n                    sprite: ${magic_tree.snow};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};', 225, 20), 13497: ('magic_tree.snow', 231, 30), 13647: ('magic_tree.xoffset', 234, 31), 13699: ('magic_tree.yoffset', 235, 31), 14118: ('spritelayout.smoke_sprites', 244, 53), 14163: ('// smoke sprites\n                building {\n                    sprite: ${smoke_sprite.sprite_number};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${smoke_sprite.xoffset};\n                    yoffset: ${smoke_sprite.yoffset};\n                    zoffset: ${smoke_sprite.zoffset};\n                    xextent: ${smoke_sprite.xextent};\n                    yextent: ${smoke_sprite.yextent};\n                    zextent: ${smoke_sprite.zextent};\n                    hide_sprite: ${smoke_sprite.hide_sprite};\n                }', 245, 16), 14237: ('smoke_sprite.sprite_number', 247, 30), 14398: ('smoke_sprite.xoffset', 250, 31), 14452: ('smoke_sprite.yoffset', 251, 31), 14506: ('smoke_sprite.zoffset', 252, 31), 14560: ('smoke_sprite.xextent', 253, 31), 14614: ('smoke_sprite.yextent', 254, 31), 14668: ('smoke_sprite.zextent', 255, 31), 14726: ('smoke_sprite.hide_sprite', 256, 35), 14849: ("'se' in spritelayout.fences", 260, 43), 14895: ('// fences SE\n                building {\n                    sprite: 1301 + LOAD_TEMP(${temp_storage.var_fencesprite_se});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_se}) == 0);\n                    xoffset: 0;\n                    yoffset:  16;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_se}) * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }', 261, 16), 14982: ('temp_storage.var_fencesprite_se', 263, 47), 15063: ('temp_storage.var_use_fence_se', 264, 46), 15210: ('temp_storage.var_fence_offset_se', 267, 42), 15549: ("'sw' in spritelayout.fences", 275, 43), 15595: ('// fences SW\n                building {\n                    sprite: 1302 + LOAD_TEMP(${temp_storage.var_fencesprite_sw});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_sw}) == 0);\n                    xoffset: 16;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_sw}) * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }', 276, 16), 15682: ('temp_storage.var_fencesprite_sw', 278, 47), 15763: ('temp_storage.var_use_fence_sw', 279, 46), 15910: ('temp_storage.var_fence_offset_sw', 282, 42)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __append('\n')
            __backup_temp_storage_139913549862280 = get('temp_storage', __marker)

            # <Value 'global_constants.temp_storage_graphics_chain' (7:32)> -> __value
            __token = 625
            __value = _lookup_attr(getitem('global_constants'), 'temp_storage_graphics_chain')
            econtext['temp_storage'] = __value
            __append('\n')
            __append('\n    ')
            __backup_spritelayout_139913549450824 = get('spritelayout', __marker)

            # <Value 'python:industry.spritelayouts' (9:44)> -> __iterator
            __token = 899
            __iterator = _lookup_attr(getitem('industry'), 'spritelayouts')
            (__iterator, ____index_139913550391952, ) = getitem('repeat')('spritelayout', __iterator)
            econtext['spritelayout'] = None
            for __item in __iterator:
                econtext['spritelayout'] = __item

                # <Interpolation value=<Substitution '\n        spritelayout ${spritelayout.id} {\n            ' (9:75)> braces_required=True translation=False at 7f40297862e8> -> __content_139913568826456
                __token = 939
                __token = 954
                __content_139913568826456 = _lookup_attr(getitem('spritelayout'), 'id')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n        spritelayout ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ' {\n            ', ))
                if (__content_139913568826456 is None):
                    pass
                else:
                    if (__content_139913568826456 is False):
                        __content_139913568826456 = None
                    else:
                        __tt = type(__content_139913568826456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139913568826456 = str(__content_139913568826456)
                        else:
                            if (__tt is bytes):
                                __content_139913568826456 = decode(__content_139913568826456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139913568826456 = __content_139913568826456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139913568826456)
                                        __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                    else:
                                        __content_139913568826456 = __content_139913568826456()
                if (__content_139913568826456 is not None):
                    __append(__content_139913568826456)

                # <Value 'spritelayout.terrain_aware_ground' (11:58)> -> __condition
                __token = 1031
                __condition = _lookup_attr(getitem('spritelayout'), 'terrain_aware_ground')
                if __condition:
                    __append('\n                ')
                    __append('\n                ')
                    __append('\n                ground {\n                    sprite: GROUNDSPRITE_NORMAL ;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_DESERT;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_TROPIC) || (climate == CLIMATE_TROPIC) && (nearby_tile_terrain_type(0, 0) != TILETYPE_DESERT);\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_DESERT_1_2;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_TROPIC) || ((climate == CLIMATE_TROPIC) && (nearby_tile_terrain_type(0, 0) == TILETYPE_DESERT)) || ((climate == CLIMATE_TROPIC) && (nearby_tile_terrain_type(0, 0) == TILETYPE_NORMAL) && ((nearby_tile_terrain_type( 1, 0) != TILETYPE_DESERT) && (nearby_tile_terrain_type(-1, 0) != TILETYPE_DESERT) && (nearby_tile_terrain_type( 0, 1) != TILETYPE_DESERT) && (nearby_tile_terrain_type( 0,-1) != TILETYPE_DESERT) ) );\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_SNOW_4_4;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_ARCTIC) || (climate == CLIMATE_ARCTIC) && (nearby_tile_height(0, 0) ')
                    __append('<')
                    __append(' (snowline_height + 2));\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_SNOW_3_4;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_ARCTIC) || (climate == CLIMATE_ARCTIC) && ((nearby_tile_height(0, 0) ')
                    __append('<')
                    __append(' (snowline_height + 1)) || (nearby_tile_height(0, 0) >= (snowline_height + 2)));\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_SNOW_2_4;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_ARCTIC) || (climate == CLIMATE_ARCTIC) && ((nearby_tile_height(0, 0) ')
                    __append('<')
                    __append(' (snowline_height + 0)) || (nearby_tile_height(0, 0) >= (snowline_height + 1)));\n                }\n                childsprite {\n                    sprite: GROUNDSPRITE_SNOW_1_4;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    always_draw: 1;\n                    hide_sprite: (climate != CLIMATE_ARCTIC) || (climate == CLIMATE_ARCTIC) && ((nearby_tile_height(0, 0) ')
                    __append('<')
                    __append(' (snowline_height - 1)) || (nearby_tile_height(0, 0) >= (snowline_height + 0)));\n                }\n            ')

                # <Interpolation value=<Substitution "\n\n            // Industry-specific ground (snow aware)\n            // non-snow\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite)};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay)};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            // snow\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_sprite, terrain_type='snow')};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ${industry.unpack_sprite_or_spriteset(spritelayout.ground_overlay, terrain_type='snow')};\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(${temp_storage.var_terrain_is_snow}));\n                always_draw: 1;\n            }\n            " (64:48)> braces_required=True translation=False at 7f4029786358> -> __content_139913568826456
                __token = 4516
                __token = 4633
                __content_139913568826456 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(_lookup_attr(getitem('spritelayout'), 'ground_sprite'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 4834
                __content_139913568826456_4832 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456_4832 = __quote(__content_139913568826456_4832, '\x00', '&#0;', None, False)
                __token = 4969
                __content_139913568826456_4967 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(_lookup_attr(getitem('spritelayout'), 'ground_overlay'))
                __content_139913568826456_4967 = __quote(__content_139913568826456_4967, '\x00', '&#0;', None, False)
                __token = 5171
                __content_139913568826456_5169 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456_5169 = __quote(__content_139913568826456_5169, '\x00', '&#0;', None, False)
                __token = 5326
                __content_139913568826456_5324 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(_lookup_attr(getitem('spritelayout'), 'ground_sprite'), terrain_type='snow')
                __content_139913568826456_5324 = __quote(__content_139913568826456_5324, '\x00', '&#0;', None, False)
                __token = 5549
                __content_139913568826456_5547 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456_5547 = __quote(__content_139913568826456_5547, '\x00', '&#0;', None, False)
                __token = 5684
                __content_139913568826456_5682 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(_lookup_attr(getitem('spritelayout'), 'ground_overlay'), terrain_type='snow')
                __content_139913568826456_5682 = __quote(__content_139913568826456_5682, '\x00', '&#0;', None, False)
                __token = 5908
                __content_139913568826456_5906 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456_5906 = __quote(__content_139913568826456_5906, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\n            // Industry-specific ground (snow aware)\n            // non-snow\n            childsprite {\n                sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(', (__content_139913568826456_4832 if (__content_139913568826456_4832 is not None) else ''), '));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ', (__content_139913568826456_4967 if (__content_139913568826456_4967 is not None) else ''), ';\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (LOAD_TEMP(', (__content_139913568826456_5169 if (__content_139913568826456_5169 is not None) else ''), '));\n                always_draw: 1;\n            }\n            // snow\n            childsprite {\n                sprite: ', (__content_139913568826456_5324 if (__content_139913568826456_5324 is not None) else ''), ';\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(', (__content_139913568826456_5547 if (__content_139913568826456_5547 is not None) else ''), '));\n                always_draw: 1;\n            }\n            childsprite {\n                sprite: ', (__content_139913568826456_5682 if (__content_139913568826456_5682 is not None) else ''), ';\n                recolour_mode: RECOLOUR_REMAP;\n                palette: PALETTE_USE_DEFAULT;\n                hide_sprite: (!LOAD_TEMP(', (__content_139913568826456_5906 if (__content_139913568826456_5906 is not None) else ''), '));\n                always_draw: 1;\n            }\n            ', ))
                if (__content_139913568826456 is None):
                    pass
                else:
                    if (__content_139913568826456 is False):
                        __content_139913568826456 = None
                    else:
                        __tt = type(__content_139913568826456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139913568826456 = str(__content_139913568826456)
                        else:
                            if (__tt is bytes):
                                __content_139913568826456 = decode(__content_139913568826456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139913568826456 = __content_139913568826456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139913568826456)
                                        __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                    else:
                                        __content_139913568826456 = __content_139913568826456()
                if (__content_139913568826456 is not None):
                    __append(__content_139913568826456)

                # <Value "'ne' in spritelayout.fences" (97:43)> -> __condition
                __token = 6034
                __condition = ('ne' in _lookup_attr(getitem('spritelayout'), 'fences'))
                if __condition:

                    # <Interpolation value=<Substitution '\n                // fences NE\n                building {\n                    sprite: 1302 + LOAD_TEMP(${temp_storage.var_fencesprite_ne});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_ne}) == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_ne}) * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ' (97:72)> braces_required=True translation=False at 7f402973d4e0> -> __content_139913568826456
                    __token = 6080
                    __token = 6167
                    __content_139913568826456 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_ne')
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 6248
                    __content_139913568826456_6246 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
                    __content_139913568826456_6246 = __quote(__content_139913568826456_6246, '\x00', '&#0;', None, False)
                    __token = 6395
                    __content_139913568826456_6393 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_ne')
                    __content_139913568826456_6393 = __quote(__content_139913568826456_6393, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                // fences NE\n                building {\n                    sprite: 1302 + LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ');\n                    hide_sprite: (LOAD_TEMP(', (__content_139913568826456_6246 if (__content_139913568826456_6246 is not None) else ''), ') == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(', (__content_139913568826456_6393 if (__content_139913568826456_6393 is not None) else ''), ') * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ', ))
                    if (__content_139913568826456 is None):
                        pass
                    else:
                        if (__content_139913568826456 is False):
                            __content_139913568826456 = None
                        else:
                            __tt = type(__content_139913568826456)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139913568826456 = str(__content_139913568826456)
                            else:
                                if (__tt is bytes):
                                    __content_139913568826456 = decode(__content_139913568826456)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139913568826456 = __content_139913568826456.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139913568826456)
                                            __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                        else:
                                            __content_139913568826456 = __content_139913568826456()
                    if (__content_139913568826456 is not None):
                        __append(__content_139913568826456)
                __append('\n            ')

                # <Value "'nw' in spritelayout.fences" (112:43)> -> __condition
                __token = 6734
                __condition = ('nw' in _lookup_attr(getitem('spritelayout'), 'fences'))
                if __condition:

                    # <Interpolation value=<Substitution '\n                // fences NW\n                building {\n                    sprite: 1301 + LOAD_TEMP(${temp_storage.var_fencesprite_nw});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_nw}) == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_nw}) * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ' (112:72)> braces_required=True translation=False at 7f402973d6d8> -> __content_139913568826456
                    __token = 6780
                    __token = 6867
                    __content_139913568826456 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_nw')
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 6948
                    __content_139913568826456_6946 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
                    __content_139913568826456_6946 = __quote(__content_139913568826456_6946, '\x00', '&#0;', None, False)
                    __token = 7095
                    __content_139913568826456_7093 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_nw')
                    __content_139913568826456_7093 = __quote(__content_139913568826456_7093, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                // fences NW\n                building {\n                    sprite: 1301 + LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ');\n                    hide_sprite: (LOAD_TEMP(', (__content_139913568826456_6946 if (__content_139913568826456_6946 is not None) else ''), ') == 0);\n                    xoffset:  0;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(', (__content_139913568826456_7093 if (__content_139913568826456_7093 is not None) else ''), ') * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ', ))
                    if (__content_139913568826456 is None):
                        pass
                    else:
                        if (__content_139913568826456 is False):
                            __content_139913568826456 = None
                        else:
                            __tt = type(__content_139913568826456)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139913568826456 = str(__content_139913568826456)
                            else:
                                if (__tt is bytes):
                                    __content_139913568826456 = decode(__content_139913568826456)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139913568826456 = __content_139913568826456.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139913568826456)
                                            __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                        else:
                                            __content_139913568826456 = __content_139913568826456()
                    if (__content_139913568826456 is not None):
                        __append(__content_139913568826456)
                __append('\n\n            ')

                # <Value 'industry.default_industry_properties.override_default_construction_states' (128:58)> -> __condition
                __token = 7450
                __condition = _lookup_attr(_lookup_attr(getitem('industry'), 'default_industry_properties'), 'override_default_construction_states')
                if __condition:
                    __backup_building_sprite_139913593805512 = get('building_sprite', __marker)

                    # <Value 'spritelayout.building_sprites' (129:71)> -> __iterator
                    __token = 7596
                    __iterator = _lookup_attr(getitem('spritelayout'), 'building_sprites')
                    (__iterator, ____index_139913550093448, ) = getitem('repeat')('building_sprite', __iterator)
                    econtext['building_sprite'] = None
                    for __item in __iterator:
                        econtext['building_sprite'] = __item

                        # <Interpolation value=<Substitution '\n                // construction states - optional (no snow awareness)\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=0)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 0);\n                }\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=1)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 1);\n                }\n                building {\n                    sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=2)};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${building_sprite.xoffset};\n                    yoffset: ${building_sprite.yoffset};\n                    zoffset: ${building_sprite.zoffset};\n                    xextent: ${building_sprite.xextent};\n                    yextent: ${building_sprite.yextent};\n                    zextent: ${building_sprite.zextent};\n                    always_draw: ${building_sprite.always_draw};\n                    hide_sprite: (construction_state != 2);\n                }\n            ' (129:102)> braces_required=True translation=False at 7f402973d160> -> __content_139913568826456
                        __token = 7644
                        __token = 7755
                        __content_139913568826456 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(getitem('building_sprite'), construction_state_num=0)
                        __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                        __token = 7968
                        __content_139913568826456_7966 = _lookup_attr(getitem('building_sprite'), 'xoffset')
                        __content_139913568826456_7966 = __quote(__content_139913568826456_7966, '\x00', '&#0;', None, False)
                        __token = 8025
                        __content_139913568826456_8023 = _lookup_attr(getitem('building_sprite'), 'yoffset')
                        __content_139913568826456_8023 = __quote(__content_139913568826456_8023, '\x00', '&#0;', None, False)
                        __token = 8082
                        __content_139913568826456_8080 = _lookup_attr(getitem('building_sprite'), 'zoffset')
                        __content_139913568826456_8080 = __quote(__content_139913568826456_8080, '\x00', '&#0;', None, False)
                        __token = 8139
                        __content_139913568826456_8137 = _lookup_attr(getitem('building_sprite'), 'xextent')
                        __content_139913568826456_8137 = __quote(__content_139913568826456_8137, '\x00', '&#0;', None, False)
                        __token = 8196
                        __content_139913568826456_8194 = _lookup_attr(getitem('building_sprite'), 'yextent')
                        __content_139913568826456_8194 = __quote(__content_139913568826456_8194, '\x00', '&#0;', None, False)
                        __token = 8253
                        __content_139913568826456_8251 = _lookup_attr(getitem('building_sprite'), 'zextent')
                        __content_139913568826456_8251 = __quote(__content_139913568826456_8251, '\x00', '&#0;', None, False)
                        __token = 8314
                        __content_139913568826456_8312 = _lookup_attr(getitem('building_sprite'), 'always_draw')
                        __content_139913568826456_8312 = __quote(__content_139913568826456_8312, '\x00', '&#0;', None, False)
                        __token = 8479
                        __content_139913568826456_8477 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(getitem('building_sprite'), construction_state_num=1)
                        __content_139913568826456_8477 = __quote(__content_139913568826456_8477, '\x00', '&#0;', None, False)
                        __token = 8692
                        __content_139913568826456_8690 = _lookup_attr(getitem('building_sprite'), 'xoffset')
                        __content_139913568826456_8690 = __quote(__content_139913568826456_8690, '\x00', '&#0;', None, False)
                        __token = 8749
                        __content_139913568826456_8747 = _lookup_attr(getitem('building_sprite'), 'yoffset')
                        __content_139913568826456_8747 = __quote(__content_139913568826456_8747, '\x00', '&#0;', None, False)
                        __token = 8806
                        __content_139913568826456_8804 = _lookup_attr(getitem('building_sprite'), 'zoffset')
                        __content_139913568826456_8804 = __quote(__content_139913568826456_8804, '\x00', '&#0;', None, False)
                        __token = 8863
                        __content_139913568826456_8861 = _lookup_attr(getitem('building_sprite'), 'xextent')
                        __content_139913568826456_8861 = __quote(__content_139913568826456_8861, '\x00', '&#0;', None, False)
                        __token = 8920
                        __content_139913568826456_8918 = _lookup_attr(getitem('building_sprite'), 'yextent')
                        __content_139913568826456_8918 = __quote(__content_139913568826456_8918, '\x00', '&#0;', None, False)
                        __token = 8977
                        __content_139913568826456_8975 = _lookup_attr(getitem('building_sprite'), 'zextent')
                        __content_139913568826456_8975 = __quote(__content_139913568826456_8975, '\x00', '&#0;', None, False)
                        __token = 9038
                        __content_139913568826456_9036 = _lookup_attr(getitem('building_sprite'), 'always_draw')
                        __content_139913568826456_9036 = __quote(__content_139913568826456_9036, '\x00', '&#0;', None, False)
                        __token = 9203
                        __content_139913568826456_9201 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(getitem('building_sprite'), construction_state_num=2)
                        __content_139913568826456_9201 = __quote(__content_139913568826456_9201, '\x00', '&#0;', None, False)
                        __token = 9416
                        __content_139913568826456_9414 = _lookup_attr(getitem('building_sprite'), 'xoffset')
                        __content_139913568826456_9414 = __quote(__content_139913568826456_9414, '\x00', '&#0;', None, False)
                        __token = 9473
                        __content_139913568826456_9471 = _lookup_attr(getitem('building_sprite'), 'yoffset')
                        __content_139913568826456_9471 = __quote(__content_139913568826456_9471, '\x00', '&#0;', None, False)
                        __token = 9530
                        __content_139913568826456_9528 = _lookup_attr(getitem('building_sprite'), 'zoffset')
                        __content_139913568826456_9528 = __quote(__content_139913568826456_9528, '\x00', '&#0;', None, False)
                        __token = 9587
                        __content_139913568826456_9585 = _lookup_attr(getitem('building_sprite'), 'xextent')
                        __content_139913568826456_9585 = __quote(__content_139913568826456_9585, '\x00', '&#0;', None, False)
                        __token = 9644
                        __content_139913568826456_9642 = _lookup_attr(getitem('building_sprite'), 'yextent')
                        __content_139913568826456_9642 = __quote(__content_139913568826456_9642, '\x00', '&#0;', None, False)
                        __token = 9701
                        __content_139913568826456_9699 = _lookup_attr(getitem('building_sprite'), 'zextent')
                        __content_139913568826456_9699 = __quote(__content_139913568826456_9699, '\x00', '&#0;', None, False)
                        __token = 9762
                        __content_139913568826456_9760 = _lookup_attr(getitem('building_sprite'), 'always_draw')
                        __content_139913568826456_9760 = __quote(__content_139913568826456_9760, '\x00', '&#0;', None, False)
                        __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                // construction states - optional (no snow awareness)\n                building {\n                    sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_7966 if (__content_139913568826456_7966 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_8023 if (__content_139913568826456_8023 is not None) else ''), ';\n                    zoffset: ', (__content_139913568826456_8080 if (__content_139913568826456_8080 is not None) else ''), ';\n                    xextent: ', (__content_139913568826456_8137 if (__content_139913568826456_8137 is not None) else ''), ';\n                    yextent: ', (__content_139913568826456_8194 if (__content_139913568826456_8194 is not None) else ''), ';\n                    zextent: ', (__content_139913568826456_8251 if (__content_139913568826456_8251 is not None) else ''), ';\n                    always_draw: ', (__content_139913568826456_8312 if (__content_139913568826456_8312 is not None) else ''), ';\n                    hide_sprite: (construction_state != 0);\n                }\n                building {\n                    sprite: ', (__content_139913568826456_8477 if (__content_139913568826456_8477 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_8690 if (__content_139913568826456_8690 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_8747 if (__content_139913568826456_8747 is not None) else ''), ';\n                    zoffset: ', (__content_139913568826456_8804 if (__content_139913568826456_8804 is not None) else ''), ';\n                    xextent: ', (__content_139913568826456_8861 if (__content_139913568826456_8861 is not None) else ''), ';\n                    yextent: ', (__content_139913568826456_8918 if (__content_139913568826456_8918 is not None) else ''), ';\n                    zextent: ', (__content_139913568826456_8975 if (__content_139913568826456_8975 is not None) else ''), ';\n                    always_draw: ', (__content_139913568826456_9036 if (__content_139913568826456_9036 is not None) else ''), ';\n                    hide_sprite: (construction_state != 1);\n                }\n                building {\n                    sprite: ', (__content_139913568826456_9201 if (__content_139913568826456_9201 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_9414 if (__content_139913568826456_9414 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_9471 if (__content_139913568826456_9471 is not None) else ''), ';\n                    zoffset: ', (__content_139913568826456_9528 if (__content_139913568826456_9528 is not None) else ''), ';\n                    xextent: ', (__content_139913568826456_9585 if (__content_139913568826456_9585 is not None) else ''), ';\n                    yextent: ', (__content_139913568826456_9642 if (__content_139913568826456_9642 is not None) else ''), ';\n                    zextent: ', (__content_139913568826456_9699 if (__content_139913568826456_9699 is not None) else ''), ';\n                    always_draw: ', (__content_139913568826456_9760 if (__content_139913568826456_9760 is not None) else ''), ';\n                    hide_sprite: (construction_state != 2);\n                }\n            ', ))
                        if (__content_139913568826456 is None):
                            pass
                        else:
                            if (__content_139913568826456 is False):
                                __content_139913568826456 = None
                            else:
                                __tt = type(__content_139913568826456)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139913568826456 = str(__content_139913568826456)
                                else:
                                    if (__tt is bytes):
                                        __content_139913568826456 = decode(__content_139913568826456)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139913568826456 = __content_139913568826456.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139913568826456)
                                                __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                            else:
                                                __content_139913568826456 = __content_139913568826456()
                        if (__content_139913568826456 is not None):
                            __append(__content_139913568826456)
                        ____index_139913550093448 -= 1
                        if (____index_139913550093448 > 0):
                            __append('')
                    if (__backup_building_sprite_139913593805512 is __marker):
                        del econtext['building_sprite']
                    else:
                        econtext['building_sprite'] = __backup_building_sprite_139913593805512
                __append('\n            ')
                __backup_date_variation_num_139913549521304 = get('date_variation_num', __marker)

                # <Value 'range(len(industry.graphics_change_dates)+1)' (171:60)> -> __iterator
                __token = 9979
                __iterator = get('range', range)((len(_lookup_attr(getitem('industry'), 'graphics_change_dates')) + 1))
                (__iterator, ____index_139913550092944, ) = getitem('repeat')('date_variation_num', __iterator)
                econtext['date_variation_num'] = None
                for __item in __iterator:
                    econtext['date_variation_num'] = __item
                    __append('\n                ')
                    __backup_building_sprite_139913549503288 = get('building_sprite', __marker)

                    # <Value 'spritelayout.building_sprites' (172:68)> -> __iterator
                    __token = 10150
                    __iterator = _lookup_attr(getitem('spritelayout'), 'building_sprites')
                    (__iterator, ____index_139913550090536, ) = getitem('repeat')('building_sprite', __iterator)
                    econtext['building_sprite'] = None
                    for __item in __iterator:
                        econtext['building_sprite'] = __item

                        # <Interpolation value=<Substitution "\n                    // buildings (snow aware)\n                    building {\n                        sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, date_variation_num=date_variation_num)};\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ${building_sprite.xoffset};\n                        yoffset: ${building_sprite.yoffset};\n                        zoffset: ${building_sprite.zoffset};\n                        xextent: ${building_sprite.xextent};\n                        yextent: ${building_sprite.yextent};\n                        zextent: ${building_sprite.zextent};\n                        always_draw: ${building_sprite.always_draw};\n                        hide_sprite: (LOAD_TEMP(${255 - date_variation_num}));\n                    }\n                    building {\n                        sprite: ${industry.unpack_sprite_or_spriteset(building_sprite, construction_state_num=3, terrain_type='snow', date_variation_num=date_variation_num)};\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ${building_sprite.xoffset};\n                        yoffset: ${building_sprite.yoffset};\n                        zoffset: ${building_sprite.zoffset};\n                        xextent: ${building_sprite.xextent};\n                        yextent: ${building_sprite.yextent};\n                        zextent: ${building_sprite.zextent};\n                        always_draw: ${building_sprite.always_draw};\n                        hide_sprite: (LOAD_TEMP(${245 - date_variation_num}));\n                    }\n                " (172:99)> braces_required=True translation=False at 7f402973db70> -> __content_139913568826456
                        __token = 10202
                        __token = 10293
                        __content_139913568826456 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(getitem('building_sprite'), construction_state_num=3, date_variation_num=getitem('date_variation_num'))
                        __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                        __token = 10557
                        __content_139913568826456_10555 = _lookup_attr(getitem('building_sprite'), 'xoffset')
                        __content_139913568826456_10555 = __quote(__content_139913568826456_10555, '\x00', '&#0;', None, False)
                        __token = 10618
                        __content_139913568826456_10616 = _lookup_attr(getitem('building_sprite'), 'yoffset')
                        __content_139913568826456_10616 = __quote(__content_139913568826456_10616, '\x00', '&#0;', None, False)
                        __token = 10679
                        __content_139913568826456_10677 = _lookup_attr(getitem('building_sprite'), 'zoffset')
                        __content_139913568826456_10677 = __quote(__content_139913568826456_10677, '\x00', '&#0;', None, False)
                        __token = 10740
                        __content_139913568826456_10738 = _lookup_attr(getitem('building_sprite'), 'xextent')
                        __content_139913568826456_10738 = __quote(__content_139913568826456_10738, '\x00', '&#0;', None, False)
                        __token = 10801
                        __content_139913568826456_10799 = _lookup_attr(getitem('building_sprite'), 'yextent')
                        __content_139913568826456_10799 = __quote(__content_139913568826456_10799, '\x00', '&#0;', None, False)
                        __token = 10862
                        __content_139913568826456_10860 = _lookup_attr(getitem('building_sprite'), 'zextent')
                        __content_139913568826456_10860 = __quote(__content_139913568826456_10860, '\x00', '&#0;', None, False)
                        __token = 10927
                        __content_139913568826456_10925 = _lookup_attr(getitem('building_sprite'), 'always_draw')
                        __content_139913568826456_10925 = __quote(__content_139913568826456_10925, '\x00', '&#0;', None, False)
                        __token = 11007
                        __content_139913568826456_11005 = (255 - getitem('date_variation_num'))
                        __content_139913568826456_11005 = __quote(__content_139913568826456_11005, '\x00', '&#0;', None, False)
                        __token = 11123
                        __content_139913568826456_11121 = _lookup_attr(getitem('industry'), 'unpack_sprite_or_spriteset')(getitem('building_sprite'), construction_state_num=3, terrain_type='snow', date_variation_num=getitem('date_variation_num'))
                        __content_139913568826456_11121 = __quote(__content_139913568826456_11121, '\x00', '&#0;', None, False)
                        __token = 11408
                        __content_139913568826456_11406 = _lookup_attr(getitem('building_sprite'), 'xoffset')
                        __content_139913568826456_11406 = __quote(__content_139913568826456_11406, '\x00', '&#0;', None, False)
                        __token = 11469
                        __content_139913568826456_11467 = _lookup_attr(getitem('building_sprite'), 'yoffset')
                        __content_139913568826456_11467 = __quote(__content_139913568826456_11467, '\x00', '&#0;', None, False)
                        __token = 11530
                        __content_139913568826456_11528 = _lookup_attr(getitem('building_sprite'), 'zoffset')
                        __content_139913568826456_11528 = __quote(__content_139913568826456_11528, '\x00', '&#0;', None, False)
                        __token = 11591
                        __content_139913568826456_11589 = _lookup_attr(getitem('building_sprite'), 'xextent')
                        __content_139913568826456_11589 = __quote(__content_139913568826456_11589, '\x00', '&#0;', None, False)
                        __token = 11652
                        __content_139913568826456_11650 = _lookup_attr(getitem('building_sprite'), 'yextent')
                        __content_139913568826456_11650 = __quote(__content_139913568826456_11650, '\x00', '&#0;', None, False)
                        __token = 11713
                        __content_139913568826456_11711 = _lookup_attr(getitem('building_sprite'), 'zextent')
                        __content_139913568826456_11711 = __quote(__content_139913568826456_11711, '\x00', '&#0;', None, False)
                        __token = 11778
                        __content_139913568826456_11776 = _lookup_attr(getitem('building_sprite'), 'always_draw')
                        __content_139913568826456_11776 = __quote(__content_139913568826456_11776, '\x00', '&#0;', None, False)
                        __token = 11858
                        __content_139913568826456_11856 = (245 - getitem('date_variation_num'))
                        __content_139913568826456_11856 = __quote(__content_139913568826456_11856, '\x00', '&#0;', None, False)
                        __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                    // buildings (snow aware)\n                    building {\n                        sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ', (__content_139913568826456_10555 if (__content_139913568826456_10555 is not None) else ''), ';\n                        yoffset: ', (__content_139913568826456_10616 if (__content_139913568826456_10616 is not None) else ''), ';\n                        zoffset: ', (__content_139913568826456_10677 if (__content_139913568826456_10677 is not None) else ''), ';\n                        xextent: ', (__content_139913568826456_10738 if (__content_139913568826456_10738 is not None) else ''), ';\n                        yextent: ', (__content_139913568826456_10799 if (__content_139913568826456_10799 is not None) else ''), ';\n                        zextent: ', (__content_139913568826456_10860 if (__content_139913568826456_10860 is not None) else ''), ';\n                        always_draw: ', (__content_139913568826456_10925 if (__content_139913568826456_10925 is not None) else ''), ';\n                        hide_sprite: (LOAD_TEMP(', (__content_139913568826456_11005 if (__content_139913568826456_11005 is not None) else ''), '));\n                    }\n                    building {\n                        sprite: ', (__content_139913568826456_11121 if (__content_139913568826456_11121 is not None) else ''), ';\n                        recolour_mode: RECOLOUR_REMAP;\n                        palette: PALETTE_USE_DEFAULT;\n                        xoffset: ', (__content_139913568826456_11406 if (__content_139913568826456_11406 is not None) else ''), ';\n                        yoffset: ', (__content_139913568826456_11467 if (__content_139913568826456_11467 is not None) else ''), ';\n                        zoffset: ', (__content_139913568826456_11528 if (__content_139913568826456_11528 is not None) else ''), ';\n                        xextent: ', (__content_139913568826456_11589 if (__content_139913568826456_11589 is not None) else ''), ';\n                        yextent: ', (__content_139913568826456_11650 if (__content_139913568826456_11650 is not None) else ''), ';\n                        zextent: ', (__content_139913568826456_11711 if (__content_139913568826456_11711 is not None) else ''), ';\n                        always_draw: ', (__content_139913568826456_11776 if (__content_139913568826456_11776 is not None) else ''), ';\n                        hide_sprite: (LOAD_TEMP(', (__content_139913568826456_11856 if (__content_139913568826456_11856 is not None) else ''), '));\n                    }\n                ', ))
                        if (__content_139913568826456 is None):
                            pass
                        else:
                            if (__content_139913568826456 is False):
                                __content_139913568826456 = None
                            else:
                                __tt = type(__content_139913568826456)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139913568826456 = str(__content_139913568826456)
                                else:
                                    if (__tt is bytes):
                                        __content_139913568826456 = decode(__content_139913568826456)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139913568826456 = __content_139913568826456.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139913568826456)
                                                __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                            else:
                                                __content_139913568826456 = __content_139913568826456()
                        if (__content_139913568826456 is not None):
                            __append(__content_139913568826456)
                        ____index_139913550090536 -= 1
                        if (____index_139913550090536 > 0):
                            __append('')
                    if (__backup_building_sprite_139913549503288 is __marker):
                        del econtext['building_sprite']
                    else:
                        econtext['building_sprite'] = __backup_building_sprite_139913549503288
                    __append('\n            ')
                    ____index_139913550092944 -= 1
                    if (____index_139913550092944 > 0):
                        __append('')
                if (__backup_date_variation_num_139913549521304 is __marker):
                    del econtext['date_variation_num']
                else:
                    econtext['date_variation_num'] = __backup_date_variation_num_139913549521304
                __append('\n\n            ')

                # <Value 'len(spritelayout.magic_trees) > 0' (203:40)> -> __condition
                __token = 12031
                __condition = (len(_lookup_attr(getitem('spritelayout'), 'magic_trees')) > 0)
                if __condition:
                    __backup_magic_tree_139913549861440 = get('magic_tree', __marker)

                    # <Value 'spritelayout.magic_trees' (203:94)> -> __iterator
                    __token = 12085
                    __iterator = _lookup_attr(getitem('spritelayout'), 'magic_trees')
                    (__iterator, ____index_139913550093392, ) = getitem('repeat')('magic_tree', __iterator)
                    econtext['magic_tree'] = None
                    for __item in __iterator:
                        econtext['magic_tree'] = __item

                        # <Interpolation value=<Substitution '\n                // magic trees, magically added by industry.add_magic_spritelayout()\n                building {\n                    sprite: ${magic_tree.default};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};\n                    ' (203:120)> braces_required=True translation=False at 7f402978d160> -> __content_139913568826456
                        __token = 12128
                        __token = 12254
                        __content_139913568826456 = _lookup_attr(getitem('magic_tree'), 'default')
                        __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                        __token = 12407
                        __content_139913568826456_12405 = _lookup_attr(getitem('magic_tree'), 'xoffset')
                        __content_139913568826456_12405 = __quote(__content_139913568826456_12405, '\x00', '&#0;', None, False)
                        __token = 12459
                        __content_139913568826456_12457 = _lookup_attr(getitem('magic_tree'), 'yoffset')
                        __content_139913568826456_12457 = __quote(__content_139913568826456_12457, '\x00', '&#0;', None, False)
                        __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                // magic trees, magically added by industry.add_magic_spritelayout()\n                building {\n                    sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_12405 if (__content_139913568826456_12405 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_12457 if (__content_139913568826456_12457 is not None) else ''), ';\n                    ', ))
                        if (__content_139913568826456 is None):
                            pass
                        else:
                            if (__content_139913568826456 is False):
                                __content_139913568826456 = None
                            else:
                                __tt = type(__content_139913568826456)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139913568826456 = str(__content_139913568826456)
                                else:
                                    if (__tt is bytes):
                                        __content_139913568826456 = decode(__content_139913568826456)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139913568826456 = __content_139913568826456.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139913568826456)
                                                __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                            else:
                                                __content_139913568826456 = __content_139913568826456()
                        if (__content_139913568826456 is not None):
                            __append(__content_139913568826456)
                        __append('\n                    ')

                        # <Interpolation value=<Substitution '\n                    xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate == CLIMATE_TROPIC || nearby_tile_height(0, 0) >= snowline_height || construction_state == 0;\n                }\n                building {\n                    sprite: ${magic_tree.tropic};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};\n                    ' (212:96)> braces_required=True translation=False at 7f402978ddd8> -> __content_139913568826456
                        __token = 12662
                        __token = 12948
                        __content_139913568826456 = _lookup_attr(getitem('magic_tree'), 'tropic')
                        __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                        __token = 13100
                        __content_139913568826456_13098 = _lookup_attr(getitem('magic_tree'), 'xoffset')
                        __content_139913568826456_13098 = __quote(__content_139913568826456_13098, '\x00', '&#0;', None, False)
                        __token = 13152
                        __content_139913568826456_13150 = _lookup_attr(getitem('magic_tree'), 'yoffset')
                        __content_139913568826456_13150 = __quote(__content_139913568826456_13150, '\x00', '&#0;', None, False)
                        __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                    xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate == CLIMATE_TROPIC || nearby_tile_height(0, 0) >= snowline_height || construction_state == 0;\n                }\n                building {\n                    sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_13098 if (__content_139913568826456_13098 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_13150 if (__content_139913568826456_13150 is not None) else ''), ';\n                    ', ))
                        if (__content_139913568826456 is None):
                            pass
                        else:
                            if (__content_139913568826456 is False):
                                __content_139913568826456 = None
                            else:
                                __tt = type(__content_139913568826456)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139913568826456 = str(__content_139913568826456)
                                else:
                                    if (__tt is bytes):
                                        __content_139913568826456 = decode(__content_139913568826456)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139913568826456 = __content_139913568826456.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139913568826456)
                                                __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                            else:
                                                __content_139913568826456 = __content_139913568826456()
                        if (__content_139913568826456 is not None):
                            __append(__content_139913568826456)

                        # <Interpolation value=<Substitution '\n                    xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate != CLIMATE_TROPIC || construction_state == 0;\n                }\n                building {\n                    sprite: ${magic_tree.snow};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${magic_tree.xoffset};\n                    yoffset: ${magic_tree.yoffset};\n                    ' (224:64)> braces_required=True translation=False at 7f402978d9b0> -> __content_139913568826456
                        __token = 13258
                        __token = 13497
                        __content_139913568826456 = _lookup_attr(getitem('magic_tree'), 'snow')
                        __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                        __token = 13647
                        __content_139913568826456_13645 = _lookup_attr(getitem('magic_tree'), 'xoffset')
                        __content_139913568826456_13645 = __quote(__content_139913568826456_13645, '\x00', '&#0;', None, False)
                        __token = 13699
                        __content_139913568826456_13697 = _lookup_attr(getitem('magic_tree'), 'yoffset')
                        __content_139913568826456_13697 = __quote(__content_139913568826456_13697, '\x00', '&#0;', None, False)
                        __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                    xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate != CLIMATE_TROPIC || construction_state == 0;\n                }\n                building {\n                    sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_13645 if (__content_139913568826456_13645 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_13697 if (__content_139913568826456_13697 is not None) else ''), ';\n                    ', ))
                        if (__content_139913568826456 is None):
                            pass
                        else:
                            if (__content_139913568826456 is False):
                                __content_139913568826456 = None
                            else:
                                __tt = type(__content_139913568826456)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_139913568826456 = str(__content_139913568826456)
                                else:
                                    if (__tt is bytes):
                                        __content_139913568826456 = decode(__content_139913568826456)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_139913568826456 = __content_139913568826456.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_139913568826456)
                                                __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                            else:
                                                __content_139913568826456 = __content_139913568826456()
                        if (__content_139913568826456 is not None):
                            __append(__content_139913568826456)
                        __append('\n                    xextent: 4;\n                    yextent: 4;\n                    zextent: 32;\n                    hide_sprite: climate != CLIMATE_ARCTIC || nearby_tile_height(0, 0) ')
                        __append('<')
                        __append(' snowline_height || construction_state == 0;\n                }\n            ')
                        ____index_139913550093392 -= 1
                        if (____index_139913550093392 > 0):
                            __append('')
                    if (__backup_magic_tree_139913549861440 is __marker):
                        del econtext['magic_tree']
                    else:
                        econtext['magic_tree'] = __backup_magic_tree_139913549861440
                __append('\n\n            ')
                __backup_smoke_sprite_139913549456440 = get('smoke_sprite', __marker)

                # <Value 'spritelayout.smoke_sprites' (244:53)> -> __iterator
                __token = 14118
                __iterator = _lookup_attr(getitem('spritelayout'), 'smoke_sprites')
                (__iterator, ____index_139913550162296, ) = getitem('repeat')('smoke_sprite', __iterator)
                econtext['smoke_sprite'] = None
                for __item in __iterator:
                    econtext['smoke_sprite'] = __item

                    # <Interpolation value=<Substitution '\n                // smoke sprites\n                building {\n                    sprite: ${smoke_sprite.sprite_number};\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ${smoke_sprite.xoffset};\n                    yoffset: ${smoke_sprite.yoffset};\n                    zoffset: ${smoke_sprite.zoffset};\n                    xextent: ${smoke_sprite.xextent};\n                    yextent: ${smoke_sprite.yextent};\n                    zextent: ${smoke_sprite.zextent};\n                    hide_sprite: ${smoke_sprite.hide_sprite};\n                }\n            ' (244:81)> braces_required=True translation=False at 7f402974e160> -> __content_139913568826456
                    __token = 14163
                    __token = 14237
                    __content_139913568826456 = _lookup_attr(getitem('smoke_sprite'), 'sprite_number')
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 14398
                    __content_139913568826456_14396 = _lookup_attr(getitem('smoke_sprite'), 'xoffset')
                    __content_139913568826456_14396 = __quote(__content_139913568826456_14396, '\x00', '&#0;', None, False)
                    __token = 14452
                    __content_139913568826456_14450 = _lookup_attr(getitem('smoke_sprite'), 'yoffset')
                    __content_139913568826456_14450 = __quote(__content_139913568826456_14450, '\x00', '&#0;', None, False)
                    __token = 14506
                    __content_139913568826456_14504 = _lookup_attr(getitem('smoke_sprite'), 'zoffset')
                    __content_139913568826456_14504 = __quote(__content_139913568826456_14504, '\x00', '&#0;', None, False)
                    __token = 14560
                    __content_139913568826456_14558 = _lookup_attr(getitem('smoke_sprite'), 'xextent')
                    __content_139913568826456_14558 = __quote(__content_139913568826456_14558, '\x00', '&#0;', None, False)
                    __token = 14614
                    __content_139913568826456_14612 = _lookup_attr(getitem('smoke_sprite'), 'yextent')
                    __content_139913568826456_14612 = __quote(__content_139913568826456_14612, '\x00', '&#0;', None, False)
                    __token = 14668
                    __content_139913568826456_14666 = _lookup_attr(getitem('smoke_sprite'), 'zextent')
                    __content_139913568826456_14666 = __quote(__content_139913568826456_14666, '\x00', '&#0;', None, False)
                    __token = 14726
                    __content_139913568826456_14724 = _lookup_attr(getitem('smoke_sprite'), 'hide_sprite')
                    __content_139913568826456_14724 = __quote(__content_139913568826456_14724, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                // smoke sprites\n                building {\n                    sprite: ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette: PALETTE_USE_DEFAULT;\n                    xoffset: ', (__content_139913568826456_14396 if (__content_139913568826456_14396 is not None) else ''), ';\n                    yoffset: ', (__content_139913568826456_14450 if (__content_139913568826456_14450 is not None) else ''), ';\n                    zoffset: ', (__content_139913568826456_14504 if (__content_139913568826456_14504 is not None) else ''), ';\n                    xextent: ', (__content_139913568826456_14558 if (__content_139913568826456_14558 is not None) else ''), ';\n                    yextent: ', (__content_139913568826456_14612 if (__content_139913568826456_14612 is not None) else ''), ';\n                    zextent: ', (__content_139913568826456_14666 if (__content_139913568826456_14666 is not None) else ''), ';\n                    hide_sprite: ', (__content_139913568826456_14724 if (__content_139913568826456_14724 is not None) else ''), ';\n                }\n            ', ))
                    if (__content_139913568826456 is None):
                        pass
                    else:
                        if (__content_139913568826456 is False):
                            __content_139913568826456 = None
                        else:
                            __tt = type(__content_139913568826456)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139913568826456 = str(__content_139913568826456)
                            else:
                                if (__tt is bytes):
                                    __content_139913568826456 = decode(__content_139913568826456)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139913568826456 = __content_139913568826456.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139913568826456)
                                            __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                        else:
                                            __content_139913568826456 = __content_139913568826456()
                    if (__content_139913568826456 is not None):
                        __append(__content_139913568826456)
                    ____index_139913550162296 -= 1
                    if (____index_139913550162296 > 0):
                        __append('')
                if (__backup_smoke_sprite_139913549456440 is __marker):
                    del econtext['smoke_sprite']
                else:
                    econtext['smoke_sprite'] = __backup_smoke_sprite_139913549456440
                __append('\n\n            ')

                # <Value "'se' in spritelayout.fences" (260:43)> -> __condition
                __token = 14849
                __condition = ('se' in _lookup_attr(getitem('spritelayout'), 'fences'))
                if __condition:

                    # <Interpolation value=<Substitution '\n                // fences SE\n                building {\n                    sprite: 1301 + LOAD_TEMP(${temp_storage.var_fencesprite_se});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_se}) == 0);\n                    xoffset: 0;\n                    yoffset:  16;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_se}) * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ' (260:72)> braces_required=True translation=False at 7f402974eda0> -> __content_139913568826456
                    __token = 14895
                    __token = 14982
                    __content_139913568826456 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_se')
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 15063
                    __content_139913568826456_15061 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
                    __content_139913568826456_15061 = __quote(__content_139913568826456_15061, '\x00', '&#0;', None, False)
                    __token = 15210
                    __content_139913568826456_15208 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_se')
                    __content_139913568826456_15208 = __quote(__content_139913568826456_15208, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                // fences SE\n                building {\n                    sprite: 1301 + LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ');\n                    hide_sprite: (LOAD_TEMP(', (__content_139913568826456_15061 if (__content_139913568826456_15061 is not None) else ''), ') == 0);\n                    xoffset: 0;\n                    yoffset:  16;\n                    zoffset:  LOAD_TEMP(', (__content_139913568826456_15208 if (__content_139913568826456_15208 is not None) else ''), ') * 8;\n                    xextent: 16;\n                    yextent: 1;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ', ))
                    if (__content_139913568826456 is None):
                        pass
                    else:
                        if (__content_139913568826456 is False):
                            __content_139913568826456 = None
                        else:
                            __tt = type(__content_139913568826456)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139913568826456 = str(__content_139913568826456)
                            else:
                                if (__tt is bytes):
                                    __content_139913568826456 = decode(__content_139913568826456)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139913568826456 = __content_139913568826456.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139913568826456)
                                            __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                        else:
                                            __content_139913568826456 = __content_139913568826456()
                    if (__content_139913568826456 is not None):
                        __append(__content_139913568826456)
                __append('\n            ')

                # <Value "'sw' in spritelayout.fences" (275:43)> -> __condition
                __token = 15549
                __condition = ('sw' in _lookup_attr(getitem('spritelayout'), 'fences'))
                if __condition:

                    # <Interpolation value=<Substitution '\n                // fences SW\n                building {\n                    sprite: 1302 + LOAD_TEMP(${temp_storage.var_fencesprite_sw});\n                    hide_sprite: (LOAD_TEMP(${temp_storage.var_use_fence_sw}) == 0);\n                    xoffset: 16;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(${temp_storage.var_fence_offset_sw}) * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ' (275:72)> braces_required=True translation=False at 7f402974e4a8> -> __content_139913568826456
                    __token = 15595
                    __token = 15682
                    __content_139913568826456 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_sw')
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 15763
                    __content_139913568826456_15761 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
                    __content_139913568826456_15761 = __quote(__content_139913568826456_15761, '\x00', '&#0;', None, False)
                    __token = 15910
                    __content_139913568826456_15908 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_sw')
                    __content_139913568826456_15908 = __quote(__content_139913568826456_15908, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                // fences SW\n                building {\n                    sprite: 1302 + LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ');\n                    hide_sprite: (LOAD_TEMP(', (__content_139913568826456_15761 if (__content_139913568826456_15761 is not None) else ''), ') == 0);\n                    xoffset: 16;\n                    yoffset:  0;\n                    zoffset:  LOAD_TEMP(', (__content_139913568826456_15908 if (__content_139913568826456_15908 is not None) else ''), ') * 8;\n                    xextent: 1;\n                    yextent: 16;\n                    zextent: 6;\n                    recolour_mode: RECOLOUR_REMAP;\n                    palette:       PALETTE_USE_DEFAULT;\n                }\n            ', ))
                    if (__content_139913568826456 is None):
                        pass
                    else:
                        if (__content_139913568826456 is False):
                            __content_139913568826456 = None
                        else:
                            __tt = type(__content_139913568826456)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139913568826456 = str(__content_139913568826456)
                            else:
                                if (__tt is bytes):
                                    __content_139913568826456 = decode(__content_139913568826456)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139913568826456 = __content_139913568826456.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139913568826456)
                                            __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                        else:
                                            __content_139913568826456 = __content_139913568826456()
                    if (__content_139913568826456 is not None):
                        __append(__content_139913568826456)
                __append('\n\n        }\n    ')
                ____index_139913550391952 -= 1
                if (____index_139913550391952 > 0):
                    __append('')
            if (__backup_spritelayout_139913549450824 is __marker):
                del econtext['spritelayout']
            else:
                econtext['spritelayout'] = __backup_spritelayout_139913549450824
            __append('\n')
            if (__backup_temp_storage_139913549862280 is __marker):
                del econtext['temp_storage']
            else:
                econtext['temp_storage'] = __backup_temp_storage_139913549862280
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }