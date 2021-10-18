# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/cargos.pynml'

__tokens = {54: ('registered_cargos', 2, 41), 82: ('${cargo.cargo_label},', 3, 8), 84: ('cargo.cargo_label', 3, 10), 411: ('registered_cargos', 12, 26), 435: ('spriteset(cargoicon_${cargo.id}) {\n        [10 + 20 * ${cargo.icon_indices[0]}, 10 + 20 * ${cargo.icon_indices[1]}, 10, 10, 0, 0, ${"ANIM," if cargo.allow_animated_pixels else None} "src/graphics/other/cargoicons.png"]\n    }', 13, 4), 457: ('cargo.id', 13, 26), 491: ('cargo.icon_indices[0]', 14, 21), 527: ('cargo.icon_indices[1]', 14, 57), 567: ('"ANIM," if cargo.allow_animated_pixels else None', 14, 97), 697: ('economies', 18, 35), 745: ('cargo.id in economy.cargos', 19, 36), 786: ('if (economy==${economy.numeric_id}) {', 20, 12), 801: ('economy.numeric_id', 20, 27), 870: ('load: cargo_props.pynml', 21, 46), 870: ('load: cargo_props.pynml', 21, 46)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139738428980720 = 'load: cargo_props.pynml'
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
            __append('cargotable {\n    ')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428542208
            __attrs_139738428542208 = _static_139738431409216
            __backup_cargo_139738447009152 = get('cargo', __marker)

            # <Value 'registered_cargos' (2:41)> -> __iterator
            __token = 54
            __iterator = getitem('registered_cargos')
            (__iterator, ____index_139738428540912, ) = getitem('repeat')('cargo', __iterator)
            econtext['cargo'] = None
            for __item in __iterator:
                econtext['cargo'] = __item

                # <Interpolation value=<Substitution '\n        ${cargo.cargo_label},\n    ' (2:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763650250> -> __content_139738435934384
                __token = 82
                __token = 84
                __content_139738435934384 = _lookup_attr(getitem('cargo'), 'cargo_label')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s' % ('\n        ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ',\n    ', ))
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
                ____index_139738428540912 -= 1
                if (____index_139738428540912 > 0):
                    __append('')
            if (__backup_cargo_139738447009152 is __marker):
                del econtext['cargo']
            else:
                econtext['cargo'] = __backup_cargo_139738447009152
            __append('\n}\n\n\ndisable_item(FEAT_CARGOS, 0, 29);\n\ndisable_item(FEAT_CARGOS, 31, 31);\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428539904
            __attrs_139738428539904 = _static_139738431409216
            __backup_cargo_139738447017488 = get('cargo', __marker)

            # <Value 'registered_cargos' (12:26)> -> __iterator
            __token = 411
            __iterator = getitem('registered_cargos')
            (__iterator, ____index_139738428542352, ) = getitem('repeat')('cargo', __iterator)
            econtext['cargo'] = None
            for __item in __iterator:
                econtext['cargo'] = __item

                # <Interpolation value=<Substitution '\n    spriteset(cargoicon_${cargo.id}) {\n        [10 + 20 * ${cargo.icon_indices[0]}, 10 + 20 * ${cargo.icon_indices[1]}, 10, 10, 0, 0, ${"ANIM," if cargo.allow_animated_pixels else None} "src/graphics/other/cargoicons.png"]\n    }\n\n\n    ' (12:45)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763650430> -> __content_139738435934384
                __token = 435
                __token = 457
                __content_139738435934384 = _lookup_attr(getitem('cargo'), 'id')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 491
                __content_139738435934384_489 = _lookup_attr(getitem('cargo'), 'icon_indices')[0]
                __content_139738435934384_489 = __quote(__content_139738435934384_489, '\x00', '&#0;', None, None)
                __token = 527
                __content_139738435934384_525 = _lookup_attr(getitem('cargo'), 'icon_indices')[1]
                __content_139738435934384_525 = __quote(__content_139738435934384_525, '\x00', '&#0;', None, None)
                __token = 567
                __content_139738435934384_565 = ('ANIM,' if _lookup_attr(getitem('cargo'), 'allow_animated_pixels') else None)
                __content_139738435934384_565 = __quote(__content_139738435934384_565, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s' % ('\n    spriteset(cargoicon_', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') {\n        [10 + 20 * ', (__content_139738435934384_489 if (__content_139738435934384_489 is not None) else ''), ', 10 + 20 * ', (__content_139738435934384_525 if (__content_139738435934384_525 is not None) else ''), ', 10, 10, 0, 0, ', (__content_139738435934384_565 if (__content_139738435934384_565 is not None) else ''), ' "src/graphics/other/cargoicons.png"]\n    }\n\n\n    ', ))
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

                # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428980096
                __attrs_139738428980096 = _static_139738431409216
                __backup_economy_139738428980528 = get('economy', __marker)

                # <Value 'economies' (18:35)> -> __iterator
                __token = 697
                __iterator = getitem('economies')
                (__iterator, ____index_139738428977888, ) = getitem('repeat')('economy', __iterator)
                econtext['economy'] = None
                for __item in __iterator:
                    econtext['economy'] = __item
                    __append('\n        ')

                    # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428977552
                    __attrs_139738428977552 = _static_139738431409216

                    # <Value 'cargo.id in economy.cargos' (19:36)> -> __condition
                    __token = 745
                    __condition = (_lookup_attr(getitem('cargo'), 'id') in _lookup_attr(getitem('economy'), 'cargos'))
                    if __condition:

                        # <Interpolation value=<Substitution '\n            if (economy==${economy.numeric_id}) {\n                ' (19:64)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f17636bbc70> -> __content_139738435934384
                        __token = 786
                        __token = 801
                        __content_139738435934384 = _lookup_attr(getitem('economy'), 'numeric_id')
                        __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                        __content_139738435934384 = ('%s%s%s' % ('\n            if (economy==', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') {\n                ', ))
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

                        # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428978656
                        __attrs_139738428978656 = _static_139738431409216
                        __backup_macroname_139738428354944 = get('macroname', __marker)

                        # <Static value=<_ast.Constant object at 0x7f17636bbdf0> name=None at 7f17636bbd60> -> __value
                        __value = _static_139738428980720
                        econtext['macroname'] = __value

                        # <Value 'load: cargo_props.pynml' (21:46)> -> __macro
                        __token = 870
                        __macro = ' cargo_props.pynml'
                        __macro = __loader(__macro)
                        __token = 870
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_139738428354944 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_139738428354944
                        __append('\n            }\n        ')
                    __append('\n    ')
                    ____index_139738428977888 -= 1
                    if (____index_139738428977888 > 0):
                        __append('')
                if (__backup_economy_139738428980528 is __marker):
                    del econtext['economy']
                else:
                    econtext['economy'] = __backup_economy_139738428980528
                __append('\n')
                ____index_139738428542352 -= 1
                if (____index_139738428542352 > 0):
                    __append('')
            if (__backup_cargo_139738447017488 is __marker):
                del econtext['cargo']
            else:
                econtext['cargo'] = __backup_cargo_139738447017488
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }