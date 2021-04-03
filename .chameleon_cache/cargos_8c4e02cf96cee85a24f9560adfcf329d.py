# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/cargos.pynml'
__tokens = {54: ('registered_cargos', 2, 41), 82: ('${cargo.cargo_label},', 3, 8), 84: ('cargo.cargo_label', 3, 10), 411: ('registered_cargos', 12, 26), 435: ('spriteset(cargoicon_${cargo.id}) {\n        [10 + 20 * ${cargo.icon_indices[0]}, 10 + 20 * ${cargo.icon_indices[1]}, 10, 10, 0, 0, ${"ANIM," if cargo.allow_animated_pixels else None} "src/graphics/other/cargoicons.png"]\n    }', 13, 4), 457: ('cargo.id', 13, 26), 491: ('cargo.icon_indices[0]', 14, 21), 527: ('cargo.icon_indices[1]', 14, 57), 567: ('"ANIM," if cargo.allow_animated_pixels else None', 14, 97), 697: ('economies', 18, 35), 745: ('cargo.id in economy.cargos', 19, 36), 786: ('if (economy==${economy.numeric_id}) {', 20, 12), 801: ('economy.numeric_id', 20, 27), 870: ('load: cargo_props.pynml', 21, 46), 870: ('load: cargo_props.pynml', 21, 46)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166499507840 = 'load: cargo_props.pynml'

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
            __append('cargotable {\n    ')
            __backup_cargo_140166525544656 = get('cargo', __marker)

            # <Value 'registered_cargos' (2:41)> -> __iterator
            __token = 54
            __iterator = getitem('registered_cargos')
            (__iterator, ____index_140166499507336, ) = getitem('repeat')('cargo', __iterator)
            econtext['cargo'] = None
            for __item in __iterator:
                econtext['cargo'] = __item

                # <Interpolation value=<Substitution '\n        ${cargo.cargo_label},\n    ' (2:60)> braces_required=True translation=False at 7f7b0e6990f0> -> __content_140166518101192
                __token = 82
                __token = 84
                __content_140166518101192 = _lookup_attr(getitem('cargo'), 'cargo_label')
                __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
                __content_140166518101192 = ('%s%s%s' % ('\n        ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n    ', ))
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
                ____index_140166499507336 -= 1
                if (____index_140166499507336 > 0):
                    __append('')
            if (__backup_cargo_140166525544656 is __marker):
                del econtext['cargo']
            else:
                econtext['cargo'] = __backup_cargo_140166525544656
            __append('\n}\n\n')
            __append('\ndisable_item(FEAT_CARGOS, 0, 29);\n')
            __append('\ndisable_item(FEAT_CARGOS, 31, 31);\n\n')
            __backup_cargo_140166525544488 = get('cargo', __marker)

            # <Value 'registered_cargos' (12:26)> -> __iterator
            __token = 411
            __iterator = getitem('registered_cargos')
            (__iterator, ____index_140166499504984, ) = getitem('repeat')('cargo', __iterator)
            econtext['cargo'] = None
            for __item in __iterator:
                econtext['cargo'] = __item

                # <Interpolation value=<Substitution '\n    spriteset(cargoicon_${cargo.id}) {\n        [10 + 20 * ${cargo.icon_indices[0]}, 10 + 20 * ${cargo.icon_indices[1]}, 10, 10, 0, 0, ${"ANIM," if cargo.allow_animated_pixels else None} "src/graphics/other/cargoicons.png"]\n    }\n\n\n    ' (12:45)> braces_required=True translation=False at 7f7b0e6992b0> -> __content_140166518101192
                __token = 435
                __token = 457
                __content_140166518101192 = _lookup_attr(getitem('cargo'), 'id')
                __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
                __token = 491
                __content_140166518101192_489 = _lookup_attr(getitem('cargo'), 'icon_indices')[0]
                __content_140166518101192_489 = __quote(__content_140166518101192_489, '\x00', '&#0;', None, False)
                __token = 527
                __content_140166518101192_525 = _lookup_attr(getitem('cargo'), 'icon_indices')[1]
                __content_140166518101192_525 = __quote(__content_140166518101192_525, '\x00', '&#0;', None, False)
                __token = 567
                __content_140166518101192_565 = ('ANIM,' if _lookup_attr(getitem('cargo'), 'allow_animated_pixels') else None)
                __content_140166518101192_565 = __quote(__content_140166518101192_565, '\x00', '&#0;', None, False)
                __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\n    spriteset(cargoicon_', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ') {\n        [10 + 20 * ', (__content_140166518101192_489 if (__content_140166518101192_489 is not None) else ''), ', 10 + 20 * ', (__content_140166518101192_525 if (__content_140166518101192_525 is not None) else ''), ', 10, 10, 0, 0, ', (__content_140166518101192_565 if (__content_140166518101192_565 is not None) else ''), ' "src/graphics/other/cargoicons.png"]\n    }\n\n\n    ', ))
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
                __backup_economy_140166525543760 = get('economy', __marker)

                # <Value 'economies' (18:35)> -> __iterator
                __token = 697
                __iterator = getitem('economies')
                (__iterator, ____index_140166499507616, ) = getitem('repeat')('economy', __iterator)
                econtext['economy'] = None
                for __item in __iterator:
                    econtext['economy'] = __item
                    __append('\n        ')

                    # <Value 'cargo.id in economy.cargos' (19:36)> -> __condition
                    __token = 745
                    __condition = (_lookup_attr(getitem('cargo'), 'id') in _lookup_attr(getitem('economy'), 'cargos'))
                    if __condition:

                        # <Interpolation value=<Substitution '\n            if (economy==${economy.numeric_id}) {\n                ' (19:64)> braces_required=True translation=False at 7f7b0e699b38> -> __content_140166518101192
                        __token = 786
                        __token = 801
                        __content_140166518101192 = _lookup_attr(getitem('economy'), 'numeric_id')
                        __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
                        __content_140166518101192 = ('%s%s%s' % ('\n            if (economy==', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ') {\n                ', ))
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
                        __backup_macroname_140166499499784 = get('macroname', __marker)

                        # <Static value=<_ast.Str object at 0x7f7b0e699e80> name=None at 7f7b0e699a90> -> __value
                        __value = _static_140166499507840
                        econtext['macroname'] = __value

                        # <Value 'load: cargo_props.pynml' (21:46)> -> __macro
                        __token = 870
                        __macro = ' cargo_props.pynml'
                        __macro = __loader(__macro)
                        __token = 870
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140166499499784 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140166499499784
                        __append('\n            }\n        ')
                    __append('\n    ')
                    ____index_140166499507616 -= 1
                    if (____index_140166499507616 > 0):
                        __append('')
                if (__backup_economy_140166525543760 is __marker):
                    del econtext['economy']
                else:
                    econtext['economy'] = __backup_economy_140166525543760
                __append('\n')
                ____index_140166499504984 -= 1
                if (____index_140166499504984 > 0):
                    __append('')
            if (__backup_cargo_140166525544488 is __marker):
                del econtext['cargo']
            else:
                econtext['cargo'] = __backup_cargo_140166525544488
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }