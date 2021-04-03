# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/industry_primary_no_supplies.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1406: ('item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}', 35, 0), 1430: ('industry.id', 35, 24), 1446: ('industry.numeric_id', 35, 40), 1511: ('industry.id', 37, 29), 1645: ('industry.id', 39, 29)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166497528744 = 'load: properties_industry.pynml'
_static_140166497529752 = "location_checks_industry.macros['render_tree']"
_static_140166498388960 = 'load: availability.pynml'
_static_140166498386720 = 'load: layouts.pynml'
_static_140166498389912 = 'load: properties_tile.pynml'
_static_140166497464784 = "animation_macros.macros['tile_animation']"
_static_140166497465512 = "location_checks_tile.macros['render_tree']"
_static_140166497467640 = 'load: graphics_switches.pynml'
_static_140166499083096 = 'load: spritelayouts.pynml'
_static_140166499082928 = 'load: spritesets.pynml'

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
            __backup_macroname_140166499036296 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e6322b0> name=None at 7f7b0e632710> -> __value
            __value = _static_140166499082928
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499036296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499036296
            __append('\n\n')
            __backup_macroname_140166499037064 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e632358> name=None at 7f7b0e632128> -> __value
            __value = _static_140166499083096
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499037064 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499037064
            __append('\n\n')
            __backup_macroname_140166499035208 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4a7cf8> name=None at 7f7b0e4a7e48> -> __value
            __value = _static_140166497467640
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499035208 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499035208
            __append('\n\n')
            __backup_location_checks_tile_140166499265280 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_140166499036040 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4a74a8> name=None at 7f7b0e4a7da0> -> __value
            __value = _static_140166497465512
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499036040 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499036040
            if (__backup_location_checks_tile_140166499265280 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_140166499265280
            __append('\n\n')
            __backup_animation_macros_140166497683720 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_140166499581768 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4a71d0> name=None at 7f7b0e4a7828> -> __value
            __value = _static_140166497464784
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499581768 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499581768
            if (__backup_animation_macros_140166497683720 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_140166497683720
            __append('\n\n')
            __backup_macroname_140166503408648 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588f98> name=None at 7f7b0e588780> -> __value
            __value = _static_140166498389912
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166503408648 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166503408648
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_140166498325640 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588320> name=None at 7f7b0e588ef0> -> __value
            __value = _static_140166498386720
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498325640 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498325640
            __append('\n\n')
            __backup_macroname_140166499580872 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e588be0> name=None at 7f7b0e4b65f8> -> __value
            __value = _static_140166498388960
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166499580872 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166499580872
            __append('\n\n')
            __backup_location_checks_industry_140166497683552 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_140166498325704 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4b6f98> name=None at 7f7b0e4b63c8> -> __value
            __value = _static_140166497529752
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166498325704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166498325704
            if (__backup_location_checks_industry_140166497683552 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_140166497683552
            __append('\n\n')
            __backup_macroname_140166497696200 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7b0e4b6ba8> name=None at 7f7b0e4dce48> -> __value
            __value = _static_140166497528744
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140166497696200 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140166497696200
            __append('\n\n')
            __append('\n')

            # <Interpolation value=<Substitution '\nitem(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n' (34:38)> braces_required=True translation=False at 7f7b0e575a58> -> __content_140166518101192
            __token = 1406
            __token = 1430
            __content_140166518101192 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1446
            __content_140166518101192_1444 = _lookup_attr(getitem('industry'), 'numeric_id')
            __content_140166518101192_1444 = __quote(__content_140166518101192_1444, '\x00', '&#0;', None, False)
            __token = 1511
            __content_140166518101192_1509 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_1509 = __quote(__content_140166518101192_1509, '\x00', '&#0;', None, False)
            __token = 1645
            __content_140166518101192_1643 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_1643 = __quote(__content_140166518101192_1643, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\nitem(FEAT_INDUSTRIES, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', ', (__content_140166518101192_1444 if (__content_140166518101192_1444 is not None) else ''), ') {\n\tgraphics {\n\t\tconstruction_probability:', (__content_140166518101192_1509 if (__content_140166518101192_1509 is not None) else ''), '_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ', (__content_140166518101192_1643 if (__content_140166518101192_1643 is not None) else ''), '_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n', ))
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

    return {'render': render, }