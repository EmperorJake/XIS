# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/industry_primary_town_producer.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 940: ('load: layouts.pynml', 23, 30), 940: ('load: layouts.pynml', 23, 30), 1149: ('load: location_check_macros_industry.pynml', 29, 46), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1223: ("location_checks_industry.macros['render_tree']", 30, 30), 1305: ('load: availability.pynml', 32, 30), 1305: ('load: availability.pynml', 32, 30), 1463: ("produce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}", 38, 0), 1473: ('industry.id', 38, 10), 1756: ('industry.id', 48, 34), 1835: ('industry.id', 49, 6), 1863: ('industry.id', 50, 3), 1922: ('load: properties_industry.pynml', 54, 30), 1922: ('load: properties_industry.pynml', 54, 30), 2106: ('economies', 57, 37), 2157: ("industry.get_property('enabled', economy) == True", 58, 39), 2217: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }', 59, 8), 2232: ('economy.numeric_id', 59, 23), 2291: ('industry.id', 60, 36), 2307: ('industry.numeric_id', 60, 52), 2405: ('industry.id', 62, 47), 2474: ('industry.id', 63, 47), 2554: ('industry.id', 64, 47), 2780: ('industry.get_extra_text_fund(economy)', 67, 47)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139738426400928 = 'load: properties_industry.pynml'
_static_139738427315920 = 'load: availability.pynml'
_static_139738427315536 = "location_checks_industry.macros['render_tree']"
_static_139738427316112 = 'load: layouts.pynml'
_static_139738427316256 = 'load: properties_tile.pynml'
_static_139738426801408 = "animation_macros.macros['tile_animation']"
_static_139738426801552 = "location_checks_tile.macros['render_tree']"
_static_139738426786912 = 'load: graphics_switches.pynml'
_static_139738426789456 = 'load: spritelayouts.pynml'
_static_139738428814192 = 'load: spritesets.pynml'
_static_139738431409216 = {}

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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425704016
            __attrs_139738425704016 = _static_139738431409216
            __backup_macroname_139738427038208 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763693370> name=None at 7f1763693280> -> __value
            __value = _static_139738428814192
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738427038208 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738427038208
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426788112
            __attrs_139738426788112 = _static_139738431409216
            __backup_macroname_139738427036928 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a4e50> name=None at 7f17634a4d90> -> __value
            __value = _static_139738426789456
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738427036928 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738427036928
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426787680
            __attrs_139738426787680 = _static_139738431409216
            __backup_macroname_139738425742464 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a4460> name=None at 7f17634a4370> -> __value
            __value = _static_139738426786912
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425742464 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425742464
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426799056
            __attrs_139738426799056 = _static_139738431409216
            __backup_location_checks_tile_139738428253664 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139738426817920 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a7d90> name=None at 7f17634a79d0> -> __value
            __value = _static_139738426801552
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426817920 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426817920
            if (__backup_location_checks_tile_139738428253664 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139738428253664
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426801360
            __attrs_139738426801360 = _static_139738431409216
            __backup_animation_macros_139738428254192 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139738427421248 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a7d00> name=None at 7f17634a7130> -> __value
            __value = _static_139738426801408
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738427421248 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738427421248
            if (__backup_animation_macros_139738428254192 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139738428254192
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427316304
            __attrs_139738427316304 = _static_139738431409216
            __backup_macroname_139738425817472 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525820> name=None at 7f1763525f10> -> __value
            __value = _static_139738427316256
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425817472 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425817472
            __append('\n\n/* *************************************************\n * Definition of the industry layouts\n * *************************************************/\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427316160
            __attrs_139738427316160 = _static_139738431409216
            __backup_macroname_139738428404288 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525790> name=None at 7f1763525e50> -> __value
            __value = _static_139738427316112
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (23:30)> -> __macro
            __token = 940
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 940
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428404288 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428404288
            __append('\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427316640
            __attrs_139738427316640 = _static_139738431409216
            __backup_location_checks_industry_139738428253856 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (29:46)> -> __value
            __token = 1149
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139738431841792 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525550> name=None at 7f1763525940> -> __value
            __value = _static_139738427315536
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (30:30)> -> __macro
            __token = 1223
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1223
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738431841792 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738431841792
            if (__backup_location_checks_industry_139738428253856 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139738428253856
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426404240
            __attrs_139738426404240 = _static_139738431409216
            __backup_macroname_139738431843392 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17635256d0> name=None at 7f1763525460> -> __value
            __value = _static_139738427315920
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1305
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1305
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738431843392 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738431843392
            __append('\n\n')

            # <Interpolation value=<Substitution "\nproduce(${industry.id}_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ${industry.id}_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ${industry.id}_production;\n\t${industry.id}_production;\n}\n\n\n" (37:4)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763446c70> -> __content_139738435934384
            __token = 1463
            __token = 1473
            __content_139738435934384 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __token = 1756
            __content_139738435934384_1754 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384_1754 = __quote(__content_139738435934384_1754, '\x00', '&#0;', None, None)
            __token = 1835
            __content_139738435934384_1833 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384_1833 = __quote(__content_139738435934384_1833, '\x00', '&#0;', None, None)
            __token = 1863
            __content_139738435934384_1861 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384_1861 = __quote(__content_139738435934384_1861, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s' % ('\nproduce(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), "_production,\n\t\twaiting_cargo_1, // should be 0\n\t\twaiting_cargo_2, // should be 0\n\t\twaiting_cargo_3, // should be 0\n\t\tLOAD_TEMP(1),    // we stored output here\n\t\t0,               // no 2nd output\n\t\t0                // don't repeat\n\t\t);\n\n\nswitch(FEAT_INDUSTRIES, PARENT, ", (__content_139738435934384_1754 if (__content_139738435934384_1754 is not None) else ''), '_produce, [STORE_TEMP(((population + 11) / (12 * 7)), 1)]) {\n\t0: ', (__content_139738435934384_1833 if (__content_139738435934384_1833 is not None) else ''), '_production;\n\t', (__content_139738435934384_1861 if (__content_139738435934384_1861 is not None) else ''), '_production;\n}\n\n\n', ))
            if (__content_139738435934384 is None):
                pass
            else:
                if (__content_139738435934384 is None):
                    __content_139738435934384 = None
                else:
                    __tt = type(__content_139738435934384)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139738435934384 = str(__content_139738435934384)
                    else:
                        if (__tt is bytes):
                            __content_139738435934384 = decode(__content_139738435934384)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139738435934384 = __content_139738435934384.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139738435934384)
                                    __content_139738435934384 = (str(__content_139738435934384) if (__content_139738435934384 is __converted) else __converted)
                                else:
                                    __content_139738435934384 = __content_139738435934384()
            if (__content_139738435934384 is not None):
                __append(__content_139738435934384)

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426404432
            __attrs_139738426404432 = _static_139738431409216
            __backup_macroname_139738428898624 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634460a0> name=None at 7f1763446d00> -> __value
            __value = _static_139738426400928
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (54:30)> -> __macro
            __token = 1922
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1922
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428898624 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428898624
            __append('\n\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428813472
            __attrs_139738428813472 = _static_139738431409216
            __backup_economy_139738428252704 = get('economy', __marker)

            # <Value 'economies' (57:37)> -> __iterator
            __token = 2106
            __iterator = getitem('economies')
            (__iterator, ____index_139738428814048, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428816448
                __attrs_139738428816448 = _static_139738431409216

                # <Value "industry.get_property('enabled', economy) == True" (58:39)> -> __condition
                __token = 2157
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    produce_256_ticks:       ${industry.id}_produce;\n                    construction_probability:${industry.id}_check_availability;\n                    location_check:          ${industry.id}_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ' (58:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763693b80> -> __content_139738435934384
                    __token = 2217
                    __token = 2232
                    __content_139738435934384 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                    __token = 2291
                    __content_139738435934384_2289 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2289 = __quote(__content_139738435934384_2289, '\x00', '&#0;', None, None)
                    __token = 2307
                    __content_139738435934384_2305 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139738435934384_2305 = __quote(__content_139738435934384_2305, '\x00', '&#0;', None, None)
                    __token = 2405
                    __content_139738435934384_2403 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2403 = __quote(__content_139738435934384_2403, '\x00', '&#0;', None, None)
                    __token = 2474
                    __content_139738435934384_2472 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2472 = __quote(__content_139738435934384_2472, '\x00', '&#0;', None, None)
                    __token = 2554
                    __content_139738435934384_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2552 = __quote(__content_139738435934384_2552, '\x00', '&#0;', None, None)
                    __token = 2780
                    __content_139738435934384_2778 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139738435934384_2778 = __quote(__content_139738435934384_2778, '\x00', '&#0;', None, None)
                    __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139738435934384_2289 if (__content_139738435934384_2289 is not None) else ''), ', ', (__content_139738435934384_2305 if (__content_139738435934384_2305 is not None) else ''), ') {\n                graphics {\n                    produce_256_ticks:       ', (__content_139738435934384_2403 if (__content_139738435934384_2403 is not None) else ''), '_produce;\n                    construction_probability:', (__content_139738435934384_2472 if (__content_139738435934384_2472 is not None) else ''), '_check_availability;\n                    location_check:          ', (__content_139738435934384_2552 if (__content_139738435934384_2552 is not None) else ''), '_check_location;\n                    monthly_prod_change:     CB_RESULT_IND_PROD_NO_CHANGE;\n                    random_prod_change:      CB_RESULT_IND_PROD_NO_CHANGE;\n                    extra_text_fund:         ', (__content_139738435934384_2778 if (__content_139738435934384_2778 is not None) else ''), ';\n                    extra_text_industry:     return string(STR_EXTRA_RECYCLING_DEPOT);\n                    colour:                  switch_colour;\n                }\n            }\n        }\n    ', ))
                    if (__content_139738435934384 is None):
                        pass
                    else:
                        if (__content_139738435934384 is None):
                            __content_139738435934384 = None
                        else:
                            __tt = type(__content_139738435934384)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139738435934384 = str(__content_139738435934384)
                            else:
                                if (__tt is bytes):
                                    __content_139738435934384 = decode(__content_139738435934384)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139738435934384 = __content_139738435934384.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139738435934384)
                                            __content_139738435934384 = (str(__content_139738435934384) if (__content_139738435934384 is __converted) else __converted)
                                        else:
                                            __content_139738435934384 = __content_139738435934384()
                    if (__content_139738435934384 is not None):
                        __append(__content_139738435934384)
                __append('\n')
                ____index_139738428814048 -= 1
                if (____index_139738428814048 > 0):
                    __append('')
            if (__backup_economy_139738428252704 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139738428252704
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }