# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/XIS/src/templates/closure_secondary.pynml'
__tokens = {106: ('industry.perm_storage', 3, 32), 330: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_increase_closure_counter,\n           STORE_PERM((1 + LOAD_PERM(${perm_storage.closure_counter})), ${perm_storage.closure_counter})) {\n        return 0;\n    }\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_reset_closure_counter, [STORE_PERM(0, ${perm_storage.closure_counter}), 1]) {\n        return 0;\n    }', 7, 4), 362: ('industry.id', 7, 36), 450: ('perm_storage.closure_counter', 8, 39), 485: ('perm_storage.closure_counter', 8, 74), 579: ('industry.id', 11, 36), 642: ('perm_storage.closure_counter', 11, 99), 837: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_secondary_production_level, [\n                transported_last_month_1 > 0 ||\n                transported_last_month_2 > 0 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_1}))', 15, 4), 869: ('industry.id', 15, 36), 1058: ('perm_storage.date_received_1', 18, 44), 1092: ('30 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_2}))', 18, 78), 1142: ('perm_storage.date_received_2', 19, 44), 1176: ('30 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_3}))', 19, 78), 1226: ('perm_storage.date_received_3', 20, 44), 1260: ('30\n                ]\n            ) {\n        0: ${industry.id}_secondary_increase_closure_counter;\n        ${industry.id}_secondary_reset_closure_counter;\n    }', 20, 78), 1310: ('industry.id', 23, 13), 1369: ('industry.id', 24, 10), 1623: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_close_random, (extra_callback_info2 & 32)) {\n\t0: return CB_RESULT_IND_PROD_CLOSE;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}', 32, 0), 1655: ('industry.id', 32, 32), 1859: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_had_produced_check, LOAD_PERM(${industry.perm_storage.closure_counter})) {\n\t0..60: return CB_RESULT_IND_PROD_NO_CHANGE;\n\t${industry.id}_secondary_close_random;\n}', 38, 0), 1891: ('industry.id', 38, 32), 1946: ('industry.perm_storage.closure_counter', 38, 87), 2037: ('industry.id', 40, 3), 2158: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_secondary_closure, allow_close_secondary) {\n\t1..255: ${industry.id}_secondary_had_produced_check;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}', 44, 0), 2190: ('industry.id', 44, 32), 2264: ('industry.id', 45, 11)}

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
            __backup_perm_storage_139875068693976 = get('perm_storage', __marker)

            # <Value 'industry.perm_storage' (3:32)> -> __value
            __token = 106
            __value = _lookup_attr(getitem('industry'), 'perm_storage')
            econtext['perm_storage'] = __value
            __append('\n    ')
            __append('\n\n    ')

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_increase_closure_counter,\n           STORE_PERM((1 + LOAD_PERM(${perm_storage.closure_counter})), ${perm_storage.closure_counter})) {\n        return 0;\n    }\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_reset_closure_counter, [STORE_PERM(0, ${perm_storage.closure_counter}), 1]) {\n        return 0;\n    }\n    ' (6:111)> braces_required=True translation=False at 7f3733e24f28> -> __content_139875089167952
            __token = 330
            __token = 362
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __token = 450
            __content_139875089167952_448 = _lookup_attr(getitem('perm_storage'), 'closure_counter')
            __content_139875089167952_448 = __quote(__content_139875089167952_448, '\x00', '&#0;', None, False)
            __token = 485
            __content_139875089167952_483 = _lookup_attr(getitem('perm_storage'), 'closure_counter')
            __content_139875089167952_483 = __quote(__content_139875089167952_483, '\x00', '&#0;', None, False)
            __token = 579
            __content_139875089167952_577 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952_577 = __quote(__content_139875089167952_577, '\x00', '&#0;', None, False)
            __token = 642
            __content_139875089167952_640 = _lookup_attr(getitem('perm_storage'), 'closure_counter')
            __content_139875089167952_640 = __quote(__content_139875089167952_640, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_secondary_increase_closure_counter,\n           STORE_PERM((1 + LOAD_PERM(', (__content_139875089167952_448 if (__content_139875089167952_448 is not None) else ''), ')), ', (__content_139875089167952_483 if (__content_139875089167952_483 is not None) else ''), ')) {\n        return 0;\n    }\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952_577 if (__content_139875089167952_577 is not None) else ''), '_secondary_reset_closure_counter, [STORE_PERM(0, ', (__content_139875089167952_640 if (__content_139875089167952_640 is not None) else ''), '), 1]) {\n        return 0;\n    }\n    ', ))
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

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_secondary_production_level, [\n                transported_last_month_1 > 0 ||\n                transported_last_month_2 > 0 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_1})) ' (14:128)> braces_required=True translation=False at 7f3733e240f0> -> __content_139875089167952
            __token = 837
            __token = 869
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __token = 1058
            __content_139875089167952_1056 = _lookup_attr(getitem('perm_storage'), 'date_received_1')
            __content_139875089167952_1056 = __quote(__content_139875089167952_1056, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_check_secondary_production_level, [\n                transported_last_month_1 > 0 ||\n                transported_last_month_2 > 0 ||\n                (current_date - LOAD_PERM(', (__content_139875089167952_1056 if (__content_139875089167952_1056 is not None) else ''), ')) ', ))
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
            __append('<')

            # <Interpolation value=<Substitution ' 30 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_2})) ' (18:77)> braces_required=True translation=False at 7f3733e24ac8> -> __content_139875089167952
            __token = 1092
            __token = 1142
            __content_139875089167952 = _lookup_attr(getitem('perm_storage'), 'date_received_2')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s' % (' 30 ||\n                (current_date - LOAD_PERM(', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), ')) ', ))
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
            __append('<')

            # <Interpolation value=<Substitution ' 30 ||\n                (current_date - LOAD_PERM(${perm_storage.date_received_3})) ' (19:77)> braces_required=True translation=False at 7f3733e24470> -> __content_139875089167952
            __token = 1176
            __token = 1226
            __content_139875089167952 = _lookup_attr(getitem('perm_storage'), 'date_received_3')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s' % (' 30 ||\n                (current_date - LOAD_PERM(', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), ')) ', ))
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
            __append('<')

            # <Interpolation value=<Substitution ' 30\n                ]\n            ) {\n        0: ${industry.id}_secondary_increase_closure_counter;\n        ${industry.id}_secondary_reset_closure_counter;\n    }\n' (20:77)> braces_required=True translation=False at 7f3733e24438> -> __content_139875089167952
            __token = 1260
            __token = 1310
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __token = 1369
            __content_139875089167952_1367 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952_1367 = __quote(__content_139875089167952_1367, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s%s%s' % (' 30\n                ]\n            ) {\n        0: ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_secondary_increase_closure_counter;\n        ', (__content_139875089167952_1367 if (__content_139875089167952_1367 is not None) else ''), '_secondary_reset_closure_counter;\n    }\n', ))
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
            if (__backup_perm_storage_139875068693976 is __marker):
                del econtext['perm_storage']
            else:
                econtext['perm_storage'] = __backup_perm_storage_139875068693976
            __append('\n\n\n')
            __append('\n\n')

            # <Interpolation value=<Substitution '\nswitch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_close_random, (extra_callback_info2 & 32)) {\n\t0: return CB_RESULT_IND_PROD_CLOSE;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}\n\n' (31:96)> braces_required=True translation=False at 7f3733dd91d0> -> __content_139875089167952
            __token = 1623
            __token = 1655
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s' % ('\nswitch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_secondary_close_random, (extra_callback_info2 & 32)) {\n\t0: return CB_RESULT_IND_PROD_CLOSE;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}\n\n', ))
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

            # <Interpolation value=<Substitution '\nswitch(FEAT_INDUSTRIES, SELF, ${industry.id}_secondary_had_produced_check, LOAD_PERM(${industry.perm_storage.closure_counter})) {\n\t0..60: return CB_RESULT_IND_PROD_NO_CHANGE;\n\t${industry.id}_secondary_close_random;\n}\n\n' (37:57)> braces_required=True translation=False at 7f3733e24358> -> __content_139875089167952
            __token = 1859
            __token = 1891
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __token = 1946
            __content_139875089167952_1944 = _lookup_attr(_lookup_attr(getitem('industry'), 'perm_storage'), 'closure_counter')
            __content_139875089167952_1944 = __quote(__content_139875089167952_1944, '\x00', '&#0;', None, False)
            __token = 2037
            __content_139875089167952_2035 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952_2035 = __quote(__content_139875089167952_2035, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s%s%s%s%s' % ('\nswitch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_secondary_had_produced_check, LOAD_PERM(', (__content_139875089167952_1944 if (__content_139875089167952_1944 is not None) else ''), ')) {\n\t0..60: return CB_RESULT_IND_PROD_NO_CHANGE;\n\t', (__content_139875089167952_2035 if (__content_139875089167952_2035 is not None) else ''), '_secondary_close_random;\n}\n\n', ))
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

            # <Interpolation value=<Substitution '\nswitch(FEAT_INDUSTRIES, SELF, ${industry.id}_check_secondary_closure, allow_close_secondary) {\n\t1..255: ${industry.id}_secondary_had_produced_check;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}\n\n\n' (43:80)> braces_required=True translation=False at 7f3733e24390> -> __content_139875089167952
            __token = 2158
            __token = 2190
            __content_139875089167952 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952 = __quote(__content_139875089167952, '\x00', '&#0;', None, False)
            __token = 2264
            __content_139875089167952_2262 = _lookup_attr(getitem('industry'), 'id')
            __content_139875089167952_2262 = __quote(__content_139875089167952_2262, '\x00', '&#0;', None, False)
            __content_139875089167952 = ('%s%s%s%s%s' % ('\nswitch(FEAT_INDUSTRIES, SELF, ', (__content_139875089167952 if (__content_139875089167952 is not None) else ''), '_check_secondary_closure, allow_close_secondary) {\n\t1..255: ', (__content_139875089167952_2262 if (__content_139875089167952_2262 is not None) else ''), '_secondary_had_produced_check;\n\treturn CB_RESULT_IND_PROD_NO_CHANGE;\n}\n\n\n', ))
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
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }