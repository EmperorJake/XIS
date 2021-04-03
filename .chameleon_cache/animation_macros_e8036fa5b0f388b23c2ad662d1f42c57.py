# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/animation_macros.pynml'
__tokens = {157: ('industry.tiles', 4, 28), 221: ('tile.custom_animation_control is not None', 5, 47), 317: ("tile.animation_macros()[tile.custom_animation_control['macro']]", 6, 53), 317: ("tile.animation_macros()[tile.custom_animation_control['macro']]", 6, 53), 1547: ('switch(FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, (extra_callback_info1 % ${tile.animation_length})) {', 31, 4), 1582: ('tile.id', 31, 39), 1631: ('tile.animation_length', 31, 88), 1692: ('range(tile.animation_length)', 32, 34), 1735: ('${repeat.frame.index}: return ${repeat.frame.index};', 33, 12), 1737: ('repeat.frame.index', 33, 14), 1767: ('repeat.frame.index', 33, 44), 2041: ('switch(FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, 0) {\n        return 0;\n    }', 42, 4), 2076: ('tile.id', 42, 39), 2283: ("switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_stop_anim, animation_frame) {\n        1: return 11; // jump to the 'stop animation cycle' when triggered and currently animated\n        2: return 12;\n        3: return 13;\n        4: return 14;\n        5: return 15;\n        6: return 16;\n        7: return 17;\n        8: return 18;\n        9: return 19;\n        10: return 20;\n        return CB_RESULT_DO_NOTHING;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_start_anim, animation_frame) {\n        11: return 1;\n        12: return 2;\n        13: return 3;\n        14: return 4;\n        15: return 5;\n        16: return 6;\n        17: return 7;\n        18: return 8;\n        19: return 9;\n        20: return 10;\n        return CB_RESULT_START_ANIMATION;\n    }\n\n    random_switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, bitmask(TRIGGER_INDUSTRYTILE_TILELOOP)) {\n        1: return ${tile.id}_stop_anim;\n        1: return ${tile.id}_start_anim;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${tile.custom_animation_next_frame}, animation_frame) {\n        10: return 1;\n        11: return CB_RESULT_STOP_ANIMATION; // Don't actually stop animation, just keep looping the same frame over and over.\n        20: return 11;\n        return CB_RESULT_NEXT_FRAME;\n    }", 49, 4), 2319: ('tile.id', 49, 40), 2739: ('tile.id', 63, 40), 3096: ('tile.id', 77, 47), 3181: ('tile.id', 78, 20), 3221: ('tile.id', 79, 20), 3289: ('tile.custom_animation_next_frame', 82, 40)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166498189664 = "tile.animation_macros()[tile.custom_animation_control['macro']]"

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render_tile_animation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')
            __backup_tile_140166498963184 = get('tile', __marker)

            # <Value 'industry.tiles' (4:28)> -> __iterator
            __token = 157
            __iterator = _lookup_attr(getitem('industry'), 'tiles')
            (__iterator, ____index_140166499557448, ) = getitem('repeat')('tile', __iterator)
            econtext['tile'] = None
            for __item in __iterator:
                econtext['tile'] = __item
                __append('\n        ')

                # <Value 'tile.custom_animation_control is not None' (5:47)> -> __condition
                __token = 221
                __condition = (_lookup_attr(getitem('tile'), 'custom_animation_control') is not None)
                if __condition:
                    __backup_macroname_140166499261768 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f7b0e558160> name=None at 7f7b0e558198> -> __value
                    __value = _static_140166498189664
                    econtext['macroname'] = __value

                    # <Value "tile.animation_macros()[tile.custom_animation_control['macro']]" (6:53)> -> __macro
                    __token = 317
                    __macro = _lookup_attr(getitem('tile'), 'animation_macros')()[_lookup_attr(getitem('tile'), 'custom_animation_control')['macro']]
                    __token = 317
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140166499261768 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140166499261768
                __append('\n    ')
                ____index_140166499557448 -= 1
                if (____index_140166499557448 > 0):
                    __append('')
            if (__backup_tile_140166498963184 is __marker):
                del econtext['tile']
            else:
                econtext['tile'] = __backup_tile_140166498963184
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_random_first_frame(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, (extra_callback_info1 % ${tile.animation_length})) {\n        ' (30:7)> braces_required=True translation=False at 7f7b0e558240> -> __content_140166518101192
            __token = 1547
            __token = 1582
            __content_140166518101192 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1631
            __content_140166518101192_1629 = _lookup_attr(getitem('tile'), 'animation_length')
            __content_140166518101192_1629 = __quote(__content_140166518101192_1629, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), '_anim_control, (extra_callback_info1 % ', (__content_140166518101192_1629 if (__content_140166518101192_1629 is not None) else ''), ')) {\n        ', ))
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
            __backup_frame_140166499152784 = get('frame', __marker)

            # <Value 'range(tile.animation_length)' (32:34)> -> __iterator
            __token = 1692
            __iterator = get('range', range)(_lookup_attr(getitem('tile'), 'animation_length'))
            (__iterator, ____index_140166498190840, ) = getitem('repeat')('frame', __iterator)
            econtext['frame'] = None
            for __item in __iterator:
                econtext['frame'] = __item

                # <Interpolation value=<Substitution '\n            ${repeat.frame.index}: return ${repeat.frame.index};\n        ' (32:64)> braces_required=True translation=False at 7f7b0e558fd0> -> __content_140166518101192
                __token = 1735
                __token = 1737
                __content_140166518101192 = _lookup_attr(_lookup_attr(getitem('repeat'), 'frame'), 'index')
                __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
                __token = 1767
                __content_140166518101192_1765 = _lookup_attr(_lookup_attr(getitem('repeat'), 'frame'), 'index')
                __content_140166518101192_1765 = __quote(__content_140166518101192_1765, '\x00', '&#0;', None, False)
                __content_140166518101192 = ('%s%s%s%s%s' % ('\n            ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ': return ', (__content_140166518101192_1765 if (__content_140166518101192_1765 is not None) else ''), ';\n        ', ))
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
                ____index_140166498190840 -= 1
                if (____index_140166498190840 > 0):
                    __append('')
            if (__backup_frame_140166499152784 is __marker):
                del econtext['frame']
            else:
                econtext['frame'] = __backup_frame_140166499152784
            __append('\n        return CB_RESULT_NEXT_FRAME;\n    }\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_first_frame_is_0(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, 0) {\n        return 0;\n    }\n' (41:90)> braces_required=True translation=False at 7f7b0e5585c0> -> __content_140166518101192
            __token = 2041
            __token = 2076
            __content_140166518101192 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s' % ('\n    switch(FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), '_anim_control, 0) {\n        return 0;\n    }\n', ))
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


    def render_oil_wells(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n    ')

            # <Interpolation value=<Substitution "\n    switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_stop_anim, animation_frame) {\n        1: return 11; // jump to the 'stop animation cycle' when triggered and currently animated\n        2: return 12;\n        3: return 13;\n        4: return 14;\n        5: return 15;\n        6: return 16;\n        7: return 17;\n        8: return 18;\n        9: return 19;\n        10: return 20;\n        return CB_RESULT_DO_NOTHING;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_start_anim, animation_frame) {\n        11: return 1;\n        12: return 2;\n        13: return 3;\n        14: return 4;\n        15: return 5;\n        16: return 6;\n        17: return 7;\n        18: return 8;\n        19: return 9;\n        20: return 10;\n        return CB_RESULT_START_ANIMATION;\n    }\n\n    random_switch (FEAT_INDUSTRYTILES, SELF, ${tile.id}_anim_control, bitmask(TRIGGER_INDUSTRYTILE_TILELOOP)) {\n        1: return ${tile.id}_stop_anim;\n        1: return ${tile.id}_start_anim;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ${tile.custom_animation_next_frame}, animation_frame) {\n        10: return 1;\n        11: return CB_RESULT_STOP_ANIMATION; // Don't actually stop animation, just keep looping the same frame over and over.\n        20: return 11;\n        return CB_RESULT_NEXT_FRAME;\n    }\n" (48:74)> braces_required=True translation=False at 7f7b0e558358> -> __content_140166518101192
            __token = 2283
            __token = 2319
            __content_140166518101192 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 2739
            __content_140166518101192_2737 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192_2737 = __quote(__content_140166518101192_2737, '\x00', '&#0;', None, False)
            __token = 3096
            __content_140166518101192_3094 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192_3094 = __quote(__content_140166518101192_3094, '\x00', '&#0;', None, False)
            __token = 3181
            __content_140166518101192_3179 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192_3179 = __quote(__content_140166518101192_3179, '\x00', '&#0;', None, False)
            __token = 3221
            __content_140166518101192_3219 = _lookup_attr(getitem('tile'), 'id')
            __content_140166518101192_3219 = __quote(__content_140166518101192_3219, '\x00', '&#0;', None, False)
            __token = 3289
            __content_140166518101192_3287 = _lookup_attr(getitem('tile'), 'custom_animation_next_frame')
            __content_140166518101192_3287 = __quote(__content_140166518101192_3287, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), "_stop_anim, animation_frame) {\n        1: return 11; // jump to the 'stop animation cycle' when triggered and currently animated\n        2: return 12;\n        3: return 13;\n        4: return 14;\n        5: return 15;\n        6: return 16;\n        7: return 17;\n        8: return 18;\n        9: return 19;\n        10: return 20;\n        return CB_RESULT_DO_NOTHING;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ", (__content_140166518101192_2737 if (__content_140166518101192_2737 is not None) else ''), '_start_anim, animation_frame) {\n        11: return 1;\n        12: return 2;\n        13: return 3;\n        14: return 4;\n        15: return 5;\n        16: return 6;\n        17: return 7;\n        18: return 8;\n        19: return 9;\n        20: return 10;\n        return CB_RESULT_START_ANIMATION;\n    }\n\n    random_switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192_3094 if (__content_140166518101192_3094 is not None) else ''), '_anim_control, bitmask(TRIGGER_INDUSTRYTILE_TILELOOP)) {\n        1: return ', (__content_140166518101192_3179 if (__content_140166518101192_3179 is not None) else ''), '_stop_anim;\n        1: return ', (__content_140166518101192_3219 if (__content_140166518101192_3219 is not None) else ''), '_start_anim;\n    }\n\n    switch (FEAT_INDUSTRYTILES, SELF, ', (__content_140166518101192_3287 if (__content_140166518101192_3287 is not None) else ''), ", animation_frame) {\n        10: return 1;\n        11: return CB_RESULT_STOP_ANIMATION; // Don't actually stop animation, just keep looping the same frame over and over.\n        20: return 11;\n        return CB_RESULT_NEXT_FRAME;\n    }\n", ))
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
            __append('\n\n')
            __token = None
            render_tile_animation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __append('\n\n')
            __append('\n\n')
            __token = None
            render_random_first_frame(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_first_frame_is_0(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __token = None
            render_oil_wells(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_tile_animation': render_tile_animation, 'render_random_first_frame': render_random_first_frame, 'render_first_frame_is_0': render_first_frame_is_0, 'render_oil_wells': render_oil_wells, 'render': render, }