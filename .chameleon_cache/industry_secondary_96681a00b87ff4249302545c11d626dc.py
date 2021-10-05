# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/XIS/src/templates/industry_secondary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: produce_secondary.pynml', 26, 30), 988: ('load: produce_secondary.pynml', 26, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1186: ('load: availability.pynml', 32, 30), 1186: ('load: availability.pynml', 32, 30), 1262: ('load: location_check_macros_industry.pynml', 34, 46), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1602: ('economies', 40, 37), 1653: ("industry.get_property('enabled', economy) == True", 41, 39), 1713: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1728: ('economy.numeric_id', 42, 23), 1787: ('industry.id', 43, 36), 1803: ('industry.numeric_id', 43, 52), 1902: ('industry.id', 45, 48), 1983: ('industry.id', 46, 48), 2053: ('industry.id', 47, 48), 2148: ('industry.id', 48, 48), 2234: ('industry.id', 49, 48), 2311: ('industry.get_extra_text_fund(economy)', 50, 48), 2399: ('industry.id', 51, 48), 2472: ('industry.id', 52, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139875070272008 = 'load: properties_industry.pynml'
_static_139875070631216 = "location_checks_industry.macros['render_tree']"
_static_139875070628192 = 'load: availability.pynml'
_static_139875070629032 = 'load: extra_text_secondary.pynml'
_static_139875070630040 = 'load: closure_secondary.pynml'
_static_139875070628248 = 'load: produce_secondary.pynml'
_static_139875070629312 = 'load: layouts.pynml'
_static_139875070628136 = 'load: properties_tile.pynml'
_static_139875070629536 = "animation_macros.macros['tile_animation']"
_static_139875070631328 = "location_checks_tile.macros['render_tree']"
_static_139875070544136 = 'load: graphics_switches.pynml'
_static_139875070542624 = 'load: spritelayouts.pynml'
_static_139875070544360 = 'load: spritesets.pynml'

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
            __backup_macroname_139875070530184 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e489e8> name=None at 7f3733e488d0> -> __value
            __value = _static_139875070544360
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070530184 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070530184
            __append('\n\n')
            __backup_macroname_139875070417224 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e48320> name=None at 7f3733e48c18> -> __value
            __value = _static_139875070542624
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070417224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070417224
            __append('\n\n')
            __backup_macroname_139875070531336 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e48908> name=None at 7f3733e5d0f0> -> __value
            __value = _static_139875070544136
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070531336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070531336
            __append('\n\n')
            __backup_location_checks_tile_139875096965808 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139875070533256 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5dda0> name=None at 7f3733e5dc88> -> __value
            __value = _static_139875070631328
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070533256 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070533256
            if (__backup_location_checks_tile_139875096965808 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139875096965808
            __append('\n\n')
            __backup_animation_macros_139875072950512 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139875070286856 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d6a0> name=None at 7f3733e5d7b8> -> __value
            __value = _static_139875070629536
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070286856 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070286856
            if (__backup_animation_macros_139875072950512 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139875072950512
            __append('\n\n')
            __backup_macroname_139875070178760 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d128> name=None at 7f3733e5d2e8> -> __value
            __value = _static_139875070628136
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070178760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070178760
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_139875070177416 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d5c0> name=None at 7f3733e5d7f0> -> __value
            __value = _static_139875070629312
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070177416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070177416
            __append('\n\n')
            __backup_macroname_139875070179464 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d198> name=None at 7f3733e5df60> -> __value
            __value = _static_139875070628248
            econtext['macroname'] = __value

            # <Value 'load: produce_secondary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' produce_secondary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070179464 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070179464
            __append('\n\n')
            __backup_macroname_139875070287560 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d898> name=None at 7f3733e5df28> -> __value
            __value = _static_139875070630040
            econtext['macroname'] = __value

            # <Value 'load: closure_secondary.pynml' (28:30)> -> __macro
            __token = 1053
            __macro = ' closure_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1053
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070287560 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070287560
            __append('\n\n')
            __backup_macroname_139875070178888 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d4a8> name=None at 7f3733e5da20> -> __value
            __value = _static_139875070629032
            econtext['macroname'] = __value

            # <Value 'load: extra_text_secondary.pynml' (30:30)> -> __macro
            __token = 1118
            __macro = ' extra_text_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1118
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070178888 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070178888
            __append('\n\n')
            __backup_macroname_139875070414536 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5d160> name=None at 7f3733e5d400> -> __value
            __value = _static_139875070628192
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1186
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1186
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070414536 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070414536
            __append('\n\n')
            __backup_location_checks_industry_139875070298152 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1262
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139875070380808 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e5dd30> name=None at 7f3733e06f60> -> __value
            __value = _static_139875070631216
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1336
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1336
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070380808 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070380808
            if (__backup_location_checks_industry_139875070298152 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139875070298152
            __append('\n\n')
            __backup_macroname_139875070390216 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f3733e06208> name=None at 7f3733e06ef0> -> __value
            __value = _static_139875070272008
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1418
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1418
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139875070390216 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139875070390216
            __append('\n\n')
            __append('\n')
            __backup_economy_139875096966816 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1602
            __iterator = getitem('economies')
            (__iterator, ____index_139875070272680, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1653
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False at 7f3733e06550> -> __content_139875089167952
                    __token = 1713
                    __token = 1728
                    __content_139875089167952 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
                    __token = 1787
                    __content_139875089167952_1785 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_1785 = __quote(__content_139875089167952_1785, '\x00', '&#0;', None, False)
                    __token = 1803
                    __content_139875089167952_1801 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_139875089167952_1801 = __quote(__content_139875089167952_1801, '\x00', '&#0;', None, False)
                    __token = 1902
                    __content_139875089167952_1900 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_1900 = __quote(__content_139875089167952_1900, '\x00', '&#0;', None, False)
                    __token = 1983
                    __content_139875089167952_1981 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_1981 = __quote(__content_139875089167952_1981, '\x00', '&#0;', None, False)
                    __token = 2053
                    __content_139875089167952_2051 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2051 = __quote(__content_139875089167952_2051, '\x00', '&#0;', None, False)
                    __token = 2148
                    __content_139875089167952_2146 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2146 = __quote(__content_139875089167952_2146, '\x00', '&#0;', None, False)
                    __token = 2234
                    __content_139875089167952_2232 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2232 = __quote(__content_139875089167952_2232, '\x00', '&#0;', None, False)
                    __token = 2311
                    __content_139875089167952_2309 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_139875089167952_2309 = __quote(__content_139875089167952_2309, '\x00', '&#0;', None, False)
                    __token = 2399
                    __content_139875089167952_2397 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2397 = __quote(__content_139875089167952_2397, '\x00', '&#0;', None, False)
                    __token = 2472
                    __content_139875089167952_2470 = _lookup_attr(getitem('industry'), 'id')
                    __content_139875089167952_2470 = __quote(__content_139875089167952_2470, '\x00', '&#0;', None, False)
                    __content_139875089167952 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_139875089167952_1785 if (__content_139875089167952_1785 is not None) else ''), ', ', (__content_139875089167952_1801 if (__content_139875089167952_1801 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_139875089167952_1900 if (__content_139875089167952_1900 is not None) else ''), '_check_availability;\n                    produce_cargo_arrival:    ', (__content_139875089167952_1981 if (__content_139875089167952_1981 is not None) else ''), '_produce;\n                    monthly_prod_change:      ', (__content_139875089167952_2051 if (__content_139875089167952_2051 is not None) else ''), '_check_secondary_production_level;\n                    random_prod_change:       ', (__content_139875089167952_2146 if (__content_139875089167952_2146 is not None) else ''), '_check_secondary_closure;\n                    location_check:           ', (__content_139875089167952_2232 if (__content_139875089167952_2232 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_139875089167952_2309 if (__content_139875089167952_2309 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_139875089167952_2397 if (__content_139875089167952_2397 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_139875089167952_2470 if (__content_139875089167952_2470 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                ____index_139875070272680 -= 1
                if (____index_139875070272680 > 0):
                    __append('')
            if (__backup_economy_139875096966816 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139875096966816
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }