# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/produce_primary.pynml'
__tokens = {87: ('industry.perm_storage', 3, 32), 115: ('produce(${industry.id}_production, 9999, 9999, 9999, 0, 0, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce, STORE_PERM(waiting_cargo_1 + waiting_cargo_2 + waiting_cargo_3 + LOAD_PERM(${perm_storage.var_num_supplies_delivered}), ${perm_storage.var_num_supplies_delivered})) {\n        ${industry.id}_production;\n    }\n\n    produce(${industry.id}_production_256, 0, 0, 0, LOAD_TEMP(9) * production_rate_1 / 100, LOAD_TEMP(9) * production_rate_2 / 100, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce_256_ticks,\n            [STORE_TEMP(\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered}) +\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered_last}) +\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered_bef_last}),\n            8),\n            STORE_TEMP((LOAD_TEMP(8) >= (${industry.supply_requirements[2]} * primary_level2_requirement)) ? primary_level2_bonus :\n                       (LOAD_TEMP(8) >= (${industry.supply_requirements[2]} * primary_level1_requirement)) ? primary_level1_bonus : 0, 9),\n            STORE_PERM(LOAD_TEMP(9), ${perm_storage.var_current_supplies_prod_factor})\n            ]) {\n        ${industry.id}_production_256;\n    }', 4, 4), 125: ('industry.id', 4, 14), 215: ('industry.id', 6, 36), 314: ('perm_storage.var_num_supplies_delivered', 6, 135), 359: ('perm_storage.var_num_supplies_delivered', 6, 180), 414: ('industry.id', 7, 10), 460: ('industry.id', 10, 14), 619: ('industry.id', 12, 36), 704: ('perm_storage.var_num_supplies_delivered', 14, 28), 776: ('perm_storage.var_num_supplies_delivered_last', 15, 28), 853: ('perm_storage.var_num_supplies_delivered_bef_last', 16, 28), 964: ('industry.supply_requirements[2]', 18, 43), 1096: ('industry.supply_requirements[2]', 19, 43), 1231: ('perm_storage.var_current_supplies_prod_factor', 20, 39), 1306: ('industry.id', 22, 10)}

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
            __append('/* Primary production which is boosted by supplies */\n\n')
            __backup_perm_storage_139913548642960 = get('perm_storage', __marker)

            # <Value 'industry.perm_storage' (3:32)> -> __value
            __token = 87
            __value = _lookup_attr(getitem('industry'), 'perm_storage')
            econtext['perm_storage'] = __value

            # <Interpolation value=<Substitution '\n    produce(${industry.id}_production, 9999, 9999, 9999, 0, 0, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce, STORE_PERM(waiting_cargo_1 + waiting_cargo_2 + waiting_cargo_3 + LOAD_PERM(${perm_storage.var_num_supplies_delivered}), ${perm_storage.var_num_supplies_delivered})) {\n        ${industry.id}_production;\n    }\n\n    produce(${industry.id}_production_256, 0, 0, 0, LOAD_TEMP(9) * production_rate_1 / 100, LOAD_TEMP(9) * production_rate_2 / 100, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_produce_256_ticks,\n            [STORE_TEMP(\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered}) +\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered_last}) +\n                LOAD_PERM(${perm_storage.var_num_supplies_delivered_bef_last}),\n            8),\n            STORE_TEMP((LOAD_TEMP(8) >= (${industry.supply_requirements[2]} * primary_level2_requirement)) ? primary_level2_bonus :\n                       (LOAD_TEMP(8) >= (${industry.supply_requirements[2]} * primary_level1_requirement)) ? primary_level1_bonus : 0, 9),\n            STORE_PERM(LOAD_TEMP(9), ${perm_storage.var_current_supplies_prod_factor})\n            ]) {\n        ${industry.id}_production_256;\n    }\n' (3:55)> braces_required=True translation=False at 7f402967d6a0> -> __content_139913568826456
            __token = 115
            __token = 125
            __content_139913568826456 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456 = __quote(__content_139913568826456, '\x00', '&#0;', None, False)
            __token = 215
            __content_139913568826456_213 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_213 = __quote(__content_139913568826456_213, '\x00', '&#0;', None, False)
            __token = 314
            __content_139913568826456_312 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered')
            __content_139913568826456_312 = __quote(__content_139913568826456_312, '\x00', '&#0;', None, False)
            __token = 359
            __content_139913568826456_357 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered')
            __content_139913568826456_357 = __quote(__content_139913568826456_357, '\x00', '&#0;', None, False)
            __token = 414
            __content_139913568826456_412 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_412 = __quote(__content_139913568826456_412, '\x00', '&#0;', None, False)
            __token = 460
            __content_139913568826456_458 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_458 = __quote(__content_139913568826456_458, '\x00', '&#0;', None, False)
            __token = 619
            __content_139913568826456_617 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_617 = __quote(__content_139913568826456_617, '\x00', '&#0;', None, False)
            __token = 704
            __content_139913568826456_702 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered')
            __content_139913568826456_702 = __quote(__content_139913568826456_702, '\x00', '&#0;', None, False)
            __token = 776
            __content_139913568826456_774 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered_last')
            __content_139913568826456_774 = __quote(__content_139913568826456_774, '\x00', '&#0;', None, False)
            __token = 853
            __content_139913568826456_851 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered_bef_last')
            __content_139913568826456_851 = __quote(__content_139913568826456_851, '\x00', '&#0;', None, False)
            __token = 964
            __content_139913568826456_962 = _lookup_attr(getitem('industry'), 'supply_requirements')[2]
            __content_139913568826456_962 = __quote(__content_139913568826456_962, '\x00', '&#0;', None, False)
            __token = 1096
            __content_139913568826456_1094 = _lookup_attr(getitem('industry'), 'supply_requirements')[2]
            __content_139913568826456_1094 = __quote(__content_139913568826456_1094, '\x00', '&#0;', None, False)
            __token = 1231
            __content_139913568826456_1229 = _lookup_attr(getitem('perm_storage'), 'var_current_supplies_prod_factor')
            __content_139913568826456_1229 = __quote(__content_139913568826456_1229, '\x00', '&#0;', None, False)
            __token = 1306
            __content_139913568826456_1304 = _lookup_attr(getitem('industry'), 'id')
            __content_139913568826456_1304 = __quote(__content_139913568826456_1304, '\x00', '&#0;', None, False)
            __content_139913568826456 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    produce(', (__content_139913568826456 if (__content_139913568826456 is not None) else ''), '_production, 9999, 9999, 9999, 0, 0, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_139913568826456_213 if (__content_139913568826456_213 is not None) else ''), '_produce, STORE_PERM(waiting_cargo_1 + waiting_cargo_2 + waiting_cargo_3 + LOAD_PERM(', (__content_139913568826456_312 if (__content_139913568826456_312 is not None) else ''), '), ', (__content_139913568826456_357 if (__content_139913568826456_357 is not None) else ''), ')) {\n        ', (__content_139913568826456_412 if (__content_139913568826456_412 is not None) else ''), '_production;\n    }\n\n    produce(', (__content_139913568826456_458 if (__content_139913568826456_458 is not None) else ''), '_production_256, 0, 0, 0, LOAD_TEMP(9) * production_rate_1 / 100, LOAD_TEMP(9) * production_rate_2 / 100, 0);\n\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_139913568826456_617 if (__content_139913568826456_617 is not None) else ''), '_produce_256_ticks,\n            [STORE_TEMP(\n                LOAD_PERM(', (__content_139913568826456_702 if (__content_139913568826456_702 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139913568826456_774 if (__content_139913568826456_774 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139913568826456_851 if (__content_139913568826456_851 is not None) else ''), '),\n            8),\n            STORE_TEMP((LOAD_TEMP(8) >= (', (__content_139913568826456_962 if (__content_139913568826456_962 is not None) else ''), ' * primary_level2_requirement)) ? primary_level2_bonus :\n                       (LOAD_TEMP(8) >= (', (__content_139913568826456_1094 if (__content_139913568826456_1094 is not None) else ''), ' * primary_level1_requirement)) ? primary_level1_bonus : 0, 9),\n            STORE_PERM(LOAD_TEMP(9), ', (__content_139913568826456_1229 if (__content_139913568826456_1229 is not None) else ''), ')\n            ]) {\n        ', (__content_139913568826456_1304 if (__content_139913568826456_1304 is not None) else ''), '_production_256;\n    }\n', ))
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
            if (__backup_perm_storage_139913548642960 is __marker):
                del econtext['perm_storage']
            else:
                econtext['perm_storage'] = __backup_perm_storage_139913548642960
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }