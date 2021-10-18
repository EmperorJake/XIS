# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/graphics_switches.pynml'

__tokens = {626: ('global_constants.temp_storage_graphics_chain', 8, 32), 997: ('industry.extra_graphics_switches', 11, 57), 1162: ('switch(FEAT_INDUSTRYTILES, SELF, ${graphics_switch.id}, nearby_tile_slope(0,0)) {', 13, 8), 1197: ('graphics_switch.id', 13, 43), 1315: ('graphics_switch.slope_spritelayout_mapping.items()', 14, 71), 1384: ('${slope_spritelayout[0]}: ${slope_spritelayout[1]};', 15, 16), 1386: ('slope_spritelayout[0]', 15, 18), 1412: ('slope_spritelayout[1]', 15, 44), 1494: ('${graphics_switch.default_result};\n        }', 17, 12), 1496: ('graphics_switch.default_result', 17, 14), 1642: ('python:industry.industry_layouts', 21, 67), 1685: ('switch(FEAT_INDUSTRYTILES, SELF, ${industry_layout.id}_graphics_switch, relative_pos) {', 22, 8), 1720: ('industry_layout.id', 22, 43), 1827: ('industry_layout.layout', 23, 54), 1868: ('relative_coord(${layout[0]}, ${layout[1]}): ${layout[3]};', 24, 16), 1885: ('layout[0]', 24, 33), 1899: ('layout[1]', 24, 47), 1914: ('layout[3]', 24, 62), 1979: ('${industry_layout.layout[0][3]}; // a default is needed, but should never be reached, layout definitions are explicit\n        }', 26, 12), 1981: ('industry_layout.layout[0][3]', 26, 14), 2157: ('switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_graphics_switch_layouts, layout_num) {', 30, 4), 2194: ('industry.id', 30, 41), 2314: ('range(len(industry.industry_layouts))', 31, 59), 2366: ('${layout_num+1}: ${industry.industry_layouts[layout_num].id}_graphics_switch;', 32, 12), 2368: ('layout_num+1', 32, 14), 2385: ('industry.industry_layouts[layout_num].id', 32, 31), 2494: ('${industry.industry_layouts[0].id}_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ${industry.get_switch_name_for_construction_states()};\n        ${industry.id}_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ${temp_storage.var_terrain_is_snow})', 34, 8), 2496: ('industry.industry_layouts[0].id', 34, 10), 2603: ('industry.id', 37, 39), 2699: ('industry.get_switch_name_for_construction_states()', 38, 16), 2762: ('industry.id', 39, 10), 2866: ('industry.id', 42, 39), 2953: ('temp_storage.var_terrain_is_snow', 43, 57), 3052: ('range(len(industry.graphics_change_dates)+1)', 44, 64), 3175: (', STORE_TEMP(${industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)},\n                             ${127 - date_variation_num})', 45, 20), 3190: ('industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)', 45, 35), 3302: ('127 - date_variation_num', 46, 31), 3391: (', STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(${127 - date_variation_num}),\n                             ${127 - date_variation_num})\n\t\t\t\t\t, STORE_TEMP(LOAD_TEMP(${graphics_temp_storage.var_terrain_is_snow}) == 0 ? 1 : LOAD_TEMP(${127 - date_variation_num}),', 47, 5), 3446: ('127 - date_variation_num', 47, 60), 3505: ('127 - date_variation_num', 48, 31), 3562: ('graphics_temp_storage.var_terrain_is_snow', 49, 30), 3629: ('127 - date_variation_num', 49, 97), 3726: ('${117 - date_variation_num})', 50, 29), 3728: ('117 - date_variation_num', 50, 31), 3834: (', STORE_TEMP(LOAD_TEMP(${graphics_temp_storage.var_terrain_is_snow}) == 1 ? 1 : LOAD_TEMP(${127 - date_variation_num}),', 51, 5), 3859: ('graphics_temp_storage.var_terrain_is_snow', 51, 30), 3926: ('127 - date_variation_num', 51, 97), 4007: ('${127 - date_variation_num})', 52, 29), 4009: ('127 - date_variation_num', 52, 31), 4087: (']) {\n        ${industry.id}_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_master_graphics_switch, STORE_TEMP(random_bits, ${temp_storage.var_random_bits})) {\n        ${industry.id}_store_temp_vars; // default\n    }', 54, 12), 4102: ('industry.id', 55, 10), 4219: ('industry.id', 58, 41), 4291: ('temp_storage.var_random_bits', 58, 113), 4335: ('industry.id', 59, 10), 4416: ('switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * !nearby_tile_is_same_industry(-1,  0), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * !nearby_tile_is_same_industry( 0, -1), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * !nearby_tile_is_same_industry( 0,  1), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * !nearby_tile_is_same_industry( 1,  0), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fences, [\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_se}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_sw}),\n\n                STORE_TEMP(1, ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_sw}),\n\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_se}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_sw}),\n                ]) {\n        ${industry.id}_tile_fence_industry;\n    }', 63, 4), 4452: ('industry.id', 63, 40), 4526: ('temp_storage.var_use_fence_ne', 64, 39), 4613: ('temp_storage.var_use_fence_ne', 64, 126), 4685: ('temp_storage.var_use_fence_nw', 65, 39), 4772: ('temp_storage.var_use_fence_nw', 65, 126), 4844: ('temp_storage.var_use_fence_se', 66, 39), 4931: ('temp_storage.var_use_fence_se', 66, 126), 5003: ('temp_storage.var_use_fence_sw', 67, 39), 5090: ('temp_storage.var_use_fence_sw', 67, 126), 5150: ('industry.id', 69, 10), 5243: ('industry.id', 72, 40), 5318: ('temp_storage.var_use_fence_ne', 73, 39), 5393: ('temp_storage.var_use_fence_ne', 73, 114), 5465: ('temp_storage.var_use_fence_nw', 74, 39), 5540: ('temp_storage.var_use_fence_nw', 74, 114), 5612: ('temp_storage.var_use_fence_se', 75, 39), 5687: ('temp_storage.var_use_fence_se', 75, 114), 5759: ('temp_storage.var_use_fence_sw', 76, 39), 5834: ('temp_storage.var_use_fence_sw', 76, 114), 5894: ('industry.id', 78, 10), 5974: ('industry.id', 81, 40), 6034: ('temp_storage.var_fencesprite_ne', 82, 32), 6101: ('temp_storage.var_fencesprite_nw', 83, 32), 6168: ('temp_storage.var_fencesprite_se', 84, 32), 6235: ('temp_storage.var_fencesprite_sw', 85, 32), 6303: ('temp_storage.var_use_fence_ne', 87, 32), 6368: ('temp_storage.var_use_fence_nw', 88, 32), 6433: ('temp_storage.var_use_fence_se', 89, 32), 6498: ('temp_storage.var_use_fence_sw', 90, 32), 6564: ('temp_storage.var_fence_offset_ne', 92, 32), 6632: ('temp_storage.var_fence_offset_nw', 93, 32), 6700: ('temp_storage.var_fence_offset_se', 94, 32), 6768: ('temp_storage.var_fence_offset_sw', 95, 32), 6835: ('industry.id', 97, 10)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_140036458220608 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
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

            # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452972720
            __attrs_140036452972720 = _static_140036458220608
            __backup_temp_storage_140036454565152 = get('temp_storage', __marker)

            # <Value 'global_constants.temp_storage_graphics_chain' (8:32)> -> __value
            __token = 626
            __value = _lookup_attr(getitem('global_constants'), 'temp_storage_graphics_chain')
            econtext['temp_storage'] = __value
            __append('\n\n    \n    ')

            # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452973440
            __attrs_140036452973440 = _static_140036458220608
            __backup_graphics_switch_140036452971328 = get('graphics_switch', __marker)

            # <Value 'industry.extra_graphics_switches' (11:57)> -> __iterator
            __token = 997
            __iterator = _lookup_attr(getitem('industry'), 'extra_graphics_switches')
            (__iterator, ____index_140036452974496, ) = getitem('repeat')('graphics_switch', __iterator)
            econtext['graphics_switch'] = None
            for __item in __iterator:
                econtext['graphics_switch'] = __item
                __append('\n        ')

                # <Interpolation value=<Substitution '\n        switch(FEAT_INDUSTRYTILES, SELF, ${graphics_switch.id}, nearby_tile_slope(0,0)) {\n            ' (12:121)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a130> -> __content_140036462745328
                __token = 1162
                __token = 1197
                __content_140036462745328 = _lookup_attr(getitem('graphics_switch'), 'id')
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n        switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ', nearby_tile_slope(0,0)) {\n            ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452689424
                __attrs_140036452689424 = _static_140036458220608
                __backup_slope_spritelayout_140036452971856 = get('slope_spritelayout', __marker)

                # <Value 'graphics_switch.slope_spritelayout_mapping.items()' (14:71)> -> __iterator
                __token = 1315
                __iterator = _lookup_attr(_lookup_attr(getitem('graphics_switch'), 'slope_spritelayout_mapping'), 'items')()
                (__iterator, ____index_140036452688272, ) = getitem('repeat')('slope_spritelayout', __iterator)
                econtext['slope_spritelayout'] = None
                for __item in __iterator:
                    econtext['slope_spritelayout'] = __item

                    # <Interpolation value=<Substitution '\n                ${slope_spritelayout[0]}: ${slope_spritelayout[1]};\n            ' (14:123)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a730> -> __content_140036462745328
                    __token = 1384
                    __token = 1386
                    __content_140036462745328 = getitem('slope_spritelayout')[0]
                    __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                    __token = 1412
                    __content_140036462745328_1410 = getitem('slope_spritelayout')[1]
                    __content_140036462745328_1410 = __quote(__content_140036462745328_1410, '\x00', '&#0;', None, None)
                    __content_140036462745328 = ('%s%s%s%s%s' % ('\n                ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ': ', (__content_140036462745328_1410 if (__content_140036462745328_1410 is not None) else ''), ';\n            ', ))
                    if (__content_140036462745328 is None):
                        pass
                    else:
                        if (__content_140036462745328 is None):
                            __content_140036462745328 = None
                        else:
                            __tt = type(__content_140036462745328)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140036462745328 = str(__content_140036462745328)
                            else:
                                if (__tt is bytes):
                                    __content_140036462745328 = decode(__content_140036462745328)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140036462745328 = __content_140036462745328.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140036462745328)
                                            __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                        else:
                                            __content_140036462745328 = __content_140036462745328()
                    if (__content_140036462745328 is not None):
                        __append(__content_140036462745328)
                    ____index_140036452688272 -= 1
                    if (____index_140036452688272 > 0):
                        __append('')
                if (__backup_slope_spritelayout_140036452971856 is __marker):
                    del econtext['slope_spritelayout']
                else:
                    econtext['slope_spritelayout'] = __backup_slope_spritelayout_140036452971856

                # <Interpolation value=<Substitution '\n            ${graphics_switch.default_result};\n        }\n    ' (16:45)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a220> -> __content_140036462745328
                __token = 1494
                __token = 1496
                __content_140036462745328 = _lookup_attr(getitem('graphics_switch'), 'default_result')
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n            ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ';\n        }\n    ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)
                ____index_140036452974496 -= 1
                if (____index_140036452974496 > 0):
                    __append('')
            if (__backup_graphics_switch_140036452971328 is __marker):
                del econtext['graphics_switch']
            else:
                econtext['graphics_switch'] = __backup_graphics_switch_140036452971328
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452688560
            __attrs_140036452688560 = _static_140036458220608
            __backup_industry_layout_140036452973248 = get('industry_layout', __marker)

            # <Value 'python:industry.industry_layouts' (21:67)> -> __iterator
            __token = 1642
            __iterator = _lookup_attr(getitem('industry'), 'industry_layouts')
            (__iterator, ____index_140036452688368, ) = getitem('repeat')('industry_layout', __iterator)
            econtext['industry_layout'] = None
            for __item in __iterator:
                econtext['industry_layout'] = __item

                # <Interpolation value=<Substitution '\n        switch(FEAT_INDUSTRYTILES, SELF, ${industry_layout.id}_graphics_switch, relative_pos) {\n            ' (21:101)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a850> -> __content_140036462745328
                __token = 1685
                __token = 1720
                __content_140036462745328 = _lookup_attr(getitem('industry_layout'), 'id')
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n        switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '_graphics_switch, relative_pos) {\n            ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452690912
                __attrs_140036452690912 = _static_140036458220608
                __backup_layout_140036452972816 = get('layout', __marker)

                # <Value 'industry_layout.layout' (23:54)> -> __iterator
                __token = 1827
                __iterator = _lookup_attr(getitem('industry_layout'), 'layout')
                (__iterator, ____index_140036452690480, ) = getitem('repeat')('layout', __iterator)
                econtext['layout'] = None
                for __item in __iterator:
                    econtext['layout'] = __item

                    # <Interpolation value=<Substitution '\n                relative_coord(${layout[0]}, ${layout[1]}): ${layout[3]};\n            ' (23:78)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704ad30> -> __content_140036462745328
                    __token = 1868
                    __token = 1885
                    __content_140036462745328 = getitem('layout')[0]
                    __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                    __token = 1899
                    __content_140036462745328_1897 = getitem('layout')[1]
                    __content_140036462745328_1897 = __quote(__content_140036462745328_1897, '\x00', '&#0;', None, None)
                    __token = 1914
                    __content_140036462745328_1912 = getitem('layout')[3]
                    __content_140036462745328_1912 = __quote(__content_140036462745328_1912, '\x00', '&#0;', None, None)
                    __content_140036462745328 = ('%s%s%s%s%s%s%s' % ('\n                relative_coord(', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ', ', (__content_140036462745328_1897 if (__content_140036462745328_1897 is not None) else ''), '): ', (__content_140036462745328_1912 if (__content_140036462745328_1912 is not None) else ''), ';\n            ', ))
                    if (__content_140036462745328 is None):
                        pass
                    else:
                        if (__content_140036462745328 is None):
                            __content_140036462745328 = None
                        else:
                            __tt = type(__content_140036462745328)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140036462745328 = str(__content_140036462745328)
                            else:
                                if (__tt is bytes):
                                    __content_140036462745328 = decode(__content_140036462745328)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140036462745328 = __content_140036462745328.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140036462745328)
                                            __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                        else:
                                            __content_140036462745328 = __content_140036462745328()
                    if (__content_140036462745328 is not None):
                        __append(__content_140036462745328)
                    ____index_140036452690480 -= 1
                    if (____index_140036452690480 > 0):
                        __append('')
                if (__backup_layout_140036452972816 is __marker):
                    del econtext['layout']
                else:
                    econtext['layout'] = __backup_layout_140036452972816

                # <Interpolation value=<Substitution '\n            ${industry_layout.layout[0][3]}; // a default is needed, but should never be reached, layout definitions are explicit\n        }\n    ' (25:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a790> -> __content_140036462745328
                __token = 1979
                __token = 1981
                __content_140036462745328 = _lookup_attr(getitem('industry_layout'), 'layout')[0][3]
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n            ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '; // a default is needed, but should never be reached, layout definitions are explicit\n        }\n    ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)
                ____index_140036452688368 -= 1
                if (____index_140036452688368 > 0):
                    __append('')
            if (__backup_industry_layout_140036452973248 is __marker):
                del econtext['industry_layout']
            else:
                econtext['industry_layout'] = __backup_industry_layout_140036452973248

            # <Interpolation value=<Substitution '\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_graphics_switch_layouts, layout_num) {\n        ' (28:44)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc708fe50> -> __content_140036462745328
            __token = 2157
            __token = 2194
            __content_140036462745328 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
            __content_140036462745328 = ('%s%s%s' % ('\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '_industry_graphics_switch_layouts, layout_num) {\n        ', ))
            if (__content_140036462745328 is None):
                pass
            else:
                if (__content_140036462745328 is None):
                    __content_140036462745328 = None
                else:
                    __tt = type(__content_140036462745328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140036462745328 = str(__content_140036462745328)
                    else:
                        if (__tt is bytes):
                            __content_140036462745328 = decode(__content_140036462745328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140036462745328 = __content_140036462745328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140036462745328)
                                    __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                else:
                                    __content_140036462745328 = __content_140036462745328()
            if (__content_140036462745328 is not None):
                __append(__content_140036462745328)

            # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036452690336
            __attrs_140036452690336 = _static_140036458220608
            __backup_layout_num_140036452973104 = get('layout_num', __marker)

            # <Value 'range(len(industry.industry_layouts))' (31:59)> -> __iterator
            __token = 2314
            __iterator = get('range', range)(len(_lookup_attr(getitem('industry'), 'industry_layouts')))
            (__iterator, ____index_140036452691920, ) = getitem('repeat')('layout_num', __iterator)
            econtext['layout_num'] = None
            for __item in __iterator:
                econtext['layout_num'] = __item

                # <Interpolation value=<Substitution '\n            ${layout_num+1}: ${industry.industry_layouts[layout_num].id}_graphics_switch;\n        ' (31:98)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704af10> -> __content_140036462745328
                __token = 2366
                __token = 2368
                __content_140036462745328 = (getitem('layout_num') + 1)
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __token = 2385
                __content_140036462745328_2383 = _lookup_attr(_lookup_attr(getitem('industry'), 'industry_layouts')[getitem('layout_num')], 'id')
                __content_140036462745328_2383 = __quote(__content_140036462745328_2383, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s%s%s' % ('\n            ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ': ', (__content_140036462745328_2383 if (__content_140036462745328_2383 is not None) else ''), '_graphics_switch;\n        ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)
                ____index_140036452691920 -= 1
                if (____index_140036452691920 > 0):
                    __append('')
            if (__backup_layout_num_140036452973104 is __marker):
                del econtext['layout_num']
            else:
                econtext['layout_num'] = __backup_layout_num_140036452973104

            # <Interpolation value=<Substitution '\n        ${industry.industry_layouts[0].id}_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ${industry.get_switch_name_for_construction_states()};\n        ${industry.id}_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ${industry.id}_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ${temp_storage.var_terrain_is_snow})\n                ' (33:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a370> -> __content_140036462745328
            __token = 2494
            __token = 2496
            __content_140036462745328 = _lookup_attr(_lookup_attr(getitem('industry'), 'industry_layouts')[0], 'id')
            __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
            __token = 2603
            __content_140036462745328_2601 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_2601 = __quote(__content_140036462745328_2601, '\x00', '&#0;', None, None)
            __token = 2699
            __content_140036462745328_2697 = _lookup_attr(getitem('industry'), 'get_switch_name_for_construction_states')()
            __content_140036462745328_2697 = __quote(__content_140036462745328_2697, '\x00', '&#0;', None, None)
            __token = 2762
            __content_140036462745328_2760 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_2760 = __quote(__content_140036462745328_2760, '\x00', '&#0;', None, None)
            __token = 2866
            __content_140036462745328_2864 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_2864 = __quote(__content_140036462745328_2864, '\x00', '&#0;', None, None)
            __token = 2953
            __content_140036462745328_2951 = _lookup_attr(getitem('temp_storage'), 'var_terrain_is_snow')
            __content_140036462745328_2951 = __quote(__content_140036462745328_2951, '\x00', '&#0;', None, None)
            __content_140036462745328 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328_2601 if (__content_140036462745328_2601 is not None) else ''), '_industry_construction_state_graphics_switch, construction_state) {\n        0..2: ', (__content_140036462745328_2697 if (__content_140036462745328_2697 is not None) else ''), ';\n        ', (__content_140036462745328_2760 if (__content_140036462745328_2760 is not None) else ''), '_industry_graphics_switch_layouts; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328_2864 if (__content_140036462745328_2864 is not None) else ''), '_store_temp_vars,\n            [STORE_TEMP(terrain_type == TILETYPE_SNOW, ', (__content_140036462745328_2951 if (__content_140036462745328_2951 is not None) else ''), ')\n                ', ))
            if (__content_140036462745328 is None):
                pass
            else:
                if (__content_140036462745328 is None):
                    __content_140036462745328 = None
                else:
                    __tt = type(__content_140036462745328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140036462745328 = str(__content_140036462745328)
                    else:
                        if (__tt is bytes):
                            __content_140036462745328 = decode(__content_140036462745328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140036462745328 = __content_140036462745328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140036462745328)
                                    __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                else:
                                    __content_140036462745328 = __content_140036462745328()
            if (__content_140036462745328 is not None):
                __append(__content_140036462745328)

            # <Static value=<_ast.Dict object at 0x7f5cc7590c40> name=None at 7f5cc7590a60> -> __attrs_140036453085536
            __attrs_140036453085536 = _static_140036458220608
            __backup_date_variation_num_140036452688656 = get('date_variation_num', __marker)

            # <Value 'range(len(industry.graphics_change_dates)+1)' (44:64)> -> __iterator
            __token = 3052
            __iterator = get('range', range)((len(_lookup_attr(getitem('industry'), 'graphics_change_dates')) + 1))
            (__iterator, ____index_140036453086592, ) = getitem('repeat')('date_variation_num', __iterator)
            econtext['date_variation_num'] = None
            for __item in __iterator:
                econtext['date_variation_num'] = __item

                # <Interpolation value=<Substitution '\n                    , STORE_TEMP(${industry.get_date_conditions_for_hide_sprites(repeat.date_variation_num.index)},\n                             ${127 - date_variation_num}) ' (44:166)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab2b0> -> __content_140036462745328
                __token = 3175
                __token = 3190
                __content_140036462745328 = _lookup_attr(getitem('industry'), 'get_date_conditions_for_hide_sprites')(_lookup_attr(_lookup_attr(getitem('repeat'), 'date_variation_num'), 'index'))
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __token = 3302
                __content_140036462745328_3300 = (127 - getitem('date_variation_num'))
                __content_140036462745328_3300 = __quote(__content_140036462745328_3300, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s%s%s' % ('\n                    , STORE_TEMP(', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ',\n                             ', (__content_140036462745328_3300 if (__content_140036462745328_3300 is not None) else ''), ') ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Interpolation value=<Substitution '\n\t\t\t\t\t, STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(${127 - date_variation_num}),\n                             ${127 - date_variation_num})\n\t\t\t\t\t, STORE_TEMP(LOAD_TEMP(${graphics_temp_storage.var_terrain_is_snow}) == 0 ? 1 : LOAD_TEMP(${127 - date_variation_num}), ' (46:114)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab490> -> __content_140036462745328
                __token = 3391
                __token = 3446
                __content_140036462745328 = (127 - getitem('date_variation_num'))
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __token = 3505
                __content_140036462745328_3503 = (127 - getitem('date_variation_num'))
                __content_140036462745328_3503 = __quote(__content_140036462745328_3503, '\x00', '&#0;', None, None)
                __token = 3562
                __content_140036462745328_3560 = _lookup_attr(getitem('graphics_temp_storage'), 'var_terrain_is_snow')
                __content_140036462745328_3560 = __quote(__content_140036462745328_3560, '\x00', '&#0;', None, None)
                __token = 3629
                __content_140036462745328_3627 = (127 - getitem('date_variation_num'))
                __content_140036462745328_3627 = __quote(__content_140036462745328_3627, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s%s%s%s%s%s%s' % ('\n\t\t\t\t\t, STORE_TEMP(construction_state != 3 ? 1 : LOAD_TEMP(', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '),\n                             ', (__content_140036462745328_3503 if (__content_140036462745328_3503 is not None) else ''), ')\n\t\t\t\t\t, STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_3560 if (__content_140036462745328_3560 is not None) else ''), ') == 0 ? 1 : LOAD_TEMP(', (__content_140036462745328_3627 if (__content_140036462745328_3627 is not None) else ''), '), ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Interpolation value=<Substitution '\n                             ${117 - date_variation_num}) ' (49:164)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab700> -> __content_140036462745328
                __token = 3726
                __token = 3728
                __content_140036462745328 = (117 - getitem('date_variation_num'))
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n                             ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ') ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Interpolation value=<Substitution '\n\t\t\t\t\t, STORE_TEMP(LOAD_TEMP(${graphics_temp_storage.var_terrain_is_snow}) == 1 ? 1 : LOAD_TEMP(${127 - date_variation_num}), ' (50:131)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab790> -> __content_140036462745328
                __token = 3834
                __token = 3859
                __content_140036462745328 = _lookup_attr(getitem('graphics_temp_storage'), 'var_terrain_is_snow')
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __token = 3926
                __content_140036462745328_3924 = (127 - getitem('date_variation_num'))
                __content_140036462745328_3924 = __quote(__content_140036462745328_3924, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s%s%s' % ('\n\t\t\t\t\t, STORE_TEMP(LOAD_TEMP(', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ') == 1 ? 1 : LOAD_TEMP(', (__content_140036462745328_3924 if (__content_140036462745328_3924 is not None) else ''), '), ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)

                # <Interpolation value=<Substitution '\n                             ${127 - date_variation_num})\n                ' (51:148)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab820> -> __content_140036462745328
                __token = 4007
                __token = 4009
                __content_140036462745328 = (127 - getitem('date_variation_num'))
                __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
                __content_140036462745328 = ('%s%s%s' % ('\n                             ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), ')\n                ', ))
                if (__content_140036462745328 is None):
                    pass
                else:
                    if (__content_140036462745328 is None):
                        __content_140036462745328 = None
                    else:
                        __tt = type(__content_140036462745328)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140036462745328 = str(__content_140036462745328)
                        else:
                            if (__tt is bytes):
                                __content_140036462745328 = decode(__content_140036462745328)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140036462745328 = __content_140036462745328.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140036462745328)
                                        __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                    else:
                                        __content_140036462745328 = __content_140036462745328()
                if (__content_140036462745328 is not None):
                    __append(__content_140036462745328)
                ____index_140036453086592 -= 1
                if (____index_140036453086592 > 0):
                    __append('')
            if (__backup_date_variation_num_140036452688656 is __marker):
                del econtext['date_variation_num']
            else:
                econtext['date_variation_num'] = __backup_date_variation_num_140036452688656

            # <Interpolation value=<Substitution '\n            ]) {\n        ${industry.id}_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ${industry.id}_industry_master_graphics_switch, STORE_TEMP(random_bits, ${temp_storage.var_random_bits})) {\n        ${industry.id}_store_temp_vars; // default\n    }\n\n    ' (53:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc704a9d0> -> __content_140036462745328
            __token = 4087
            __token = 4102
            __content_140036462745328 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
            __token = 4219
            __content_140036462745328_4217 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_4217 = __quote(__content_140036462745328_4217, '\x00', '&#0;', None, None)
            __token = 4291
            __content_140036462745328_4289 = _lookup_attr(getitem('temp_storage'), 'var_random_bits')
            __content_140036462745328_4289 = __quote(__content_140036462745328_4289, '\x00', '&#0;', None, None)
            __token = 4335
            __content_140036462745328_4333 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_4333 = __quote(__content_140036462745328_4333, '\x00', '&#0;', None, None)
            __content_140036462745328 = ('%s%s%s%s%s%s%s%s%s' % ('\n            ]) {\n        ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '_industry_construction_state_graphics_switch; // default\n    }\n\n    switch(FEAT_INDUSTRYTILES, PARENT, ', (__content_140036462745328_4217 if (__content_140036462745328_4217 is not None) else ''), '_industry_master_graphics_switch, STORE_TEMP(random_bits, ', (__content_140036462745328_4289 if (__content_140036462745328_4289 is not None) else ''), ')) {\n        ', (__content_140036462745328_4333 if (__content_140036462745328_4333 is not None) else ''), '_store_temp_vars; // default\n    }\n\n    ', ))
            if (__content_140036462745328 is None):
                pass
            else:
                if (__content_140036462745328 is None):
                    __content_140036462745328 = None
                else:
                    __tt = type(__content_140036462745328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140036462745328 = str(__content_140036462745328)
                    else:
                        if (__tt is bytes):
                            __content_140036462745328 = decode(__content_140036462745328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140036462745328 = __content_140036462745328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140036462745328)
                                    __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                else:
                                    __content_140036462745328 = __content_140036462745328()
            if (__content_140036462745328 is not None):
                __append(__content_140036462745328)

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_ne}) * !nearby_tile_is_same_industry(-1,  0), ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_nw}) * !nearby_tile_is_same_industry( 0, -1), ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_se}) * !nearby_tile_is_same_industry( 0,  1), ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(LOAD_TEMP(${temp_storage.var_use_fence_sw}) * !nearby_tile_is_same_industry( 1,  0), ${temp_storage.var_use_fence_sw}),\n            ]) {\n        ${industry.id}_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${industry.id}_tile_fences, [\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_se}),\n                STORE_TEMP(0, ${temp_storage.var_fencesprite_sw}),\n\n                STORE_TEMP(1, ${temp_storage.var_use_fence_ne}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_nw}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_se}),\n                STORE_TEMP(1, ${temp_storage.var_use_fence_sw}),\n\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_ne}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_nw}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_se}),\n                STORE_TEMP(0, ${temp_storage.var_fence_offset_sw}),\n                ]) {\n        ${industry.id}_tile_fence_industry;\n    }\n    ' (62:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f5cc70ab0a0> -> __content_140036462745328
            __token = 4416
            __token = 4452
            __content_140036462745328 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328 = __quote(__content_140036462745328, '\x00', '&#0;', None, None)
            __token = 4526
            __content_140036462745328_4524 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_140036462745328_4524 = __quote(__content_140036462745328_4524, '\x00', '&#0;', None, None)
            __token = 4613
            __content_140036462745328_4611 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_140036462745328_4611 = __quote(__content_140036462745328_4611, '\x00', '&#0;', None, None)
            __token = 4685
            __content_140036462745328_4683 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_140036462745328_4683 = __quote(__content_140036462745328_4683, '\x00', '&#0;', None, None)
            __token = 4772
            __content_140036462745328_4770 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_140036462745328_4770 = __quote(__content_140036462745328_4770, '\x00', '&#0;', None, None)
            __token = 4844
            __content_140036462745328_4842 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_140036462745328_4842 = __quote(__content_140036462745328_4842, '\x00', '&#0;', None, None)
            __token = 4931
            __content_140036462745328_4929 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_140036462745328_4929 = __quote(__content_140036462745328_4929, '\x00', '&#0;', None, None)
            __token = 5003
            __content_140036462745328_5001 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_140036462745328_5001 = __quote(__content_140036462745328_5001, '\x00', '&#0;', None, None)
            __token = 5090
            __content_140036462745328_5088 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_140036462745328_5088 = __quote(__content_140036462745328_5088, '\x00', '&#0;', None, None)
            __token = 5150
            __content_140036462745328_5148 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_5148 = __quote(__content_140036462745328_5148, '\x00', '&#0;', None, None)
            __token = 5243
            __content_140036462745328_5241 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_5241 = __quote(__content_140036462745328_5241, '\x00', '&#0;', None, None)
            __token = 5318
            __content_140036462745328_5316 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_140036462745328_5316 = __quote(__content_140036462745328_5316, '\x00', '&#0;', None, None)
            __token = 5393
            __content_140036462745328_5391 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_140036462745328_5391 = __quote(__content_140036462745328_5391, '\x00', '&#0;', None, None)
            __token = 5465
            __content_140036462745328_5463 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_140036462745328_5463 = __quote(__content_140036462745328_5463, '\x00', '&#0;', None, None)
            __token = 5540
            __content_140036462745328_5538 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_140036462745328_5538 = __quote(__content_140036462745328_5538, '\x00', '&#0;', None, None)
            __token = 5612
            __content_140036462745328_5610 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_140036462745328_5610 = __quote(__content_140036462745328_5610, '\x00', '&#0;', None, None)
            __token = 5687
            __content_140036462745328_5685 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_140036462745328_5685 = __quote(__content_140036462745328_5685, '\x00', '&#0;', None, None)
            __token = 5759
            __content_140036462745328_5757 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_140036462745328_5757 = __quote(__content_140036462745328_5757, '\x00', '&#0;', None, None)
            __token = 5834
            __content_140036462745328_5832 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_140036462745328_5832 = __quote(__content_140036462745328_5832, '\x00', '&#0;', None, None)
            __token = 5894
            __content_140036462745328_5892 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_5892 = __quote(__content_140036462745328_5892, '\x00', '&#0;', None, None)
            __token = 5974
            __content_140036462745328_5972 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_5972 = __quote(__content_140036462745328_5972, '\x00', '&#0;', None, None)
            __token = 6034
            __content_140036462745328_6032 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_ne')
            __content_140036462745328_6032 = __quote(__content_140036462745328_6032, '\x00', '&#0;', None, None)
            __token = 6101
            __content_140036462745328_6099 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_nw')
            __content_140036462745328_6099 = __quote(__content_140036462745328_6099, '\x00', '&#0;', None, None)
            __token = 6168
            __content_140036462745328_6166 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_se')
            __content_140036462745328_6166 = __quote(__content_140036462745328_6166, '\x00', '&#0;', None, None)
            __token = 6235
            __content_140036462745328_6233 = _lookup_attr(getitem('temp_storage'), 'var_fencesprite_sw')
            __content_140036462745328_6233 = __quote(__content_140036462745328_6233, '\x00', '&#0;', None, None)
            __token = 6303
            __content_140036462745328_6301 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_ne')
            __content_140036462745328_6301 = __quote(__content_140036462745328_6301, '\x00', '&#0;', None, None)
            __token = 6368
            __content_140036462745328_6366 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_nw')
            __content_140036462745328_6366 = __quote(__content_140036462745328_6366, '\x00', '&#0;', None, None)
            __token = 6433
            __content_140036462745328_6431 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_se')
            __content_140036462745328_6431 = __quote(__content_140036462745328_6431, '\x00', '&#0;', None, None)
            __token = 6498
            __content_140036462745328_6496 = _lookup_attr(getitem('temp_storage'), 'var_use_fence_sw')
            __content_140036462745328_6496 = __quote(__content_140036462745328_6496, '\x00', '&#0;', None, None)
            __token = 6564
            __content_140036462745328_6562 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_ne')
            __content_140036462745328_6562 = __quote(__content_140036462745328_6562, '\x00', '&#0;', None, None)
            __token = 6632
            __content_140036462745328_6630 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_nw')
            __content_140036462745328_6630 = __quote(__content_140036462745328_6630, '\x00', '&#0;', None, None)
            __token = 6700
            __content_140036462745328_6698 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_se')
            __content_140036462745328_6698 = __quote(__content_140036462745328_6698, '\x00', '&#0;', None, None)
            __token = 6768
            __content_140036462745328_6766 = _lookup_attr(getitem('temp_storage'), 'var_fence_offset_sw')
            __content_140036462745328_6766 = __quote(__content_140036462745328_6766, '\x00', '&#0;', None, None)
            __token = 6835
            __content_140036462745328_6833 = _lookup_attr(getitem('industry'), 'id')
            __content_140036462745328_6833 = __quote(__content_140036462745328_6833, '\x00', '&#0;', None, None)
            __content_140036462745328 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328 if (__content_140036462745328 is not None) else ''), '_tile_fence_station, [\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_4524 if (__content_140036462745328_4524 is not None) else ''), ') * (nearby_tile_class(-1,  0) != TILE_CLASS_STATION), ', (__content_140036462745328_4611 if (__content_140036462745328_4611 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_4683 if (__content_140036462745328_4683 is not None) else ''), ') * (nearby_tile_class( 0, -1) != TILE_CLASS_STATION), ', (__content_140036462745328_4770 if (__content_140036462745328_4770 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_4842 if (__content_140036462745328_4842 is not None) else ''), ') * (nearby_tile_class( 0,  1) != TILE_CLASS_STATION), ', (__content_140036462745328_4929 if (__content_140036462745328_4929 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_5001 if (__content_140036462745328_5001 is not None) else ''), ') * (nearby_tile_class( 1,  0) != TILE_CLASS_STATION), ', (__content_140036462745328_5088 if (__content_140036462745328_5088 is not None) else ''), '),\n            ]) {\n        ', (__content_140036462745328_5148 if (__content_140036462745328_5148 is not None) else ''), '_industry_master_graphics_switch;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328_5241 if (__content_140036462745328_5241 is not None) else ''), '_tile_fence_industry, [\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_5316 if (__content_140036462745328_5316 is not None) else ''), ') * !nearby_tile_is_same_industry(-1,  0), ', (__content_140036462745328_5391 if (__content_140036462745328_5391 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_5463 if (__content_140036462745328_5463 is not None) else ''), ') * !nearby_tile_is_same_industry( 0, -1), ', (__content_140036462745328_5538 if (__content_140036462745328_5538 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_5610 if (__content_140036462745328_5610 is not None) else ''), ') * !nearby_tile_is_same_industry( 0,  1), ', (__content_140036462745328_5685 if (__content_140036462745328_5685 is not None) else ''), '),\n                STORE_TEMP(LOAD_TEMP(', (__content_140036462745328_5757 if (__content_140036462745328_5757 is not None) else ''), ') * !nearby_tile_is_same_industry( 1,  0), ', (__content_140036462745328_5832 if (__content_140036462745328_5832 is not None) else ''), '),\n            ]) {\n        ', (__content_140036462745328_5892 if (__content_140036462745328_5892 is not None) else ''), '_tile_fence_station;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140036462745328_5972 if (__content_140036462745328_5972 is not None) else ''), '_tile_fences, [\n                STORE_TEMP(0, ', (__content_140036462745328_6032 if (__content_140036462745328_6032 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6099 if (__content_140036462745328_6099 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6166 if (__content_140036462745328_6166 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6233 if (__content_140036462745328_6233 is not None) else ''), '),\n\n                STORE_TEMP(1, ', (__content_140036462745328_6301 if (__content_140036462745328_6301 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_140036462745328_6366 if (__content_140036462745328_6366 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_140036462745328_6431 if (__content_140036462745328_6431 is not None) else ''), '),\n                STORE_TEMP(1, ', (__content_140036462745328_6496 if (__content_140036462745328_6496 is not None) else ''), '),\n\n                STORE_TEMP(0, ', (__content_140036462745328_6562 if (__content_140036462745328_6562 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6630 if (__content_140036462745328_6630 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6698 if (__content_140036462745328_6698 is not None) else ''), '),\n                STORE_TEMP(0, ', (__content_140036462745328_6766 if (__content_140036462745328_6766 is not None) else ''), '),\n                ]) {\n        ', (__content_140036462745328_6833 if (__content_140036462745328_6833 is not None) else ''), '_tile_fence_industry;\n    }\n    ', ))
            if (__content_140036462745328 is None):
                pass
            else:
                if (__content_140036462745328 is None):
                    __content_140036462745328 = None
                else:
                    __tt = type(__content_140036462745328)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140036462745328 = str(__content_140036462745328)
                    else:
                        if (__tt is bytes):
                            __content_140036462745328 = decode(__content_140036462745328)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140036462745328 = __content_140036462745328.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140036462745328)
                                    __content_140036462745328 = (str(__content_140036462745328) if (__content_140036462745328 is __converted) else __converted)
                                else:
                                    __content_140036462745328 = __content_140036462745328()
            if (__content_140036462745328 is not None):
                __append(__content_140036462745328)
            __append('\n')
            if (__backup_temp_storage_140036454565152 is __marker):
                del econtext['temp_storage']
            else:
                econtext['temp_storage'] = __backup_temp_storage_140036454565152
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }