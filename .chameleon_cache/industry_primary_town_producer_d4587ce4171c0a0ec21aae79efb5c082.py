# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/industry_primary_town_producer.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 940: ('load: layouts.pynml', 23, 30), 940: ('load: layouts.pynml', 23, 30), 1149: ('load: location_check_macros_industry.pynml', 29, 46), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1305: ('load: availability.pynml', 32, 30), 1305: ('load: availability.pynml', 32, 30), 1463: ("produce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}", 38, 0), 1473: ('industry.id', 38, 10), 1756: ('industry.id', 48, 34), 1835: ('industry.id', 49, 6), 1863: ('industry.id', 50, 3), 1922: ('load: properties_industry.pynml', 54, 30), 1922: ('load: properties_industry.pynml', 54, 30), 2106: ('economies', 57, 37), 2157: ("industry.get_property('enabled', economy) == True", 58, 39), 2217: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }', 59, 8), 2232: ('economy.numeric_id', 59, 23), 2291: ('industry.id', 60, 36), 2307: ('industry.numeric_id', 60, 52), 2405: ('industry.id', 62, 47), 2474: ('industry.id', 63, 47), 2554: ('industry.id', 64, 47), 2780: ('industry.get_extra_text_fund(economy)', 67, 47)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166497526056 = 'load: properties_industry.pynml'
_static_140166497529024 = 'load: availability.pynml'
_static_140166498684376 = "location_checks_industry.macros['render_tree']"
_static_140166498386496 = 'load: layouts.pynml'
_static_140166498387336 = 'load: properties_tile.pynml'
_static_140166498389296 = "animation_macros.macros['tile_animation']"
_static_140166498311864 = "location_checks_tile.macros['render_tree']"
_static_140166498309568 = 'load: graphics_switches.pynml'
_static_140166498312088 = 'load: spritelayouts.pynml'
_static_140166498308728 = 'load: spritesets.pynml'

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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')
            __backup_macroname_140166497044104 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e575278> name=None at 7f7b0e5752e8> -> __value
            __value = _static_140166498308728
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497044104 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497044104
            __append('\n\n')
            __backup_macroname_140166497993736 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e575f98> name=None at 7f7b0e575be0> -> __value
            __value = _static_140166498312088
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497993736 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497993736
            __append('\n\n')
            __backup_macroname_140166497803400 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e5755c0> name=None at 7f7b0e575c18> -> __value
            __value = _static_140166498309568
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497803400 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497803400
            __append('\n\n')
            __backup_location_checks_tile_140166499564120 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_140166497896008 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e575eb8> name=None at 7f7b0e575198> -> __value
            __value = _static_140166498311864
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497896008 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497896008
            if (__backup_location_checks_tile_140166499564120 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_140166499564120
            __append('\n\n')
            __backup_animation_macros_140166499561824 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_140166497955080 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588d30> name=None at 7f7b0e588978> -> __value
            __value = _static_140166498389296
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497955080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497955080
            if (__backup_animation_macros_140166499561824 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_140166499561824
            __append('\n\n')
            __backup_macroname_140166498786696 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588588> name=None at 7f7b0e588b70> -> __value
            __value = _static_140166498387336
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498786696 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498786696
            __append('\n\n/* *************************************************\n * Definition of the industry layouts\n * *************************************************/\n\n')
            __backup_macroname_140166498783752 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588240> name=None at 7f7b0e588278> -> __value
            __value = _static_140166498386496
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (23:30)> -> __macro
            __token = 940
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 940
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498783752 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498783752
            __append('\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_location_checks_industry_140166499155024 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (29:46)> -> __value
            __token = 1149
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_140166498784264 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e5d0dd8> name=None at 7f7b0e5d0f98> -> __value
            __value = _static_140166498684376
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (30:30)> -> __macro
            __token = 1223
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1223
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498784264 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498784264
            if (__backup_location_checks_industry_140166499155024 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_140166499155024
            __append('\n\n')
            __backup_macroname_140166498783496 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4b6cc0> name=None at 7f7b0e4b6c88> -> __value
            __value = _static_140166497529024
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1305
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1305
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498783496 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498783496
            __append('\n\n')

            # <Interpolation value=<Substitution "\nproduce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}\n\n\n" (37:4)> braces_required=True translation=False at 7f7b0e4b6588> -> __content_140166518101192
            __token = 1463
            __token = 1473
            __content_140166518101192 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1756
            __content_140166518101192_1754 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_1754 = __quote(__content_140166518101192_1754, '\x00', '&#0;', None, False)
            __token = 1835
            __content_140166518101192_1833 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_1833 = __quote(__content_140166518101192_1833, '\x00', '&#0;', None, False)
            __token = 1863
            __content_140166518101192_1861 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_1861 = __quote(__content_140166518101192_1861, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\nproduce(', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), "_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ", (__content_140166518101192_1754 if (__content_140166518101192_1754 is not None) else ''), '_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ', (__content_140166518101192_1833 if (__content_140166518101192_1833 is not None) else ''), '_production;\n\t', (__content_140166518101192_1861 if (__content_140166518101192_1861 is not None) else ''), '_production;\n}\n\n\n', ))
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
            __backup_macroname_140166498786760 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4b6128> name=None at 7f7b0e4b69e8> -> __value
            __value = _static_140166497526056
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (54:30)> -> __macro
            __token = 1922
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1922
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498786760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498786760
            __append('\n\n')
            __append('\n')
            __backup_economy_140166498095456 = get('economy', __marker)

            # <Value 'economies' (57:37)> -> __iterator
            __token = 2106
            __iterator = getitem('economies')
            (__iterator, ____index_140166497527680, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (58:39)> -> __condition
                __token = 2157
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ' (58:90)> braces_required=True translation=False at 7f7b0e4b6a20> -> __content_140166518101192
                    __token = 2217
                    __token = 2232
                    __content_140166518101192 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
                    __token = 2291
                    __content_140166518101192_2289 = _lookup_attr(getitem('industry'), 'id')
                    __content_140166518101192_2289 = __quote(__content_140166518101192_2289, '\x00', '&#0;', None, False)
                    __token = 2307
                    __content_140166518101192_2305 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_140166518101192_2305 = __quote(__content_140166518101192_2305, '\x00', '&#0;', None, False)
                    __token = 2405
                    __content_140166518101192_2403 = _lookup_attr(getitem('industry'), 'id')
                    __content_140166518101192_2403 = __quote(__content_140166518101192_2403, '\x00', '&#0;', None, False)
                    __token = 2474
                    __content_140166518101192_2472 = _lookup_attr(getitem('industry'), 'id')
                    __content_140166518101192_2472 = __quote(__content_140166518101192_2472, '\x00', '&#0;', None, False)
                    __token = 2554
                    __content_140166518101192_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_140166518101192_2552 = __quote(__content_140166518101192_2552, '\x00', '&#0;', None, False)
                    __token = 2780
                    __content_140166518101192_2778 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_140166518101192_2778 = __quote(__content_140166518101192_2778, '\x00', '&#0;', None, False)
                    __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_140166518101192_2289 if (__content_140166518101192_2289 is not None) else ''), ', ', (__content_140166518101192_2305 if (__content_140166518101192_2305 is not None) else ''), ') {\n                graphics {\n                    produce_256_ticks:       ', (__content_140166518101192_2403 if (__content_140166518101192_2403 is not None) else ''), '_produce;\n                    construction_probability:', (__content_140166518101192_2472 if (__content_140166518101192_2472 is not None) else ''), '_check_availability;\n                    location_check:          ', (__content_140166518101192_2552 if (__content_140166518101192_2552 is not None) else ''), '_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ', (__content_140166518101192_2778 if (__content_140166518101192_2778 is not None) else ''), ';\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ', ))
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
                __append('\n')
                ____index_140166497527680 -= 1
                if (____index_140166497527680 > 0):
                    __append('')
            if (__backup_economy_140166498095456 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140166498095456
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }