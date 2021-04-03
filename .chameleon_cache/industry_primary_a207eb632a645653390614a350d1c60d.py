# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/firs-3.0.10-source/bundle_dir/src/src/templates/industry_primary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1197: ('load: availability.pynml', 32, 30), 1197: ('load: availability.pynml', 32, 30), 1273: ('load: location_check_macros_industry.pynml', 34, 46), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1613: ('economies', 40, 37), 1664: ("industry.get_property('enabled', economy) == True", 41, 39), 1724: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1739: ('economy.numeric_id', 42, 23), 1798: ('industry.id', 43, 36), 1814: ('industry.numeric_id', 43, 52), 1913: ('industry.id', 45, 48), 2079: ('industry.id', 47, 48), 2149: ('industry.id', 48, 48), 2229: ('industry.id', 49, 48), 2389: ('industry.id', 51, 48), 2466: ('industry.get_extra_text_fund(economy)', 52, 48), 2554: ('industry.id', 53, 48), 2627: ('industry.id', 54, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140183229602056 = 'load: properties_industry.pynml'
_static_140183229600656 = "location_checks_industry.macros['render_tree']"
_static_140183229602728 = 'load: availability.pynml'
_static_140183229600040 = 'load: check_primary_supplies_delivered.pynml'
_static_140183229603512 = 'load: produce_primary.pynml'
_static_140183229603176 = 'load: extra_text_primary.pynml'
_static_140183229602280 = 'load: layouts.pynml'
_static_140183229047136 = 'load: properties_tile.pynml'
_static_140183229049320 = "animation_macros.macros['tile_animation']"
_static_140183229048760 = "location_checks_tile.macros['render_tree']"
_static_140183229048536 = 'load: graphics_switches.pynml'
_static_140183229047024 = 'load: spritelayouts.pynml'
_static_140183229050440 = 'load: spritesets.pynml'

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
            __backup_macroname_140183228525512 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef3922e48> name=None at 7f7ef39225f8> -> __value
            __value = _static_140183229050440
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228525512 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228525512
            __append('\n\n')
            __backup_macroname_140183228610184 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39220f0> name=None at 7f7ef3922128> -> __value
            __value = _static_140183229047024
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228610184 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228610184
            __append('\n\n')
            __backup_macroname_140183228700680 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39226d8> name=None at 7f7ef3922828> -> __value
            __value = _static_140183229048536
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228700680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228700680
            __append('\n\n')
            __backup_location_checks_tile_140183229332056 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_140183228702536 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39227b8> name=None at 7f7ef3922b38> -> __value
            __value = _static_140183229048760
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228702536 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228702536
            if (__backup_location_checks_tile_140183229332056 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_140183229332056
            __append('\n\n')
            __backup_animation_macros_140183229453928 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_140183228716296 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39229e8> name=None at 7f7ef3922908> -> __value
            __value = _static_140183229049320
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228716296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228716296
            if (__backup_animation_macros_140183229453928 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_140183229453928
            __append('\n\n')
            __backup_macroname_140183229251528 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef3922160> name=None at 7f7ef3922978> -> __value
            __value = _static_140183229047136
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229251528 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229251528
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_140183229353288 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a99e8> name=None at 7f7ef39a9278> -> __value
            __value = _static_140183229602280
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229353288 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229353288
            __append('\n\n')
            __backup_macroname_140183229196808 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9d68> name=None at 7f7ef39a90f0> -> __value
            __value = _static_140183229603176
            econtext['macroname'] = __value

            # <Value 'load: extra_text_primary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' extra_text_primary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229196808 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229196808
            __append('\n\n')
            __backup_macroname_140183228736520 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9eb8> name=None at 7f7ef39a98d0> -> __value
            __value = _static_140183229603512
            econtext['macroname'] = __value

            # <Value 'load: produce_primary.pynml' (28:30)> -> __macro
            __token = 1054
            __macro = ' produce_primary.pynml'
            __macro = __loader(__macro)
            __token = 1054
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228736520 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228736520
            __append('\n\n')
            __backup_macroname_140183228710344 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9128> name=None at 7f7ef39a9828> -> __value
            __value = _static_140183229600040
            econtext['macroname'] = __value

            # <Value 'load: check_primary_supplies_delivered.pynml' (30:30)> -> __macro
            __token = 1117
            __macro = ' check_primary_supplies_delivered.pynml'
            __macro = __loader(__macro)
            __token = 1117
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228710344 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228710344
            __append('\n\n')
            __backup_macroname_140183230867208 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9ba8> name=None at 7f7ef39a9240> -> __value
            __value = _static_140183229602728
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1197
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183230867208 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183230867208
            __append('\n\n')
            __backup_location_checks_industry_140183229331832 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1273
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_140183230252488 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9390> name=None at 7f7ef39a9358> -> __value
            __value = _static_140183229600656
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1347
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183230252488 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183230252488
            if (__backup_location_checks_industry_140183229331832 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_140183229331832
            __append('\n\n')
            __backup_macroname_140183229353416 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39a9908> name=None at 7f7ef39a9438> -> __value
            __value = _static_140183229602056
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1429
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1429
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229353416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229353416
            __append('\n\n')
            __append('\n')
            __backup_economy_140183229452360 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1613
            __iterator = getitem('economies')
            (__iterator, ____index_140183229602896, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1664
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False at 7f7ef541cf28> -> __content_140183249773656
                    __token = 1724
                    __token = 1739
                    __content_140183249773656 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
                    __token = 1798
                    __content_140183249773656_1796 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_1796 = __quote(__content_140183249773656_1796, '\x00', '&#0;', None, False)
                    __token = 1814
                    __content_140183249773656_1812 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_140183249773656_1812 = __quote(__content_140183249773656_1812, '\x00', '&#0;', None, False)
                    __token = 1913
                    __content_140183249773656_1911 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_1911 = __quote(__content_140183249773656_1911, '\x00', '&#0;', None, False)
                    __token = 2079
                    __content_140183249773656_2077 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2077 = __quote(__content_140183249773656_2077, '\x00', '&#0;', None, False)
                    __token = 2149
                    __content_140183249773656_2147 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2147 = __quote(__content_140183249773656_2147, '\x00', '&#0;', None, False)
                    __token = 2229
                    __content_140183249773656_2227 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2227 = __quote(__content_140183249773656_2227, '\x00', '&#0;', None, False)
                    __token = 2389
                    __content_140183249773656_2387 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2387 = __quote(__content_140183249773656_2387, '\x00', '&#0;', None, False)
                    __token = 2466
                    __content_140183249773656_2464 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_140183249773656_2464 = __quote(__content_140183249773656_2464, '\x00', '&#0;', None, False)
                    __token = 2554
                    __content_140183249773656_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2552 = __quote(__content_140183249773656_2552, '\x00', '&#0;', None, False)
                    __token = 2627
                    __content_140183249773656_2625 = _lookup_attr(getitem('industry'), 'id')
                    __content_140183249773656_2625 = __quote(__content_140183249773656_2625, '\x00', '&#0;', None, False)
                    __content_140183249773656 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_140183249773656_1796 if (__content_140183249773656_1796 is not None) else ''), ', ', (__content_140183249773656_1812 if (__content_140183249773656_1812 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_140183249773656_1911 if (__content_140183249773656_1911 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ', (__content_140183249773656_2077 if (__content_140183249773656_2077 is not None) else ''), '_produce;\n                    produce_256_ticks:        ', (__content_140183249773656_2147 if (__content_140183249773656_2147 is not None) else ''), '_produce_256_ticks;\n                    monthly_prod_change:      ', (__content_140183249773656_2227 if (__content_140183249773656_2227 is not None) else ''), '_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ', (__content_140183249773656_2387 if (__content_140183249773656_2387 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_140183249773656_2464 if (__content_140183249773656_2464 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_140183249773656_2552 if (__content_140183249773656_2552 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_140183249773656_2625 if (__content_140183249773656_2625 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
                    if (__content_140183249773656 is None):
                        pass
                    else:
                        if (__content_140183249773656 is False):
                            __content_140183249773656 = None
                        else:
                            __tt = type(__content_140183249773656)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140183249773656 = str(__content_140183249773656)
                            else:
                                if (__tt is bytes):
                                    __content_140183249773656 = decode(__content_140183249773656)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140183249773656 = __content_140183249773656.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140183249773656)
                                            __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                        else:
                                            __content_140183249773656 = __content_140183249773656()
                    if (__content_140183249773656 is not None):
                        __append(__content_140183249773656)
                __append('\n')
                ____index_140183229602896 -= 1
                if (____index_140183229602896 > 0):
                    __append('')
            if (__backup_economy_140183229452360 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140183229452360
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }