# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/graphics_switches.pynml'
__tokens = {626: ('global_constants.temp_storage_graphics_chain', 8, 32), 997: ('industry.extra_graphics_switches', 11, 57), 1162: ('switch(FEAT_INDUSTRYTILES, SELF, ${graphics_switch.id}, nearby_tile_slope(0,0)) {', 13, 8), 1197: ('graphics_switch.id', 13, 43), 1315: ('graphics_switch.slope_spritelayout_mapping.items()', 14, 71), 1384: ('${slope_spritelayout[0]}: ${slope_spritelayout[1]};', 15, 16), 1386: ('slope_spritelayout[0]', 15, 18), 1412: ('slope_spritelayout[1]', 15, 44), 1494: ('${graphics_switch.default_result};\n        }', 17, 12), 1496: ('graphics_switch.default_result', 17, 14), 1642: ('python:industry.industry_layouts', 21, 67), 1685: ('switch(FEAT_INDUSTRYTILES, SELF, ${industry_layout.id}_graphics_switch, relative_pos) {', 22, 8), 1720: ('industry_layout.id', 22, 43), 1827: ('industry_layout.layout', 23, 54), 1868: ('relative_coord(${layout[0]}, ${layout[1]}): ${layout[3]};', 24, 16), 1885: ('layout[0]', 24, 33), 1899: ('layout[1]', 24, 47), 1914: ('layout[3]', 24, 62), 1979: ('${industry_layout.layout[0][3]}; // a default is needed, but should never be reached, layout definitions are explicit\n        }', 26, 12), 1981: ('industry_layout.layout[0][3]', 26, 14), 2157: ('switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_graphics_switch_layouts, layout_num) {', 30, 4), 2194: ('industry.id', 30, 41), 2314: ('range(len(industry.industry_layouts))', 31, 59), 2366: ('${layout_num+1}: ${industry.industry_layouts[layout_num].id}_graphics_switch;', 32, 12), 2368: ('layout_num+1', 32, 14), 2385: ('industry.industry_layouts[layout_num].id', 32, 31), 2494: ('${industry.industry_layouts[0].id}_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ${industry.get_switch_name_for_construction_states()};\n        ${industry.id}_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ${temp_storage.var_terrain_is_snow})', 34, 8), 2496: ('industry.industry_layouts[0].id', 34, 10), 2603: ('industry.id', 37, 39), 2699: ('industry.get_switch_name_for_construction_states()', 38, 16), 2762: ('industry.id', 39, 10), 2866: ('industry.id', 42, 39), 2953: ('temp_storage.var_terrain_is_snow', 43, 57), 3052: ('range(len(industry.graphics_change_dates)+1)', 44, 64), 3175: (', STORE_TEMP(${industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)},\n                                 ${255 - date_variation_num})', 45, 20), 3190: ('industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)', 45, 35), 3306: ('255 - date_variation_num', 46, 35), 3410: (', STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(${255 - date_variation_num}),\n                                 ${255 - date_variation_num})\n                    , STORE_TEMP(LOAD_TEMP(${temp_storage.var_terrain_is_snow}) == 0 ? 1 : LOAD_TEMP(${255 - date_variation_num}),', 47, 20), 3465: ('255 - date_variation_num', 47, 75), 3528: ('255 - date_variation_num', 48, 35), 3600: ('temp_storage.var_terrain_is_snow', 49, 45), 3658: ('255 - date_variation_num', 49, 103), 3759: ('${245 - date_variation_num})', 50, 33), 3761: ('245 - date_variation_num', 50, 35), 3882: (', STORE_TEMP(LOAD_TEMP(${temp_storage.var_terrain_is_snow}) == 1 ? 1 : LOAD_TEMP(${255 - date_variation_num}),', 51, 20), 3907: ('temp_storage.var_terrain_is_snow', 51, 45), 3965: ('255 - date_variation_num', 51, 103), 4050: ('${255 - date_variation_num})', 52, 33), 4052: ('255 - date_variation_num', 52, 35), 4130: (']) {\n        ${industry.id}_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_master_graphics_switch, STORE_TEMP(random_bits, ${temp_storage.var_random_bits})) {\n        ${industry.id}_store_temp_vars; // default\n    }', 54, 12), 4145: ('industry.id', 55, 10), 4262: ('industry.id', 58, 41), 4334: ('temp_storage.var_random_bits', 58, 113), 4378: ('industry.id', 59, 10), 4459: ('switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * !nearby_tile_is_same_industry(-1,  0), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * !nearby_tile_is_same_industry( 0, -1), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * !nearby_tile_is_same_industry( 0,  1), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * !nearby_tile_is_same_industry( 1,  0), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fences, [\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_se}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_sw}),\n\n                STORE_TEMP(1, ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_sw}),\n\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_se}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_sw}),\n                ]) {\n        ${industry.id}_tile_fence_industry;\n    }', 63, 4), 4495: ('industry.id', 63, 40), 4569: ('temp_storage.var_use_fence_ne', 64, 39), 4656: ('temp_storage.var_use_fence_ne', 64, 126), 4728: ('temp_storage.var_use_fence_nw', 65, 39), 4815: ('temp_storage.var_use_fence_nw', 65, 126), 4887: ('temp_storage.var_use_fence_se', 66, 39), 4974: ('temp_storage.var_use_fence_se', 66, 126), 5046: ('temp_storage.var_use_fence_sw', 67, 39), 5133: ('temp_storage.var_use_fence_sw', 67, 126), 5193: ('industry.id', 69, 10), 5286: ('industry.id', 72, 40), 5361: ('temp_storage.var_use_fence_ne', 73, 39), 5436: ('temp_storage.var_use_fence_ne', 73, 114), 5508: ('temp_storage.var_use_fence_nw', 74, 39), 5583: ('temp_storage.var_use_fence_nw', 74, 114), 5655: ('temp_storage.var_use_fence_se', 75, 39), 5730: ('temp_storage.var_use_fence_se', 75, 114), 5802: ('temp_storage.var_use_fence_sw', 76, 39), 5877: ('temp_storage.var_use_fence_sw', 76, 114), 5937: ('industry.id', 78, 10), 6017: ('industry.id', 81, 40), 6077: ('temp_storage.var_fencesprite_ne', 82, 32), 6144: ('temp_storage.var_fencesprite_nw', 83, 32), 6211: ('temp_storage.var_fencesprite_se', 84, 32), 6278: ('temp_storage.var_fencesprite_sw', 85, 32), 6346: ('temp_storage.var_use_fence_ne', 87, 32), 6411: ('temp_storage.var_use_fence_nw', 88, 32), 6476: ('temp_storage.var_use_fence_se', 89, 32), 6541: ('temp_storage.var_use_fence_sw', 90, 32), 6607: ('temp_storage.var_fence_offset_ne', 92, 32), 6675: ('temp_storage.var_fence_offset_nw', 93, 32), 6743: ('temp_storage.var_fence_offset_se', 94, 32), 6811: ('temp_storage.var_fence_offset_sw', 95, 32), 6878: ('industry.id', 97, 10)}

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
            __append('\n\n')
            __backup_temp_storage_139913549219376 = get('temp_storage', __marker)

            # <Value 'global_constants.temp_storage_graphics_chain' (8:32)> -> __value
            __token = 626
            __value = _lookup_attr(getitem('global_constants'), 'temp_storage_graphics_chain')
            econtext['temp_storage'] = __value
            __append('\n')
            __append('\n    ')
            __append('\n    ')
            __backup_graphics_switch_139913549510360 = get('graphics_switch', __marker)

            # <Value 'industry.extra_graphics_switches' (11:57)> -> __iterator
            __token = 997
            __iterator = _lookup_attr(getitem('industry'), 'extra_graphics_switches')
            (__iterator, ____index_139913550092048, ) = getitem('repeat')('graphics_switch', __iterator)
            econtext['graphics_switch'] = None
            for __item in __iterator:
                econtext['graphics_switch'] = __item
                __append('\n        ')

                # <Interpolation value=<Substitution '\n        switch(FEAT_INDUSTRYTILES, SELF, ${graphics_switch.id}, nearby_tile_slope(0,0)) {\n            ' (12:121)> braces_required=True translation=False at 7f402973d400> -> __content_139913568826456
                __token = 1162
                __token = 1197
                __content_139913568826456 = _lookup_attr(getitem('graphics_switch'), 'id')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n        switch(FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ', nearby_tile_slope(0,0)) {\n            ', ))
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
                __backup_slope_spritelayout_139913548908920 = get('slope_spritelayout', __marker)

                # <Value 'graphics_switch.slope_spritelayout_mapping.items()' (14:71)> -> __iterator
                __token = 1315
                __iterator = _lookup_attr(_lookup_attr(getitem('graphics_switch'), 'slope_spritelayout_mapping'), 'items')()
                (__iterator, ____index_139913550093336, ) = getitem('repeat')('slope_spritelayout', __iterator)
                econtext['slope_spritelayout'] = None
                for __item in __iterator:
                    econtext['slope_spritelayout'] = __item

                    # <Interpolation value=<Substitution '\n                ${slope_spritelayout[0]}: ${slope_spritelayout[1]};\n            ' (14:123)> braces_required=True translation=False at 7f402977b518> -> __content_139913568826456
                    __token = 1384
                    __token = 1386
                    __content_139913568826456 = getitem('slope_spritelayout')[0]
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 1412
                    __content_139913568826456_1410 = getitem('slope_spritelayout')[1]
                    __content_139913568826456_1410 = __quote(__content_139913568826456_1410, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s' % ('\n                ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ': ', (__content_139913568826456_1410 if (__content_139913568826456_1410 is not None) else ''), ';\n            ', ))
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
                    ____index_139913550093336 -= 1
                    if (____index_139913550093336 > 0):
                        __append('')
                if (__backup_slope_spritelayout_139913548908920 is __marker):
                    del econtext['slope_spritelayout']
                else:
                    econtext['slope_spritelayout'] = __backup_slope_spritelayout_139913548908920

                # <Interpolation value=<Substitution '\n            ${graphics_switch.default_result};\n        }\n    ' (16:45)> braces_required=True translation=False at 7f402973d588> -> __content_139913568826456
                __token = 1494
                __token = 1496
                __content_139913568826456 = _lookup_attr(getitem('graphics_switch'), 'default_result')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n            ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ';\n        }\n    ', ))
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
                ____index_139913550092048 -= 1
                if (____index_139913550092048 > 0):
                    __append('')
            if (__backup_graphics_switch_139913549510360 is __marker):
                del econtext['graphics_switch']
            else:
                econtext['graphics_switch'] = __backup_graphics_switch_139913549510360
            __append('\n\n    ')
            __backup_industry_layout_139913549557376 = get('industry_layout', __marker)

            # <Value 'python:industry.industry_layouts' (21:67)> -> __iterator
            __token = 1642
            __iterator = _lookup_attr(getitem('industry'), 'industry_layouts')
            (__iterator, ____index_139913550346952, ) = getitem('repeat')('industry_layout', __iterator)
            econtext['industry_layout'] = None
            for __item in __iterator:
                econtext['industry_layout'] = __item

                # <Interpolation value=<Substitution '\n        switch(FEAT_INDUSTRYTILES, SELF, ${industry_layout.id}_graphics_switch, relative_pos) {\n            ' (21:101)> braces_required=True translation=False at 7f402977b6a0> -> __content_139913568826456
                __token = 1685
                __token = 1720
                __content_139913568826456 = _lookup_attr(getitem('industry_layout'), 'id')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n        switch(FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_graphics_switch, relative_pos) {\n            ', ))
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
                __backup_layout_139913550347176 = get('layout', __marker)

                # <Value 'industry_layout.layout' (23:54)> -> __iterator
                __token = 1827
                __iterator = _lookup_attr(getitem('industry_layout'), 'layout')
                (__iterator, ____index_139913550344992, ) = getitem('repeat')('layout', __iterator)
                econtext['layout'] = None
                for __item in __iterator:
                    econtext['layout'] = __item

                    # <Interpolation value=<Substitution '\n                relative_coord(${layout[0]}, ${layout[1]}): ${layout[3]};\n            ' (23:78)> braces_required=True translation=False at 7f402977bc50> -> __content_139913568826456
                    __token = 1868
                    __token = 1885
                    __content_139913568826456 = getitem('layout')[0]
                    __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                    __token = 1899
                    __content_139913568826456_1897 = getitem('layout')[1]
                    __content_139913568826456_1897 = __quote(__content_139913568826456_1897, '\x00', '&#0;', None, False)
                    __token = 1914
                    __content_139913568826456_1912 = getitem('layout')[3]
                    __content_139913568826456_1912 = __quote(__content_139913568826456_1912, '\x00', '&#0;', None, False)
                    __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n                relative_coord(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ', ', (__content_139913568826456_1897 if (__content_139913568826456_1897 is not None) else ''), '): ', (__content_139913568826456_1912 if (__content_139913568826456_1912 is not None) else ''), ';\n            ', ))
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
                    ____index_139913550344992 -= 1
                    if (____index_139913550344992 > 0):
                        __append('')
                if (__backup_layout_139913550347176 is __marker):
                    del econtext['layout']
                else:
                    econtext['layout'] = __backup_layout_139913550347176

                # <Interpolation value=<Substitution '\n            ${industry_layout.layout[0][3]}; // a default is needed, but should never be reached, layout definitions are explicit\n        }\n    ' (25:40)> braces_required=True translation=False at 7f402977bdd8> -> __content_139913568826456
                __token = 1979
                __token = 1981
                __content_139913568826456 = _lookup_attr(getitem('industry_layout'), 'layout')[0][3]
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n            ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '; // a default is needed, but should never be reached, layout definitions are explicit\n        }\n    ', ))
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
                ____index_139913550346952 -= 1
                if (____index_139913550346952 > 0):
                    __append('')
            if (__backup_industry_layout_139913549557376 is __marker):
                del econtext['industry_layout']
            else:
                econtext['industry_layout'] = __backup_industry_layout_139913549557376

            # <Interpolation value=<Substitution '\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_graphics_switch_layouts, layout_num) {\n        ' (28:44)> braces_required=True translation=False at 7f402973da58> -> __content_139913568826456
            __token = 2157
            __token = 2194
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s' % ('\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_industry_graphics_switch_layouts, layout_num) {\n        ', ))
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
            __backup_layout_num_139913549274640 = get('layout_num', __marker)

            # <Value 'range(len(industry.industry_layouts))' (31:59)> -> __iterator
            __token = 2314
            __iterator = get('range', range)(len(_lookup_attr(getitem('industry'), 'industry_layouts')))
            (__iterator, ____index_139913550344488, ) = getitem('repeat')('layout_num', __iterator)
            econtext['layout_num'] = None
            for __item in __iterator:
                econtext['layout_num'] = __item

                # <Interpolation value=<Substitution '\n            ${layout_num+1}: ${industry.industry_layouts[layout_num].id}_graphics_switch;\n        ' (31:98)> braces_required=True translation=False at 7f402977bd30> -> __content_139913568826456
                __token = 2366
                __token = 2368
                __content_139913568826456 = (getitem('layout_num') + 1)
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 2385
                __content_139913568826456_2383 = _lookup_attr(_lookup_attr(getitem('industry'), 'industry_layouts')[getitem('layout_num')], 'id')
                __content_139913568826456_2383 = __quote(__content_139913568826456_2383, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s' % ('\n            ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ': ', (__content_139913568826456_2383 if (__content_139913568826456_2383 is not None) else ''), '_graphics_switch;\n        ', ))
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
                ____index_139913550344488 -= 1
                if (____index_139913550344488 > 0):
                    __append('')
            if (__backup_layout_num_139913549274640 is __marker):
                del econtext['layout_num']
            else:
                econtext['layout_num'] = __backup_layout_num_139913549274640

            # <Interpolation value=<Substitution '\n        ${industry.industry_layouts[0].id}_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ${industry.get_switch_name_for_construction_states()};\n        ${industry.id}_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ${temp_storage.var_terrain_is_snow})\n                ' (33:41)> braces_required=True translation=False at 7f402977bf28> -> __content_139913568826456
            __token = 2494
            __token = 2496
            __content_139913568826456 = _lookup_attr(_lookup_attr(getitem('industry'), 'industry_layouts')[0], 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 2603
            __content_139913568826456_2601 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_2601 = __quote(__content_139913568826456_2601, '\x00', '&#0;', None, False)
            __token = 2699
            __content_139913568826456_2697 = _lookup_attr(getitem('industry'), 'get_switch_name_for_construction_states')()
            __content_139913568826456_2697 = __quote(__content_139913568826456_2697, '\x00', '&#0;', None, False)
            __token = 2762
            __content_139913568826456_2760 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_2760 = __quote(__content_139913568826456_2760, '\x00', '&#0;', None, False)
            __token = 2866
            __content_139913568826456_2864 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_2864 = __quote(__content_139913568826456_2864, '\x00', '&#0;', None, False)
            __token = 2953
            __content_139913568826456_2951 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
            __content_139913568826456_2951 = __quote(__content_139913568826456_2951, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456_2601 if (__content_139913568826456_2601 is not None) else ''), '_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ', (__content_139913568826456_2697 if (__content_139913568826456_2697 is not None) else ''), ';\n        ', (__content_139913568826456_2760 if (__content_139913568826456_2760 is not None) else ''), '_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456_2864 if (__content_139913568826456_2864 is not None) else ''), '_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ', (__content_139913568826456_2951 if (__content_139913568826456_2951 is not None) else ''), ')\n                ', ))
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
            __backup_date_variation_num_139913549861720 = get('date_variation_num', __marker)

            # <Value 'range(len(industry.graphics_change_dates)+1)' (44:64)> -> __iterator
            __token = 3052
            __iterator = get('range', range)((len(_lookup_attr(getitem('industry'), 'graphics_change_dates')) + 1))
            (__iterator, ____index_139913550345776, ) = getitem('repeat')('date_variation_num', __iterator)
            econtext['date_variation_num'] = None
            for __item in __iterator:
                econtext['date_variation_num'] = __item

                # <Interpolation value=<Substitution '\n                    , STORE_TEMP(${industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)},\n                                 ${255 - date_variation_num}) ' (44:166)> braces_required=True translation=False at 7f402977b5f8> -> __content_139913568826456
                __token = 3175
                __token = 3190
                __content_139913568826456 = _lookup_attr(getitem('industry'), 'get_date_conditions_for_hide_sprites')(_lookup_attr(_lookup_attr(getitem('repeat'), 'date_variation_num'), 'index'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 3306
                __content_139913568826456_3304 = (255 - getitem('date_variation_num'))
                __content_139913568826456_3304 = __quote(__content_139913568826456_3304, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s' % ('\n                    , STORE_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ',\n                                 ', (__content_139913568826456_3304 if (__content_139913568826456_3304 is not None) else ''), ') ', ))
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

                # <Interpolation value=<Substitution '\n                    , STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(${255 - date_variation_num}),\n                                 ${255 - date_variation_num})\n                    , STORE_TEMP(LOAD_TEMP(${temp_storage.var_terrain_is_snow}) == 0 ? 1 : LOAD_TEMP(${255 - date_variation_num}), ' (46:118)> braces_required=True translation=False at 7f402977b9b0> -> __content_139913568826456
                __token = 3410
                __token = 3465
                __content_139913568826456 = (255 - getitem('date_variation_num'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 3528
                __content_139913568826456_3526 = (255 - getitem('date_variation_num'))
                __content_139913568826456_3526 = __quote(__content_139913568826456_3526, '\x00', '&#0;', None, False)
                __token = 3600
                __content_139913568826456_3598 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456_3598 = __quote(__content_139913568826456_3598, '\x00', '&#0;', None, False)
                __token = 3658
                __content_139913568826456_3656 = (255 - getitem('date_variation_num'))
                __content_139913568826456_3656 = __quote(__content_139913568826456_3656, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s' % ('\n                    , STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '),\n                                 ', (__content_139913568826456_3526 if (__content_139913568826456_3526 is not None) else ''), ')\n                    , STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_3598 if (__content_139913568826456_3598 is not None) else ''), ') == 0 ? 1 : LOAD_TEMP(', (__content_139913568826456_3656 if (__content_139913568826456_3656 is not None) else ''), '), ', ))
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

                # <Interpolation value=<Substitution '\n                                 ${245 - date_variation_num}) ' (49:170)> braces_required=True translation=False at 7f402977b160> -> __content_139913568826456
                __token = 3759
                __token = 3761
                __content_139913568826456 = (245 - getitem('date_variation_num'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n                                 ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ') ', ))
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

                # <Interpolation value=<Substitution '\n                    , STORE_TEMP(LOAD_TEMP(${temp_storage.var_terrain_is_snow}) == 1 ? 1 : LOAD_TEMP(${255 - date_variation_num}), ' (50:135)> braces_required=True translation=False at 7f402977b198> -> __content_139913568826456
                __token = 3882
                __token = 3907
                __content_139913568826456 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 3965
                __content_139913568826456_3963 = (255 - getitem('date_variation_num'))
                __content_139913568826456_3963 = __quote(__content_139913568826456_3963, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s' % ('\n                    , STORE_TEMP(LOAD_TEMP(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ') == 1 ? 1 : LOAD_TEMP(', (__content_139913568826456_3963 if (__content_139913568826456_3963 is not None) else ''), '), ', ))
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

                # <Interpolation value=<Substitution '\n                                 ${255 - date_variation_num})\n                ' (51:154)> braces_required=True translation=False at 7f402977b6d8> -> __content_139913568826456
                __token = 4050
                __token = 4052
                __content_139913568826456 = (255 - getitem('date_variation_num'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s' % ('\n                                 ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ')\n                ', ))
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
                ____index_139913550345776 -= 1
                if (____index_139913550345776 > 0):
                    __append('')
            if (__backup_date_variation_num_139913549861720 is __marker):
                del econtext['date_variation_num']
            else:
                econtext['date_variation_num'] = __backup_date_variation_num_139913549861720

            # <Interpolation value=<Substitution '\n            ]) {\n        ${industry.id}_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_master_graphics_switch, STORE_TEMP(random_bits, ${temp_storage.var_random_bits})) {\n        ${industry.id}_store_temp_vars; // default\n    }\n\n    ' (53:38)> braces_required=True translation=False at 7f402977beb8> -> __content_139913568826456
            __token = 4130
            __token = 4145
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 4262
            __content_139913568826456_4260 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_4260 = __quote(__content_139913568826456_4260, '\x00', '&#0;', None, False)
            __token = 4334
            __content_139913568826456_4332 = _lookup_attr(getitem('temp_storage'), 'var_random_bits')
            __content_139913568826456_4332 = __quote(__content_139913568826456_4332, '\x00', '&#0;', None, False)
            __token = 4378
            __content_139913568826456_4376 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_4376 = __quote(__content_139913568826456_4376, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s' % ('\n            ]) {\n        ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ', (__content_139913568826456_4260 if (__content_139913568826456_4260 is not None) else ''), '_industry_master_graphics_switch, STORE_TEMP(random_bits, ', (__content_139913568826456_4332 if (__content_139913568826456_4332 is not None) else ''), ')) {\n        ', (__content_139913568826456_4376 if (__content_139913568826456_4376 is not None) else ''), '_store_temp_vars; // default\n    }\n\n    ', ))
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * !nearby_tile_is_same_industry(-1,  0), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * !nearby_tile_is_same_industry( 0, -1), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * !nearby_tile_is_same_industry( 0,  1), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * !nearby_tile_is_same_industry( 1,  0), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fences, [\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_se}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_sw}),\n\n                STORE_TEMP(1, ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_sw}),\n\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_se}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_sw}),\n                ]) {\n        ${industry.id}_tile_fence_industry;\n    }\n    ' (62:28)> braces_required=True translation=False at 7f402977be10> -> __content_139913568826456
            __token = 4459
            __token = 4495
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 4569
            __content_139913568826456_4567 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_139913568826456_4567 = __quote(__content_139913568826456_4567, '\x00', '&#0;', None, False)
            __token = 4656
            __content_139913568826456_4654 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_139913568826456_4654 = __quote(__content_139913568826456_4654, '\x00', '&#0;', None, False)
            __token = 4728
            __content_139913568826456_4726 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_139913568826456_4726 = __quote(__content_139913568826456_4726, '\x00', '&#0;', None, False)
            __token = 4815
            __content_139913568826456_4813 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_139913568826456_4813 = __quote(__content_139913568826456_4813, '\x00', '&#0;', None, False)
            __token = 4887
            __content_139913568826456_4885 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_139913568826456_4885 = __quote(__content_139913568826456_4885, '\x00', '&#0;', None, False)
            __token = 4974
            __content_139913568826456_4972 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_139913568826456_4972 = __quote(__content_139913568826456_4972, '\x00', '&#0;', None, False)
            __token = 5046
            __content_139913568826456_5044 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_139913568826456_5044 = __quote(__content_139913568826456_5044, '\x00', '&#0;', None, False)
            __token = 5133
            __content_139913568826456_5131 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_139913568826456_5131 = __quote(__content_139913568826456_5131, '\x00', '&#0;', None, False)
            __token = 5193
            __content_139913568826456_5191 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_5191 = __quote(__content_139913568826456_5191, '\x00', '&#0;', None, False)
            __token = 5286
            __content_139913568826456_5284 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_5284 = __quote(__content_139913568826456_5284, '\x00', '&#0;', None, False)
            __token = 5361
            __content_139913568826456_5359 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_139913568826456_5359 = __quote(__content_139913568826456_5359, '\x00', '&#0;', None, False)
            __token = 5436
            __content_139913568826456_5434 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_139913568826456_5434 = __quote(__content_139913568826456_5434, '\x00', '&#0;', None, False)
            __token = 5508
            __content_139913568826456_5506 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_139913568826456_5506 = __quote(__content_139913568826456_5506, '\x00', '&#0;', None, False)
            __token = 5583
            __content_139913568826456_5581 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_139913568826456_5581 = __quote(__content_139913568826456_5581, '\x00', '&#0;', None, False)
            __token = 5655
            __content_139913568826456_5653 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_139913568826456_5653 = __quote(__content_139913568826456_5653, '\x00', '&#0;', None, False)
            __token = 5730
            __content_139913568826456_5728 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_139913568826456_5728 = __quote(__content_139913568826456_5728, '\x00', '&#0;', None, False)
            __token = 5802
            __content_139913568826456_5800 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_139913568826456_5800 = __quote(__content_139913568826456_5800, '\x00', '&#0;', None, False)
            __token = 5877
            __content_139913568826456_5875 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_139913568826456_5875 = __quote(__content_139913568826456_5875, '\x00', '&#0;', None, False)
            __token = 5937
            __content_139913568826456_5935 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_5935 = __quote(__content_139913568826456_5935, '\x00', '&#0;', None, False)
            __token = 6017
            __content_139913568826456_6015 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_6015 = __quote(__content_139913568826456_6015, '\x00', '&#0;', None, False)
            __token = 6077
            __content_139913568826456_6075 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_ne')
            __content_139913568826456_6075 = __quote(__content_139913568826456_6075, '\x00', '&#0;', None, False)
            __token = 6144
            __content_139913568826456_6142 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_nw')
            __content_139913568826456_6142 = __quote(__content_139913568826456_6142, '\x00', '&#0;', None, False)
            __token = 6211
            __content_139913568826456_6209 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_se')
            __content_139913568826456_6209 = __quote(__content_139913568826456_6209, '\x00', '&#0;', None, False)
            __token = 6278
            __content_139913568826456_6276 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_sw')
            __content_139913568826456_6276 = __quote(__content_139913568826456_6276, '\x00', '&#0;', None, False)
            __token = 6346
            __content_139913568826456_6344 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_139913568826456_6344 = __quote(__content_139913568826456_6344, '\x00', '&#0;', None, False)
            __token = 6411
            __content_139913568826456_6409 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_139913568826456_6409 = __quote(__content_139913568826456_6409, '\x00', '&#0;', None, False)
            __token = 6476
            __content_139913568826456_6474 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_139913568826456_6474 = __quote(__content_139913568826456_6474, '\x00', '&#0;', None, False)
            __token = 6541
            __content_139913568826456_6539 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_139913568826456_6539 = __quote(__content_139913568826456_6539, '\x00', '&#0;', None, False)
            __token = 6607
            __content_139913568826456_6605 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_ne')
            __content_139913568826456_6605 = __quote(__content_139913568826456_6605, '\x00', '&#0;', None, False)
            __token = 6675
            __content_139913568826456_6673 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_nw')
            __content_139913568826456_6673 = __quote(__content_139913568826456_6673, '\x00', '&#0;', None, False)
            __token = 6743
            __content_139913568826456_6741 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_se')
            __content_139913568826456_6741 = __quote(__content_139913568826456_6741, '\x00', '&#0;', None, False)
            __token = 6811
            __content_139913568826456_6809 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_sw')
            __content_139913568826456_6809 = __quote(__content_139913568826456_6809, '\x00', '&#0;', None, False)
            __token = 6878
            __content_139913568826456_6876 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_6876 = __quote(__content_139913568826456_6876, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_4567 if (__content_139913568826456_4567 is not None) else ''), ') * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ', (__content_139913568826456_4654 if (__content_139913568826456_4654 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_4726 if (__content_139913568826456_4726 is not None) else ''), ') * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ', (__content_139913568826456_4813 if (__content_139913568826456_4813 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_4885 if (__content_139913568826456_4885 is not None) else ''), ') * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ', (__content_139913568826456_4972 if (__content_139913568826456_4972 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_5044 if (__content_139913568826456_5044 is not None) else ''), ') * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ', (__content_139913568826456_5131 if (__content_139913568826456_5131 is not None) else ''), '),\n            ]) {\n        ', (__content_139913568826456_5191 if (__content_139913568826456_5191 is not None) else ''), '_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456_5284 if (__content_139913568826456_5284 is not None) else ''), '_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_5359 if (__content_139913568826456_5359 is not None) else ''), ') * !nearby_tile_is_same_industry(-1,  0), ', (__content_139913568826456_5434 if (__content_139913568826456_5434 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_5506 if (__content_139913568826456_5506 is not None) else ''), ') * !nearby_tile_is_same_industry( 0, -1), ', (__content_139913568826456_5581 if (__content_139913568826456_5581 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_5653 if (__content_139913568826456_5653 is not None) else ''), ') * !nearby_tile_is_same_industry( 0,  1), ', (__content_139913568826456_5728 if (__content_139913568826456_5728 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_139913568826456_5800 if (__content_139913568826456_5800 is not None) else ''), ') * !nearby_tile_is_same_industry( 1,  0), ', (__content_139913568826456_5875 if (__content_139913568826456_5875 is not None) else ''), '),\n            ]) {\n        ', (__content_139913568826456_5935 if (__content_139913568826456_5935 is not None) else ''), '_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_139913568826456_6015 if (__content_139913568826456_6015 is not None) else ''), '_tile_fences, [\n                STORE_TEMP(0, ', (__content_139913568826456_6075 if (__content_139913568826456_6075 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6142 if (__content_139913568826456_6142 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6209 if (__content_139913568826456_6209 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6276 if (__content_139913568826456_6276 is not None) else ''), '),\n\n                STORE_TEMP(1, ', (__content_139913568826456_6344 if (__content_139913568826456_6344 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_139913568826456_6409 if (__content_139913568826456_6409 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_139913568826456_6474 if (__content_139913568826456_6474 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_139913568826456_6539 if (__content_139913568826456_6539 is not None) else ''), '),\n\n                STORE_TEMP(0, ', (__content_139913568826456_6605 if (__content_139913568826456_6605 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6673 if (__content_139913568826456_6673 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6741 if (__content_139913568826456_6741 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_139913568826456_6809 if (__content_139913568826456_6809 is not None) else ''), '),\n                ]) {\n        ', (__content_139913568826456_6876 if (__content_139913568826456_6876 is not None) else ''), '_tile_fence_industry;\n    }\n    ', ))
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
            __append('\n')
            if (__backup_temp_storage_139913549219376 is __marker):
                del econtext['temp_storage']
            else:
                econtext['temp_storage'] = __backup_temp_storage_139913549219376
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }