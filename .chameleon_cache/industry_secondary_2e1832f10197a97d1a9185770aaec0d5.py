# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/industry_secondary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: produce_secondary.pynml', 26, 30), 988: ('load: produce_secondary.pynml', 26, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1053: ('load: closure_secondary.pynml', 28, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1118: ('load: extra_text_secondary.pynml', 30, 30), 1186: ('load: availability.pynml', 32, 30), 1186: ('load: availability.pynml', 32, 30), 1262: ('load: location_check_macros_industry.pynml', 34, 46), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1336: ("location_checks_industry.macros['render_tree']", 35, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1418: ('load: properties_industry.pynml', 37, 30), 1602: ('economies', 40, 37), 1653: ("industry.get_property('enabled', economy) == True", 41, 39), 1713: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1728: ('economy.numeric_id', 42, 23), 1787: ('industry.id', 43, 36), 1803: ('industry.numeric_id', 43, 52), 1902: ('industry.id', 45, 48), 1983: ('industry.id', 46, 48), 2053: ('industry.id', 47, 48), 2148: ('industry.id', 48, 48), 2234: ('industry.id', 49, 48), 2311: ('industry.get_extra_text_fund(economy)', 50, 48), 2399: ('industry.id', 51, 48), 2472: ('industry.id', 52, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140302364747088 = 'load: properties_industry.pynml'
_static_140302364749328 = "location_checks_industry.macros['render_tree']"
_static_140302364747144 = 'load: availability.pynml'
_static_140302364745800 = 'load: extra_text_secondary.pynml'
_static_140302364818288 = 'load: closure_secondary.pynml'
_static_140302364817392 = 'load: produce_secondary.pynml'
_static_140302364817784 = 'load: layouts.pynml'
_static_140302364819240 = 'load: properties_tile.pynml'
_static_140302364817896 = "animation_macros.macros['tile_animation']"
_static_140302364816608 = "location_checks_tile.macros['render_tree']"
_static_140302364818120 = 'load: graphics_switches.pynml'
_static_140302364816104 = 'load: spritelayouts.pynml'
_static_140302364467888 = 'load: spritesets.pynml'

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
            __backup_macroname_140302364938952 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09862b0> name=None at 7f9ab0986e80> -> __value
            __value = _static_140302364467888
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364938952 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364938952
            __append('\n\n')
            __backup_macroname_140302364369160 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09db2e8> name=None at 7f9ab09db940> -> __value
            __value = _static_140302364816104
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364369160 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364369160
            __append('\n\n')
            __backup_macroname_140302364371336 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09dbac8> name=None at 7f9ab09db8d0> -> __value
            __value = _static_140302364818120
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364371336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364371336
            __append('\n\n')
            __backup_location_checks_tile_140302390806288 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_140302364369992 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09db4e0> name=None at 7f9ab09db470> -> __value
            __value = _static_140302364816608
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364369992 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364369992
            if (__backup_location_checks_tile_140302390806288 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_140302390806288
            __append('\n\n')
            __backup_animation_macros_140302390818296 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_140302364812296 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09db9e8> name=None at 7f9ab09db278> -> __value
            __value = _static_140302364817896
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364812296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364812296
            if (__backup_animation_macros_140302390818296 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_140302390818296
            __append('\n\n')
            __backup_macroname_140302364623304 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09dbf28> name=None at 7f9ab09dbc18> -> __value
            __value = _static_140302364819240
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364623304 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364623304
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_140302364197064 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09db978> name=None at 7f9ab09dbef0> -> __value
            __value = _static_140302364817784
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364197064 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364197064
            __append('\n\n')
            __backup_macroname_140302364198344 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09db7f0> name=None at 7f9ab09db860> -> __value
            __value = _static_140302364817392
            econtext['macroname'] = __value

            # <Value 'load: produce_secondary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' produce_secondary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364198344 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364198344
            __append('\n\n')
            __backup_macroname_140302364811848 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09dbb70> name=None at 7f9ab09dbd30> -> __value
            __value = _static_140302364818288
            econtext['macroname'] = __value

            # <Value 'load: closure_secondary.pynml' (28:30)> -> __macro
            __token = 1053
            __macro = ' closure_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1053
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364811848 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364811848
            __append('\n\n')
            __backup_macroname_140302364200776 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09ca048> name=None at 7f9ab09cab38> -> __value
            __value = _static_140302364745800
            econtext['macroname'] = __value

            # <Value 'load: extra_text_secondary.pynml' (30:30)> -> __macro
            __token = 1118
            __macro = ' extra_text_secondary.pynml'
            __macro = __loader(__macro)
            __token = 1118
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364200776 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364200776
            __append('\n\n')
            __backup_macroname_140302364952584 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09ca588> name=None at 7f9ab09ca860> -> __value
            __value = _static_140302364747144
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1186
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1186
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364952584 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364952584
            __append('\n\n')
            __backup_location_checks_industry_140302390808416 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1262
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_140302364511304 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09cae10> name=None at 7f9ab09ca6a0> -> __value
            __value = _static_140302364749328
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1336
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1336
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364511304 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364511304
            if (__backup_location_checks_industry_140302390808416 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_140302390808416
            __append('\n\n')
            __backup_macroname_140302364511112 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f9ab09ca550> name=None at 7f9ab09ca3c8> -> __value
            __value = _static_140302364747088
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1418
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1418
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140302364511112 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140302364511112
            __append('\n\n')
            __append('\n')
            __backup_economy_140302364495376 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1602
            __iterator = getitem('economies')
            (__iterator, ____index_140302364748320, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1653
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    monthly_prod_change:      ${industry.id}_check_secondary_production_level;\n                    random_prod_change:       ${industry.id}_check_secondary_closure;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False at 7f9ab09cac88> -> __content_140302383355024
                    __token = 1713
                    __token = 1728
                    __content_140302383355024 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_140302383355024 = __quote(__content_140302383355024, '\x00', '&#0;', None, False)
                    __token = 1787
                    __content_140302383355024_1785 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_1785 = __quote(__content_140302383355024_1785, '\x00', '&#0;', None, False)
                    __token = 1803
                    __content_140302383355024_1801 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_140302383355024_1801 = __quote(__content_140302383355024_1801, '\x00', '&#0;', None, False)
                    __token = 1902
                    __content_140302383355024_1900 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_1900 = __quote(__content_140302383355024_1900, '\x00', '&#0;', None, False)
                    __token = 1983
                    __content_140302383355024_1981 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_1981 = __quote(__content_140302383355024_1981, '\x00', '&#0;', None, False)
                    __token = 2053
                    __content_140302383355024_2051 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_2051 = __quote(__content_140302383355024_2051, '\x00', '&#0;', None, False)
                    __token = 2148
                    __content_140302383355024_2146 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_2146 = __quote(__content_140302383355024_2146, '\x00', '&#0;', None, False)
                    __token = 2234
                    __content_140302383355024_2232 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_2232 = __quote(__content_140302383355024_2232, '\x00', '&#0;', None, False)
                    __token = 2311
                    __content_140302383355024_2309 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_140302383355024_2309 = __quote(__content_140302383355024_2309, '\x00', '&#0;', None, False)
                    __token = 2399
                    __content_140302383355024_2397 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_2397 = __quote(__content_140302383355024_2397, '\x00', '&#0;', None, False)
                    __token = 2472
                    __content_140302383355024_2470 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_2470 = __quote(__content_140302383355024_2470, '\x00', '&#0;', None, False)
                    __content_140302383355024 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_140302383355024 if (__content_140302383355024 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_140302383355024_1785 if (__content_140302383355024_1785 is not None) else ''), ', ', (__content_140302383355024_1801 if (__content_140302383355024_1801 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_140302383355024_1900 if (__content_140302383355024_1900 is not None) else ''), '_check_availability;\n                    produce_cargo_arrival:    ', (__content_140302383355024_1981 if (__content_140302383355024_1981 is not None) else ''), '_produce;\n                    monthly_prod_change:      ', (__content_140302383355024_2051 if (__content_140302383355024_2051 is not None) else ''), '_check_secondary_production_level;\n                    random_prod_change:       ', (__content_140302383355024_2146 if (__content_140302383355024_2146 is not None) else ''), '_check_secondary_closure;\n                    location_check:           ', (__content_140302383355024_2232 if (__content_140302383355024_2232 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_140302383355024_2309 if (__content_140302383355024_2309 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_140302383355024_2397 if (__content_140302383355024_2397 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_140302383355024_2470 if (__content_140302383355024_2470 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
                    if (__content_140302383355024 is None):
                        pass
                    else:
                        if (__content_140302383355024 is False):
                            __content_140302383355024 = None
                        else:
                            __tt = type(__content_140302383355024)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140302383355024 = str(__content_140302383355024)
                            else:
                                if (__tt is bytes):
                                    __content_140302383355024 = decode(__content_140302383355024)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140302383355024 = __content_140302383355024.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140302383355024)
                                            __content_140302383355024 = (str(__content_140302383355024) if (__content_140302383355024 is __converted) else __converted)
                                        else:
                                            __content_140302383355024 = __content_140302383355024()
                    if (__content_140302383355024 is not None):
                        __append(__content_140302383355024)
                __append('\n')
                ____index_140302364748320 -= 1
                if (____index_140302364748320 > 0):
                    __append('')
            if (__backup_economy_140302364495376 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140302364495376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }