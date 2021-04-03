# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/location_check_macros_tile.pynml'
__tokens = {389: ('industry.tiles', 9, 43), 448: ('tile.location_checks.get_render_tree(tile.id, industry.id)', 10, 42), 531: ('location_checks', 10, 125), 604: ('location_check.macro', 11, 55), 604: ('location_check.macro', 11, 55), 1009: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_water_class(0,0)) {\n        WATER_CLASS_SEA: ${location_check.switch_result};\n        WATER_CLASS_NONE: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 22, 4), 1044: ('location_check.switch_entry_point', 22, 39), 1139: ('location_check.switch_result', 23, 27), 1198: ('location_check.switch_result', 24, 28), 1631: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, UCMP(nearby_tile_height(0, 0) - ${location_check.minh}, ${location_check.maxh} - ${location_check.minh})) {\n        0..1: ${location_check.switch_result};\n        ${location_check.outrange};\n    }', 33, 4), 1666: ('location_check.switch_entry_point', 33, 39), 1736: ('location_check.minh', 33, 109), 1760: ('location_check.maxh', 33, 133), 1785: ('location_check.minh', 33, 158), 1826: ('location_check.switch_result', 34, 16), 1867: ('location_check.outrange', 35, 10), 2083: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_is_water(0, 0)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 42, 4), 2118: ('location_check.switch_entry_point', 42, 39), 2241: ('location_check.switch_result', 44, 10), 2485: ('switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) & bitmask(IS_STEEP_SLOPE)) {\n        0: ${location_check.switch_result};\n        return string(STR_ERR_LOCATION_NOT_ON_STEEP_SLOPE);\n    }', 51, 4), 2521: ('location_check.switch_entry_point', 51, 40), 2622: ('location_check.switch_result', 52, 13), 2909: ('switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 60, 4), 2945: ('location_check.switch_entry_point', 60, 40), 3034: ('location_check.switch_result', 61, 13), 3327: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 69, 4), 3362: ('location_check.switch_entry_point', 69, 39), 3495: ('location_check.switch_result', 71, 10), 3720: ('switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                                                      (\n                                                      nearby_tile_class(0, -1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(0, 1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(-1, 0) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(1, 0) == TILE_CLASS_ROAD ? 1 : 0\n                                                      ))))) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 79, 4), 3756: ('location_check.switch_entry_point', 79, 40), 4342: ('location_check.switch_result', 86, 13), 4620: ('switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_class(${location_check.x}, ${location_check.y})) {', 94, 4), 4656: ('location_check.switch_entry_point', 94, 40), 4712: ('location_check.x', 94, 96), 4733: ('location_check.y', 94, 117), 4951: ('TILE_CLASS_HOUSE: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }', 96, 8), 5012: ('location_check.switch_result', 97, 10), 5403: ('switch (FEAT_INDUSTRYTILES, PARENT, ${location_check.switch_entry_point}, (\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_FUND) ||\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }', 108, 4), 5441: ('location_check.switch_entry_point', 108, 42), 5730: ('location_check.switch_result', 114, 10), 6148: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n        (nearby_tile_class( 1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0,  1) == TILE_CLASS_INDUSTRY)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 125, 4), 6183: ('location_check.switch_entry_point', 125, 39), 6765: ('location_check.switch_result', 135, 10), 7028: ('switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                (nearby_tile_terrain_type( 1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  1) == TILETYPE_DESERT)\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 142, 4), 7063: ('location_check.switch_entry_point', 142, 39), 7826: ('location_check.switch_result', 154, 10), 8422: ('switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                (\n                nearby_tile_height(-relative_x, -relative_y)\n                + (nearby_tile_slope(-relative_x, -relative_y)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(-relative_x, -relative_y) == bitmask(IS_STEEP_SLOPE) ? 2 : 1\n                )) == (nearby_tile_height(0, 0)\n                + (nearby_tile_slope(0, 0)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(0, 0) == bitmask(IS_STEEP_SLOPE) ? 2 : 1))\n                ) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 168, 4), 8458: ('location_check.switch_entry_point', 168, 40), 9004: ('location_check.switch_result', 179, 13)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166499479680 = 'location_check.macro'

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render_render_tree(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')
            __backup_tile_140166499564512 = get('tile', __marker)

            # <Value 'industry.tiles' (9:43)> -> __iterator
            __token = 389
            __iterator = _lookup_attr(getitem('industry'), 'tiles')
            (__iterator, ____index_140166499483208, ) = getitem('repeat')('tile', __iterator)
            econtext['tile'] = None
            for __item in __iterator:
                econtext['tile'] = __item
                __append('\n        ')
                __backup_location_checks_140166499421768 = get('location_checks', __marker)

                # <Value 'tile.location_checks.get_render_tree(tile.id, industry.id)' (10:42)> -> __value
                __token = 448
                __value = _lookup_attr(_lookup_attr(getitem('tile'), 'location_checks'), 'get_render_tree')(_lookup_attr(getitem('tile'), 'id'), _lookup_attr(getitem('industry'), 'id'))
                econtext['location_checks'] = __value
                __backup_location_check_140166499565520 = get('location_check', __marker)

                # <Value 'location_checks' (10:125)> -> __iterator
                __token = 531
                __iterator = getitem('location_checks')
                (__iterator, ____index_140166499481976, ) = getitem('repeat')('location_check', __iterator)
                econtext['location_check'] = None
                for __item in __iterator:
                    econtext['location_check'] = __item
                    __append('\n            ')
                    __backup_macroname_140166498206600 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f7b0e693080> name=None at 7f7b0e693ac8> -> __value
                    __value = _static_140166499479680
                    econtext['macroname'] = __value

                    # <Value 'location_check.macro' (11:55)> -> __macro
                    __token = 604
                    __macro = _lookup_attr(getitem('location_check'), 'macro')
                    __token = 604
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140166498206600 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140166498206600
                    __append('\n        ')
                    ____index_140166499481976 -= 1
                    if (____index_140166499481976 > 0):
                        __append('')
                if (__backup_location_check_140166499565520 is __marker):
                    del econtext['location_check']
                else:
                    econtext['location_check'] = __backup_location_check_140166499565520
                if (__backup_location_checks_140166499421768 is __marker):
                    del econtext['location_checks']
                else:
                    econtext['location_checks'] = __backup_location_checks_140166499421768
                __append('\n    ')
                ____index_140166499483208 -= 1
                if (____index_140166499483208 > 0):
                    __append('')
            if (__backup_tile_140166499564512 is __marker):
                del econtext['tile']
            else:
                econtext['tile'] = __backup_tile_140166499564512
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_sea_tile(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_water_class(0,0)) {\n        WATER_CLASS_SEA: ${location_check.switch_result};\n        WATER_CLASS_NONE: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n' (21:105)> braces_required=True translation=False at 7f7b0e6931d0> -> __content_140166518101192
            __token = 1009
            __token = 1044
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1139
            __content_140166518101192_1137 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_1137 = __quote(__content_140166518101192_1137, '\x00', '&#0;', None, False)
            __token = 1198
            __content_140166518101192_1196 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_1196 = __quote(__content_140166518101192_1196, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_water_class(0,0)) {\n        WATER_CLASS_SEA: ', (__content_140166518101192_1137 if (__content_140166518101192_1137 is not None) else ''), ';\n        WATER_CLASS_NONE: ', (__content_140166518101192_1196 if (__content_140166518101192_1196 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_height_range(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, UCMP(nearby_tile_height(0, 0) - ${location_check.minh}, ${location_check.maxh} - ${location_check.minh})) {\n        0..1: ${location_check.switch_result};\n        ${location_check.outrange};\n    }\n' (32:114)> braces_required=True translation=False at 7f7b0e693400> -> __content_140166518101192
            __token = 1631
            __token = 1666
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1736
            __content_140166518101192_1734 = _lookup_attr(getitem('location_check'), 'minh')
            __content_140166518101192_1734 = __quote(__content_140166518101192_1734, '\x00', '&#0;', None, False)
            __token = 1760
            __content_140166518101192_1758 = _lookup_attr(getitem('location_check'), 'maxh')
            __content_140166518101192_1758 = __quote(__content_140166518101192_1758, '\x00', '&#0;', None, False)
            __token = 1785
            __content_140166518101192_1783 = _lookup_attr(getitem('location_check'), 'minh')
            __content_140166518101192_1783 = __quote(__content_140166518101192_1783, '\x00', '&#0;', None, False)
            __token = 1826
            __content_140166518101192_1824 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_1824 = __quote(__content_140166518101192_1824, '\x00', '&#0;', None, False)
            __token = 1867
            __content_140166518101192_1865 = _lookup_attr(getitem('location_check'), 'outrange')
            __content_140166518101192_1865 = __quote(__content_140166518101192_1865, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', UCMP(nearby_tile_height(0, 0) - ', (__content_140166518101192_1734 if (__content_140166518101192_1734 is not None) else ''), ', ', (__content_140166518101192_1758 if (__content_140166518101192_1758 is not None) else ''), ' - ', (__content_140166518101192_1783 if (__content_140166518101192_1783 is not None) else ''), ')) {\n        0..1: ', (__content_140166518101192_1824 if (__content_140166518101192_1824 is not None) else ''), ';\n        ', (__content_140166518101192_1865 if (__content_140166518101192_1865 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_disallow_coast_or_water(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_is_water(0, 0)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n' (41:70)> braces_required=True translation=False at 7f7b0e6936a0> -> __content_140166518101192
            __token = 2083
            __token = 2118
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 2241
            __content_140166518101192_2239 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_2239 = __quote(__content_140166518101192_2239, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_is_water(0, 0)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_2239 if (__content_140166518101192_2239 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_disallow_steep_slopes(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) & bitmask(IS_STEEP_SLOPE)) {\n        0: ${location_check.switch_result};\n        return string(STR_ERR_LOCATION_NOT_ON_STEEP_SLOPE);\n    }\n' (50:94)> braces_required=True translation=False at 7f7b0e693518> -> __content_140166518101192
            __token = 2485
            __token = 2521
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 2622
            __content_140166518101192_2620 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_2620 = __quote(__content_140166518101192_2620, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_slope(0,0) & bitmask(IS_STEEP_SLOPE)) {\n        0: ', (__content_140166518101192_2620 if (__content_140166518101192_2620 is not None) else ''), ';\n        return string(STR_ERR_LOCATION_NOT_ON_STEEP_SLOPE);\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_disallow_slopes(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n' (59:91)> braces_required=True translation=False at 7f7b0e693e80> -> __content_140166518101192
            __token = 2909
            __token = 2945
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 3034
            __content_140166518101192_3032 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_3032 = __quote(__content_140166518101192_3032, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: ', (__content_140166518101192_3032 if (__content_140166518101192_3032 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_slope(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n\n' (68:123)> braces_required=True translation=False at 7f7b0e6933c8> -> __content_140166518101192
            __token = 3327
            __token = 3362
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 3495
            __content_140166518101192_3493 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_3493 = __quote(__content_140166518101192_3493, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_slope(0,0) == SLOPE_FLAT) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_3493 if (__content_140166518101192_3493 is not None) else ''), ';\n    }\n\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_road_adjacent(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                                                      (\n                                                      nearby_tile_class(0, -1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(0, 1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(-1, 0) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(1, 0) == TILE_CLASS_ROAD ? 1 : 0\n                                                      ))))) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n' (78:84)> braces_required=True translation=False at 7f7b0ff6f320> -> __content_140166518101192
            __token = 3720
            __token = 3756
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 4342
            __content_140166518101192_4340 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_4340 = __quote(__content_140166518101192_4340, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n                                                      (\n                                                      nearby_tile_class(0, -1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(0, 1) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(-1, 0) == TILE_CLASS_ROAD ? 1 :\n                                                      (nearby_tile_class(1, 0) == TILE_CLASS_ROAD ? 1 : 0\n                                                      ))))) {\n        1: ', (__content_140166518101192_4340 if (__content_140166518101192_4340 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_houses_nearby(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point}, nearby_tile_class(${location_check.x}, ${location_check.y})) {\n        ' (93:86)> braces_required=True translation=False at 7f7b0ff6f7b8> -> __content_140166518101192
            __token = 4620
            __token = 4656
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 4712
            __content_140166518101192_4710 = _lookup_attr(getitem('location_check'), 'x')
            __content_140166518101192_4710 = __quote(__content_140166518101192_4710, '\x00', '&#0;', None, False)
            __token = 4733
            __content_140166518101192_4731 = _lookup_attr(getitem('location_check'), 'y')
            __content_140166518101192_4731 = __quote(__content_140166518101192_4731, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', nearby_tile_class(', (__content_140166518101192_4710 if (__content_140166518101192_4710 is not None) else ''), ', ', (__content_140166518101192_4731 if (__content_140166518101192_4731 is not None) else ''), ')) {\n        ', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)

            # <Interpolation value=<Substitution '\n        TILE_CLASS_HOUSE: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }\n' (95:187)> braces_required=True translation=False at 7f7b0ff6f208> -> __content_140166518101192
            __token = 4951
            __token = 5012
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s' % ('\n        TILE_CLASS_HOUSE: return CB_RESULT_LOCATION_ALLOW;\n        ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_allow_player(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, PARENT, ${location_check.switch_entry_point}, (\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_FUND) ||\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }\n' (107:7)> braces_required=True translation=False at 7f7b0e643f28> -> __content_140166518101192
            __token = 5403
            __token = 5441
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 5730
            __content_140166518101192_5728 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_5728 = __quote(__content_140166518101192_5728, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, PARENT, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', (\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_FUND) ||\n                (((extra_callback_info2 & 0xFF00) >> 8) == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ', (__content_140166518101192_5728 if (__content_140166518101192_5728 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_disallow_industry_adjacent(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n        (nearby_tile_class( 1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0,  1) == TILE_CLASS_INDUSTRY)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n' (124:7)> braces_required=True translation=False at 7f7b0e643a20> -> __content_140166518101192
            __token = 6148
            __token = 6183
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 6765
            __content_140166518101192_6763 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_6763 = __quote(__content_140166518101192_6763, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n        (nearby_tile_class( 1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1, -1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  0) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class(-1,  1) == TILE_CLASS_INDUSTRY) |\n        (nearby_tile_class( 0,  1) == TILE_CLASS_INDUSTRY)) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_6763 if (__content_140166518101192_6763 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_disallow_desert(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                (nearby_tile_terrain_type( 1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  1) == TILETYPE_DESERT)\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n' (141:122)> braces_required=True translation=False at 7f7b0e643c50> -> __content_140166518101192
            __token = 7028
            __token = 7063
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 7826
            __content_140166518101192_7824 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_7824 = __quote(__content_140166518101192_7824, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n                (nearby_tile_terrain_type( 1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 1,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type( 0,  1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1, -1) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  0) == TILETYPE_DESERT) &&\n                (nearby_tile_terrain_type(-1,  1) == TILETYPE_DESERT)\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_7824 if (__content_140166518101192_7824 is not None) else ''), ';\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_require_effectively_flat(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRYTILES, SELF, ${location_check.switch_entry_point},\n                (\n                nearby_tile_height(-relative_x, -relative_y)\n                + (nearby_tile_slope(-relative_x, -relative_y)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(-relative_x, -relative_y) == bitmask(IS_STEEP_SLOPE) ? 2 : 1\n                )) == (nearby_tile_height(0, 0)\n                + (nearby_tile_slope(0, 0)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(0, 0) == bitmask(IS_STEEP_SLOPE) ? 2 : 1))\n                ) {\n        1: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n' (167:7)> braces_required=True translation=False at 7f7b0e65efd0> -> __content_140166518101192
            __token = 8422
            __token = 8458
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 9004
            __content_140166518101192_9002 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_9002 = __quote(__content_140166518101192_9002, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n                (\n                nearby_tile_height(-relative_x, -relative_y)\n                + (nearby_tile_slope(-relative_x, -relative_y)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(-relative_x, -relative_y) == bitmask(IS_STEEP_SLOPE) ? 2 : 1\n                )) == (nearby_tile_height(0, 0)\n                + (nearby_tile_slope(0, 0)\n                == SLOPE_FLAT ? 0 :\n                nearby_tile_slope(0, 0) == bitmask(IS_STEEP_SLOPE) ? 2 : 1))\n                ) {\n        1: ', (__content_140166518101192_9002 if (__content_140166518101192_9002 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n', ))
            if (__content_140166518101192 is None):
                pass
            else:
                if (__content_140166518101192 is False):
                    __content_140166518101192 = None
                else:
                    __tt = type(__content_140166518101192)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140166518101192 = str(__content_140166518101192)
                    else:
                        if (__tt is bytes):
                            __content_140166518101192 = decode(__content_140166518101192)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140166518101192 = __content_140166518101192.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140166518101192)
                                    __content_140166518101192 = (str(__content_140166518101192) if (__content_140166518101192 is __converted) else __converted)
                                else:
                                    __content_140166518101192 = __content_140166518101192()
            if (__content_140166518101192 is not None):
                __append(__content_140166518101192)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __append('\n\n')
            __token = None
            render_render_tree(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __append('\n\n')
            __token = None
            render_require_sea_tile(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_require_height_range(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_disallow_coast_or_water(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_disallow_steep_slopes(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_disallow_slopes(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_require_slope(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_require_road_adjacent(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_require_houses_nearby(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_allow_player(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_disallow_industry_adjacent(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_disallow_desert(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_require_effectively_flat(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_render_tree': render_render_tree, 'render_require_sea_tile': render_require_sea_tile, 'render_require_height_range': render_require_height_range, 'render_disallow_coast_or_water': render_disallow_coast_or_water, 'render_disallow_steep_slopes': render_disallow_steep_slopes, 'render_disallow_slopes': render_disallow_slopes, 'render_require_slope': render_require_slope, 'render_require_road_adjacent': render_require_road_adjacent, 'render_require_houses_nearby': render_require_houses_nearby, 'render_allow_player': render_allow_player, 'render_disallow_industry_adjacent': render_disallow_industry_adjacent, 'render_disallow_desert': render_disallow_desert, 'render_require_effectively_flat': render_require_effectively_flat, 'render': render, }