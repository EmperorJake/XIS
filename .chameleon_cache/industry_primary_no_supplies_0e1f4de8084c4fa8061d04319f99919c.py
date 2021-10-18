# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/industry_primary_no_supplies.pynml'

__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1406: ('item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}', 35, 0), 1430: ('industry.id', 35, 24), 1446: ('industry.numeric_id', 35, 40), 1511: ('industry.id', 37, 29), 1645: ('industry.id', 39, 29)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139738427913888 = 'load: properties_industry.pynml'
_static_139738427912784 = "location_checks_industry.macros['render_tree']"
_static_139738427914320 = 'load: availability.pynml'
_static_139738427914416 = 'load: layouts.pynml'
_static_139738426788208 = 'load: properties_tile.pynml'
_static_139738426787776 = "animation_macros.macros['tile_animation']"
_static_139738427315200 = "location_checks_tile.macros['render_tree']"
_static_139738427316352 = 'load: graphics_switches.pynml'
_static_139738427315824 = 'load: spritelayouts.pynml'
_static_139738427315968 = 'load: spritesets.pynml'
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

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427315152
            __attrs_139738427315152 = _static_139738431409216
            __backup_macroname_139738426817408 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525700> name=None at 7f1763525490> -> __value
            __value = _static_139738427315968
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426817408 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426817408
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427318080
            __attrs_139738427318080 = _static_139738431409216
            __backup_macroname_139738428424256 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525670> name=None at 7f1763525eb0> -> __value
            __value = _static_139738427315824
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428424256 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428424256
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427317408
            __attrs_139738427317408 = _static_139738431409216
            __backup_macroname_139738428425216 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525880> name=None at 7f1763525d00> -> __value
            __value = _static_139738427316352
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428425216 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428425216
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427317696
            __attrs_139738427317696 = _static_139738431409216
            __backup_location_checks_tile_139738425704304 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_139738426406848 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f1763525400> name=None at 7f1763525a30> -> __value
            __value = _static_139738427315200
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426406848 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426406848
            if (__backup_location_checks_tile_139738425704304 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_139738425704304
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426786480
            __attrs_139738426786480 = _static_139738431409216
            __backup_animation_macros_139738426787824 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_139738426406016 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a47c0> name=None at 7f17634a4f10> -> __value
            __value = _static_139738426787776
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426406016 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426406016
            if (__backup_animation_macros_139738426787824 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_139738426787824
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738426786288
            __attrs_139738426786288 = _static_139738431409216
            __backup_macroname_139738426407488 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17634a4970> name=None at 7f17634a4dc0> -> __value
            __value = _static_139738426788208
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738426407488 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738426407488
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427913216
            __attrs_139738427913216 = _static_139738431409216
            __backup_macroname_139738427149120 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17635b78b0> name=None at 7f17635b73a0> -> __value
            __value = _static_139738427914416
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738427149120 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738427149120
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427913456
            __attrs_139738427913456 = _static_139738431409216
            __backup_macroname_139738428389632 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17635b7850> name=None at 7f17635b72e0> -> __value
            __value = _static_139738427914320
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428389632 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428389632
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427916000
            __attrs_139738427916000 = _static_139738431409216
            __backup_location_checks_industry_139738425569536 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_139738428119680 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17635b7250> name=None at 7f17635b71c0> -> __value
            __value = _static_139738427912784
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428119680 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428119680
            if (__backup_location_checks_industry_139738425569536 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_139738425569536
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738427612032
            __attrs_139738427612032 = _static_139738431409216
            __backup_macroname_139738428118400 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f17635b76a0> name=None at 7f17635b7a30> -> __value
            __value = _static_139738427913888
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139738428118400 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139738428118400
            __append('\n\n\n')

            # <Interpolation value=<Substitution '\nitem(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n' (34:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176340da60> -> __content_139738435934384
            __token = 1406
            __token = 1430
            __content_139738435934384 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __token = 1446
            __content_139738435934384_1444 = _lookup_attr(getitem('industry'), 'numeric_id')
            __content_139738435934384_1444 = __quote(__content_139738435934384_1444, '\x00', '&#0;', None, None)
            __token = 1511
            __content_139738435934384_1509 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384_1509 = __quote(__content_139738435934384_1509, '\x00', '&#0;', None, None)
            __token = 1645
            __content_139738435934384_1643 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384_1643 = __quote(__content_139738435934384_1643, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s' % ('\nitem(FEAT_INDUSTRIES, ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_1444 if (__content_139738435934384_1444 is not None) else ''), ') {\n\tgraphics {\n\t\tconstruction_probability:', (__content_139738435934384_1509 if (__content_139738435934384_1509 is not None) else ''), '_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ', (__content_139738435934384_1643 if (__content_139738435934384_1643 is not None) else ''), '_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n', ))
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
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }