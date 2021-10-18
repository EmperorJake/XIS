# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/industry_primary.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1197: ('load: availability.pynml', 32, 30), 1197: ('load: availability.pynml', 32, 30), 1273: ('load: location_check_macros_industry.pynml', 34, 46), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1613: ('economies', 40, 37), 1664: ("industry.get_property('enabled', economy) == True", 41, 39), 1724: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1739: ('economy.numeric_id', 42, 23), 1798: ('industry.id', 43, 36), 1814: ('industry.numeric_id', 43, 52), 1913: ('industry.id', 45, 48), 2079: ('industry.id', 47, 48), 2149: ('industry.id', 48, 48), 2229: ('industry.id', 49, 48), 2389: ('industry.id', 51, 48), 2466: ('industry.get_extra_text_fund(economy)', 52, 48), 2554: ('industry.id', 53, 48), 2627: ('industry.id', 54, 48)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139738425570544 = 'load: properties_industry.pynml'
_static_139738425572992 = "location_checks_industry.macros['render_tree']"
_static_139738427612608 = 'load: availability.pynml'
_static_139738426105920 = 'load: check_primary_supplies_delivered.pynml'
_static_139738426106112 = 'load: produce_primary.pynml'
_static_139738426108320 = 'load: extra_text_primary.pynml'
_static_139738447011744 = 'load: layouts.pynml'
_static_139738447009824 = 'load: properties_tile.pynml'
_static_139738425701856 = "animation_macros.macros['tile_animation']"
_static_139738425703248 = "location_checks_tile.macros['render_tree']"
_static_139738425703008 = 'load: graphics_switches.pynml'
_static_139738425702432 = 'load: spritelayouts.pynml'
_static_139738425702576 = 'load: spritesets.pynml'
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

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425702096
            __attrs_139738425702096 = _static_139738431409216
            __backup_macroname_139738425170560 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176339b8b0> name=None at 7f176339b3a0> -> __value
            __value = _static_139738425702576
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425170560 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425170560
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425702384
            __attrs_139738425702384 = _static_139738431409216
            __backup_macroname_139738425167936 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176339b820> name=None at 7f176339b580> -> __value
            __value = _static_139738425702432
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425167936 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425167936
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425702816
            __attrs_139738425702816 = _static_139738431409216
            __backup_macroname_139738425169408 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176339ba60> name=None at 7f176339b460> -> __value
            __value = _static_139738425703008
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425169408 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425169408
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425704352
            __attrs_139738425704352 = _static_139738431409216
            __backup_location_checks_tile_139738426282960 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139738431829632 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176339bb50> name=None at 7f176339bc40> -> __value
            __value = _static_139738425703248
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738431829632 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738431829632
            if (__backup_location_checks_tile_139738426282960 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139738426282960
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738447008720
            __attrs_139738447008720 = _static_139738431409216
            __backup_animation_macros_139738426285024 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139738428652864 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176339b5e0> name=None at 7f176339baf0> -> __value
            __value = _static_139738425701856
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428652864 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428652864
            if (__backup_animation_macros_139738426285024 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139738426285024
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738447009392
            __attrs_139738447009392 = _static_139738431409216
            __backup_macroname_139738426815680 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17647ed820> name=None at 7f17647ed280> -> __value
            __value = _static_139738447009824
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426815680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426815680
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738447010160
            __attrs_139738447010160 = _static_139738431409216
            __backup_macroname_139738425190784 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17647edfa0> name=None at 7f17647ed8b0> -> __value
            __value = _static_139738447011744
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425190784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425190784
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426108704
            __attrs_139738426108704 = _static_139738431409216
            __backup_macroname_139738434365888 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17633fe9a0> name=None at 7f17633fef10> -> __value
            __value = _static_139738426108320
            econtext['macroname'] = __value

            # <Value 'load: extra_text_primary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' extra_text_primary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738434365888 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738434365888
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426109424
            __attrs_139738426109424 = _static_139738431409216
            __backup_macroname_139738427052800 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17633fe100> name=None at 7f17633fe910> -> __value
            __value = _static_139738426106112
            econtext['macroname'] = __value

            # <Value 'load: produce_primary.pynml' (28:30)> -> __macro
            __token = 1054
            __macro = ' produce_primary.pynml'
            __macro = __loader(__macro)
            __token = 1054
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738427052800 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738427052800
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427610544
            __attrs_139738427610544 = _static_139738431409216
            __backup_macroname_139738431585216 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17633fe040> name=None at 7f176356d820> -> __value
            __value = _static_139738426105920
            econtext['macroname'] = __value

            # <Value 'load: check_primary_supplies_delivered.pynml' (30:30)> -> __macro
            __token = 1117
            __macro = ' check_primary_supplies_delivered.pynml'
            __macro = __loader(__macro)
            __token = 1117
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738431585216 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738431585216
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427612944
            __attrs_139738427612944 = _static_139738431409216
            __backup_macroname_139738425875328 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176356ddc0> name=None at 7f176356deb0> -> __value
            __value = _static_139738427612608
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1197
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425875328 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425875328
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425572464
            __attrs_139738425572464 = _static_139738431409216
            __backup_location_checks_industry_139738426109616 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1273
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139738425875776 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176337be80> name=None at 7f176337b100> -> __value
            __value = _static_139738425572992
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1347
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425875776 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425875776
            if (__backup_location_checks_industry_139738426109616 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139738426109616
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425572800
            __attrs_139738425572800 = _static_139738431409216
            __backup_macroname_139738425875712 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f176337b4f0> name=None at 7f176337b040> -> __value
            __value = _static_139738425570544
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1429
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1429
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738425875712 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738425875712
            __append('\n\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425571936
            __attrs_139738425571936 = _static_139738431409216
            __backup_economy_139738426107072 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1613
            __iterator = getitem('economies')
            (__iterator, ____index_139738425571648, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425570880
                __attrs_139738425570880 = _static_139738431409216

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1664
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176337b7f0> -> __content_139738435934384
                    __token = 1724
                    __token = 1739
                    __content_139738435934384 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                    __token = 1798
                    __content_139738435934384_1796 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_1796 = __quote(__content_139738435934384_1796, '\x00', '&#0;', None, None)
                    __token = 1814
                    __content_139738435934384_1812 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139738435934384_1812 = __quote(__content_139738435934384_1812, '\x00', '&#0;', None, None)
                    __token = 1913
                    __content_139738435934384_1911 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_1911 = __quote(__content_139738435934384_1911, '\x00', '&#0;', None, None)
                    __token = 2079
                    __content_139738435934384_2077 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2077 = __quote(__content_139738435934384_2077, '\x00', '&#0;', None, None)
                    __token = 2149
                    __content_139738435934384_2147 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2147 = __quote(__content_139738435934384_2147, '\x00', '&#0;', None, None)
                    __token = 2229
                    __content_139738435934384_2227 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2227 = __quote(__content_139738435934384_2227, '\x00', '&#0;', None, None)
                    __token = 2389
                    __content_139738435934384_2387 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2387 = __quote(__content_139738435934384_2387, '\x00', '&#0;', None, None)
                    __token = 2466
                    __content_139738435934384_2464 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139738435934384_2464 = __quote(__content_139738435934384_2464, '\x00', '&#0;', None, None)
                    __token = 2554
                    __content_139738435934384_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2552 = __quote(__content_139738435934384_2552, '\x00', '&#0;', None, None)
                    __token = 2627
                    __content_139738435934384_2625 = _lookup_attr(getitem('industry'), 'id')
                    __content_139738435934384_2625 = __quote(__content_139738435934384_2625, '\x00', '&#0;', None, None)
                    __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139738435934384_1796 if (__content_139738435934384_1796 is not None) else ''), ', ', (__content_139738435934384_1812 if (__content_139738435934384_1812 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_139738435934384_1911 if (__content_139738435934384_1911 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ', (__content_139738435934384_2077 if (__content_139738435934384_2077 is not None) else ''), '_produce;\n                    produce_256_ticks:        ', (__content_139738435934384_2147 if (__content_139738435934384_2147 is not None) else ''), '_produce_256_ticks;\n                    monthly_prod_change:      ', (__content_139738435934384_2227 if (__content_139738435934384_2227 is not None) else ''), '_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ', (__content_139738435934384_2387 if (__content_139738435934384_2387 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_139738435934384_2464 if (__content_139738435934384_2464 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_139738435934384_2552 if (__content_139738435934384_2552 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_139738435934384_2625 if (__content_139738435934384_2625 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                ____index_139738425571648 -= 1
                if (____index_139738425571648 > 0):
                    __append('')
            if (__backup_economy_139738426107072 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139738426107072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }