# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/XIS/src/templates/industry_primary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1197: ('load: availability.pynml', 32, 30), 1197: ('load: availability.pynml', 32, 30), 1273: ('load: location_check_macros_industry.pynml', 34, 46), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1613: ('economies', 40, 37), 1664: ("industry.get_property('enabled', economy) == True", 41, 39), 1724: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1739: ('economy.numeric_id', 42, 23), 1798: ('industry.id', 43, 36), 1814: ('industry.numeric_id', 43, 52), 1913: ('industry.id', 45, 48), 2079: ('industry.id', 47, 48), 2149: ('industry.id', 48, 48), 2229: ('industry.id', 49, 48), 2389: ('industry.id', 51, 48), 2466: ('industry.get_extra_text_fund(economy)', 52, 48), 2554: ('industry.id', 53, 48), 2627: ('industry.id', 54, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139875069736664 = 'load: properties_industry.pynml'
_static_139875069735992 = "location_checks_industry.macros['render_tree']"
_static_139875069737168 = 'load: availability.pynml'
_static_139875069737000 = 'load: check_primary_supplies_delivered.pynml'
_static_139875070090824 = 'load: produce_primary.pynml'
_static_139875070090488 = 'load: extra_text_primary.pynml'
_static_139875068560104 = 'load: layouts.pynml'
_static_139875068561504 = 'load: properties_tile.pynml'
_static_139875068559600 = "animation_macros.macros['tile_animation']"
_static_139875068822304 = "location_checks_tile.macros['render_tree']"
_static_139875068824544 = 'load: graphics_switches.pynml'
_static_139875068821744 = 'load: spritelayouts.pynml'
_static_139875068825048 = 'load: spritesets.pynml'

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
            __backup_macroname_139875068161672 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733ca4dd8> name=None at 7f3733ca4908> -> __value
            __value = _static_139875068825048
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068161672 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068161672
            __append('\n\n')
            __backup_macroname_139875068161992 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733ca40f0> name=None at 7f3733ca42b0> -> __value
            __value = _static_139875068821744
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068161992 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068161992
            __append('\n\n')
            __backup_macroname_139875068161416 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733ca4be0> name=None at 7f3733ca4c88> -> __value
            __value = _static_139875068824544
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068161416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068161416
            __append('\n\n')
            __backup_location_checks_tile_139875068824432 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139875069863944 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733ca4320> name=None at 7f3733ca4208> -> __value
            __value = _static_139875068822304
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875069863944 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875069863944
            if (__backup_location_checks_tile_139875068824432 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139875068824432
            __append('\n\n')
            __backup_animation_macros_139875068824096 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139875068159752 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733c640f0> name=None at 7f3733c64f60> -> __value
            __value = _static_139875068559600
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068159752 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068159752
            if (__backup_animation_macros_139875068824096 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139875068824096
            __append('\n\n')
            __backup_macroname_139875068158856 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733c64860> name=None at 7f3733c645c0> -> __value
            __value = _static_139875068561504
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068158856 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068158856
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_139875070045064 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733c642e8> name=None at 7f3733c64160> -> __value
            __value = _static_139875068560104
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070045064 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070045064
            __append('\n\n')
            __backup_macroname_139875068961736 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733dd9cf8> name=None at 7f3733dd9d68> -> __value
            __value = _static_139875070090488
            econtext['macroname'] = __value

            # <Value 'load: extra_text_primary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' extra_text_primary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068961736 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068961736
            __append('\n\n')
            __backup_macroname_139875068082760 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733dd9e48> name=None at 7f3733d83780> -> __value
            __value = _static_139875070090824
            econtext['macroname'] = __value

            # <Value 'load: produce_primary.pynml' (28:30)> -> __macro
            __token = 1054
            __macro = ' produce_primary.pynml'
            __macro = __loader(__macro)
            __token = 1054
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068082760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068082760
            __append('\n\n')
            __backup_macroname_139875068083400 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733d83828> name=None at 7f3733d83198> -> __value
            __value = _static_139875069737000
            econtext['macroname'] = __value

            # <Value 'load: check_primary_supplies_delivered.pynml' (30:30)> -> __macro
            __token = 1117
            __macro = ' check_primary_supplies_delivered.pynml'
            __macro = __loader(__macro)
            __token = 1117
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068083400 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068083400
            __append('\n\n')
            __backup_macroname_139875070044744 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733d838d0> name=None at 7f3733d83550> -> __value
            __value = _static_139875069737168
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1197
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070044744 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070044744
            __append('\n\n')
            __backup_location_checks_industry_139875068823760 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1273
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139875068158024 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733d83438> name=None at 7f3733d839b0> -> __value
            __value = _static_139875069735992
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1347
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875068158024 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875068158024
            if (__backup_location_checks_industry_139875068823760 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139875068823760
            __append('\n\n')
            __backup_macroname_139875070564552 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733d836d8> name=None at 7f3733d83978> -> __value
            __value = _static_139875069736664
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1429
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1429
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070564552 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070564552
            __append('\n\n')
            __append('\n')
            __backup_economy_139875068825216 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1613
            __iterator = getitem('economies')
            (__iterator, ____index_139875069738120, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1664
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False at 7f3733d83588> -> __content_139875089167952
                    __token = 1724
                    __token = 1739
                    __content_139875089167952 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
                    __token = 1798
                    __content_139875089167952_1796 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_1796 = __quote(__content_139875089167952_1796, '\x00', '&#0;', None, False)
                    __token = 1814
                    __content_139875089167952_1812 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139875089167952_1812 = __quote(__content_139875089167952_1812, '\x00', '&#0;', None, False)
                    __token = 1913
                    __content_139875089167952_1911 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_1911 = __quote(__content_139875089167952_1911, '\x00', '&#0;', None, False)
                    __token = 2079
                    __content_139875089167952_2077 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2077 = __quote(__content_139875089167952_2077, '\x00', '&#0;', None, False)
                    __token = 2149
                    __content_139875089167952_2147 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2147 = __quote(__content_139875089167952_2147, '\x00', '&#0;', None, False)
                    __token = 2229
                    __content_139875089167952_2227 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2227 = __quote(__content_139875089167952_2227, '\x00', '&#0;', None, False)
                    __token = 2389
                    __content_139875089167952_2387 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2387 = __quote(__content_139875089167952_2387, '\x00', '&#0;', None, False)
                    __token = 2466
                    __content_139875089167952_2464 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139875089167952_2464 = __quote(__content_139875089167952_2464, '\x00', '&#0;', None, False)
                    __token = 2554
                    __content_139875089167952_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2552 = __quote(__content_139875089167952_2552, '\x00', '&#0;', None, False)
                    __token = 2627
                    __content_139875089167952_2625 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2625 = __quote(__content_139875089167952_2625, '\x00', '&#0;', None, False)
                    __content_139875089167952 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139875089167952_1796 if (__content_139875089167952_1796 is not None) else ''), ', ', (__content_139875089167952_1812 if (__content_139875089167952_1812 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_139875089167952_1911 if (__content_139875089167952_1911 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ', (__content_139875089167952_2077 if (__content_139875089167952_2077 is not None) else ''), '_produce;\n                    produce_256_ticks:        ', (__content_139875089167952_2147 if (__content_139875089167952_2147 is not None) else ''), '_produce_256_ticks;\n                    monthly_prod_change:      ', (__content_139875089167952_2227 if (__content_139875089167952_2227 is not None) else ''), '_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ', (__content_139875089167952_2387 if (__content_139875089167952_2387 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_139875089167952_2464 if (__content_139875089167952_2464 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_139875089167952_2552 if (__content_139875089167952_2552 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_139875089167952_2625 if (__content_139875089167952_2625 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
                    if (__content_139875089167952 is None):
                        pass
                    else:
                        if (__content_139875089167952 is False):
                            __content_139875089167952 = None
                        else:
                            __tt = type(__content_139875089167952)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_139875089167952 = str(__content_139875089167952)
                            else:
                                if (__tt is bytes):
                                    __content_139875089167952 = decode(__content_139875089167952)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_139875089167952 = __content_139875089167952.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_139875089167952)
                                            __content_139875089167952 = (str(__content_139875089167952) if (__content_139875089167952 is __converted) else __converted)
                                        else:
                                            __content_139875089167952 = __content_139875089167952()
                    if (__content_139875089167952 is not None):
                        __append(__content_139875089167952)
                __append('\n')
                ____index_139875069738120 -= 1
                if (____index_139875069738120 > 0):
                    __append('')
            if (__backup_economy_139875068825216 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139875068825216
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }