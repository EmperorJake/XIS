# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/availability.pynml'
__tokens = {282: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability_param, restrict_open_during_gameplay) {\n\t1..255: return CB_RESULT_IND_NO_CONSTRUCTION;         // disallow when restrictions in place\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;       // we may build\n}', 10, 0), 314: ('industry.id', 10, 32), 592: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_map_gen, extra_callback_info2 == IND_CREATION_GENERATION) {\n\t1: return CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n\t${industry.id}_check_availability_param;\n}', 16, 0), 625: ('industry.id', 16, 33), 759: ('industry.id', 18, 3), 846: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_available_game_mode, game_mode == GAMEMODE_GAME) {\n\t1: ${industry.id}_check_map_gen;\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n}', 21, 0), 879: ('industry.id', 21, 33), 949: ('industry.id', 22, 6), 1137: ('economies', 27, 35), 1153: ('/* ${industry.get_intro_year(economy)} */\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability_${economy.numeric_id}, current_date) {\n        date(${industry.get_intro_year(economy)},1,1) .. date(${industry.get_expiry_year(economy)},12,31): ${industry.id}_available_game_mode;\n        return CB_RESULT_IND_NO_CONSTRUCTION;\n    }', 28, 4), 1158: ('industry.get_intro_year(economy)', 28, 9), 1232: ('industry.id', 29, 37), 1266: ('economy.numeric_id', 29, 71), 1318: ('industry.get_intro_year(economy)', 30, 15), 1367: ('industry.get_expiry_year(economy)', 30, 64), 1412: ('industry.id', 30, 109), 1520: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability, economy) {', 35, 0), 1553: ('industry.id', 35, 33), 1639: ('economies', 36, 42), 1659: ('${economy.numeric_id}: ${industry.id}_check_availability_${economy.numeric_id};', 37, 8), 1661: ('economy.numeric_id', 37, 10), 1684: ('industry.id', 37, 33), 1718: ('economy.numeric_id', 37, 67)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

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
            __append('\n\n')

            # <Interpolation value=<Substitution '\nswitch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability_param, restrict_open_during_gameplay) {\n\t1..255: return CB_RESULT_IND_NO_CONSTRUCTION;         // disallow when restrictions in place\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;       // we may build\n}\n\n' (9:45)> braces_required=True translation=False at 7f402952a4a8> -> __content_139913568826456
            __token = 282
            __token = 314
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s' % ('\nswitch(FEAT_INDUSTRIES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_check_availability_param, restrict_open_during_gameplay) {\n\t1..255: return CB_RESULT_IND_NO_CONSTRUCTION;         // disallow when restrictions in place\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;       // we may build\n}\n\n', ))
            if (__content_139913568826456 is None):
                pass
            else:
                if (__content_139913568826456 is False):
                    __content_139913568826456 = None
                else:
                    __tt = type(__content_139913568826456)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139913568826456 = str(__content_139913568826456)
                    else:
                        if (__tt is bytes):
                            __content_139913568826456 = decode(__content_139913568826456)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139913568826456 = __content_139913568826456.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139913568826456)
                                    __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                else:
                                    __content_139913568826456 = __content_139913568826456()
            if (__content_139913568826456 is not None):
                __append(__content_139913568826456)

            # <Interpolation value=<Substitution '\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_map_gen, extra_callback_info2 == IND_CREATION_GENERATION) {\n\t1: return CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n\t${industry.id}_check_availability_param;\n}\n' (15:37)> braces_required=True translation=False at 7f402952a320> -> __content_139913568826456
            __token = 592
            __token = 625
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 759
            __content_139913568826456_757 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_757 = __quote(__content_139913568826456_757, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s' % ('\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_check_map_gen, extra_callback_info2 == IND_CREATION_GENERATION) {\n\t1: return CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n\t', (__content_139913568826456_757 if (__content_139913568826456_757 is not None) else ''), '_check_availability_param;\n}\n', ))
            if (__content_139913568826456 is None):
                pass
            else:
                if (__content_139913568826456 is False):
                    __content_139913568826456 = None
                else:
                    __tt = type(__content_139913568826456)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139913568826456 = str(__content_139913568826456)
                    else:
                        if (__tt is bytes):
                            __content_139913568826456 = decode(__content_139913568826456)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139913568826456 = __content_139913568826456.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139913568826456)
                                    __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                else:
                                    __content_139913568826456 = __content_139913568826456()
            if (__content_139913568826456 is not None):
                __append(__content_139913568826456)

            # <Interpolation value=<Substitution '\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_available_game_mode, game_mode == GAMEMODE_GAME) {\n\t1: ${industry.id}_check_map_gen;\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n}\n\n' (20:45)> braces_required=True translation=False at 7f402952a908> -> __content_139913568826456
            __token = 846
            __token = 879
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 949
            __content_139913568826456_947 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_947 = __quote(__content_139913568826456_947, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s' % ('\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_available_game_mode, game_mode == GAMEMODE_GAME) {\n\t1: ', (__content_139913568826456_947 if (__content_139913568826456_947 is not None) else ''), '_check_map_gen;\n\treturn CB_RESULT_IND_PROBABILITY_FROM_PROPERTY;\n}\n\n', ))
            if (__content_139913568826456 is None):
                pass
            else:
                if (__content_139913568826456 is False):
                    __content_139913568826456 = None
                else:
                    __tt = type(__content_139913568826456)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139913568826456 = str(__content_139913568826456)
                    else:
                        if (__tt is bytes):
                            __content_139913568826456 = decode(__content_139913568826456)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139913568826456 = __content_139913568826456.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139913568826456)
                                    __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                else:
                                    __content_139913568826456 = __content_139913568826456()
            if (__content_139913568826456 is not None):
                __append(__content_139913568826456)
            __append('\n')
            __backup_economy_139913547928464 = get('economy', __marker)

            # <Value 'economies' (27:35)> -> __iterator
            __token = 1137
            __iterator = getitem('economies')
            (__iterator, ____index_139913547917632, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n    /* ${industry.get_intro_year(economy)} */\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability_${economy.numeric_id}, current_date) {\n        date(${industry.get_intro_year(economy)},1,1) .. date(${industry.get_expiry_year(economy)},12,31): ${industry.id}_available_game_mode;\n        return CB_RESULT_IND_NO_CONSTRUCTION;\n    }\n' (27:46)> braces_required=True translation=False at 7f402952ab38> -> __content_139913568826456
                __token = 1153
                __token = 1158
                __content_139913568826456 = _lookup_attr(getitem('industry'), 'get_intro_year')(getitem('economy'))
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 1232
                __content_139913568826456_1230 = _lookup_attr(getitem('industry'), 'id')
                __content_139913568826456_1230 = __quote(__content_139913568826456_1230, '\x00', '&#0;', None, False)
                __token = 1266
                __content_139913568826456_1264 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139913568826456_1264 = __quote(__content_139913568826456_1264, '\x00', '&#0;', None, False)
                __token = 1318
                __content_139913568826456_1316 = _lookup_attr(getitem('industry'), 'get_intro_year')(getitem('economy'))
                __content_139913568826456_1316 = __quote(__content_139913568826456_1316, '\x00', '&#0;', None, False)
                __token = 1367
                __content_139913568826456_1365 = _lookup_attr(getitem('industry'), 'get_expiry_year')(getitem('economy'))
                __content_139913568826456_1365 = __quote(__content_139913568826456_1365, '\x00', '&#0;', None, False)
                __token = 1412
                __content_139913568826456_1410 = _lookup_attr(getitem('industry'), 'id')
                __content_139913568826456_1410 = __quote(__content_139913568826456_1410, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    /* ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ' */\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_139913568826456_1230 if (__content_139913568826456_1230 is not None) else ''), '_check_availability_', (__content_139913568826456_1264 if (__content_139913568826456_1264 is not None) else ''), ', current_date) {\n        date(', (__content_139913568826456_1316 if (__content_139913568826456_1316 is not None) else ''), ',1,1) .. date(', (__content_139913568826456_1365 if (__content_139913568826456_1365 is not None) else ''), ',12,31): ', (__content_139913568826456_1410 if (__content_139913568826456_1410 is not None) else ''), '_available_game_mode;\n        return CB_RESULT_IND_NO_CONSTRUCTION;\n    }\n', ))
                if (__content_139913568826456 is None):
                    pass
                else:
                    if (__content_139913568826456 is False):
                        __content_139913568826456 = None
                    else:
                        __tt = type(__content_139913568826456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139913568826456 = str(__content_139913568826456)
                        else:
                            if (__tt is bytes):
                                __content_139913568826456 = decode(__content_139913568826456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139913568826456 = __content_139913568826456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139913568826456)
                                        __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                    else:
                                        __content_139913568826456 = __content_139913568826456()
                if (__content_139913568826456 is not None):
                    __append(__content_139913568826456)
                ____index_139913547917632 -= 1
                if (____index_139913547917632 > 0):
                    __append('')
            if (__backup_economy_139913547928464 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139913547928464

            # <Interpolation value=<Substitution '\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_availability, economy) {\n    ' (33:20)> braces_required=True translation=False at 7f402952ad30> -> __content_139913568826456
            __token = 1520
            __token = 1553
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s' % ('\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_check_availability, economy) {\n    ', ))
            if (__content_139913568826456 is None):
                pass
            else:
                if (__content_139913568826456 is False):
                    __content_139913568826456 = None
                else:
                    __tt = type(__content_139913568826456)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139913568826456 = str(__content_139913568826456)
                    else:
                        if (__tt is bytes):
                            __content_139913568826456 = decode(__content_139913568826456)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139913568826456 = __content_139913568826456.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139913568826456)
                                    __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                else:
                                    __content_139913568826456 = __content_139913568826456()
            if (__content_139913568826456 is not None):
                __append(__content_139913568826456)
            __backup_economy_139913549458064 = get('economy', __marker)

            # <Value 'economies' (36:42)> -> __iterator
            __token = 1639
            __iterator = getitem('economies')
            (__iterator, ____index_139913547915952, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n        ${economy.numeric_id}: ${industry.id}_check_availability_${economy.numeric_id};\n    ' (36:53)> braces_required=True translation=False at 7f402952ada0> -> __content_139913568826456
                __token = 1659
                __token = 1661
                __content_139913568826456 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
                __token = 1684
                __content_139913568826456_1682 = _lookup_attr(getitem('industry'), 'id')
                __content_139913568826456_1682 = __quote(__content_139913568826456_1682, '\x00', '&#0;', None, False)
                __token = 1718
                __content_139913568826456_1716 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139913568826456_1716 = __quote(__content_139913568826456_1716, '\x00', '&#0;', None, False)
                __content_139913568826456 = ('%s%s%s%s%s%s%s' % ('\n        ', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), ': ', (__content_139913568826456_1682 if (__content_139913568826456_1682 is not None) else ''), '_check_availability_', (__content_139913568826456_1716 if (__content_139913568826456_1716 is not None) else ''), ';\n    ', ))
                if (__content_139913568826456 is None):
                    pass
                else:
                    if (__content_139913568826456 is False):
                        __content_139913568826456 = None
                    else:
                        __tt = type(__content_139913568826456)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139913568826456 = str(__content_139913568826456)
                        else:
                            if (__tt is bytes):
                                __content_139913568826456 = decode(__content_139913568826456)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139913568826456 = __content_139913568826456.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139913568826456)
                                        __content_139913568826456 = (str(__content_139913568826456) if (__content_139913568826456 is __converted) else __converted)
                                    else:
                                        __content_139913568826456 = __content_139913568826456()
                if (__content_139913568826456 is not None):
                    __append(__content_139913568826456)
                ____index_139913547915952 -= 1
                if (____index_139913547915952 > 0):
                    __append('')
            if (__backup_economy_139913549458064 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139913549458064
            __append('\n}\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }