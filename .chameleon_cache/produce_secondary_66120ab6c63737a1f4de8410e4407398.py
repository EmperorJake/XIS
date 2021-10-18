# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/produce_secondary.pynml'

__tokens = {457: ('0', 10, 41), 500: (' ', 11, 40), 543: ('3', 12, 39), 586: ('o', 13, 38), 626: ('o', 14, 34), 666: ('i', 15, 33), 712: ('x', 16, 38), 757: ('a', 17, 36), 791: ('storage industry.perm', 18, 24), 986: ('produce (${industry.id}_simple_produce,\n                waiting_cargo_1,\n                waiting_cargo_2,\n                waiting_cargo_3,\n                LOAD_PERM(${perm_storage.leftover_cargo_1}) * LOAD_PERM(${perm_storage.ratio_input_1}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_2}) * LOAD_PERM(${perm_storage.ratio_input_2}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_3}) * LOAD_PERM(${perm_storage.ratio_input_3}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}),\n\n                LOAD_PERM(${perm_storage.leftover_cargo_1}) * LOAD_PERM(${perm_storage.ratio_input_1}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_2}) * LOAD_PERM(${perm_storage.ratio_input_2}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_3}) * LOAD_PERM(${perm_storage.ratio_input_3}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}),\n                [', 20, 4), 997: ('industry.id', 20, 15), 1153: ('perm_storage.leftover_cargo_1', 24, 28), 1199: ('perm_storage.ratio_input_1', 24, 74), 1242: ('var_output_ratio_1', 24, 117), 1268: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 24, 143), 1351: ('perm_storage.leftover_cargo_2', 25, 28), 1397: ('perm_storage.ratio_input_2', 25, 74), 1440: ('var_output_ratio_1', 25, 117), 1466: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 25, 143), 1549: ('perm_storage.leftover_cargo_3', 26, 28), 1595: ('perm_storage.ratio_input_3', 26, 74), 1638: ('var_output_ratio_1', 26, 117), 1664: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 26, 143), 1747: ('perm_storage.leftover_cargo_1', 28, 28), 1793: ('perm_storage.ratio_input_1', 28, 74), 1836: ('var_output_ratio_2', 28, 117), 1862: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 28, 143), 1945: ('perm_storage.leftover_cargo_2', 29, 28), 1991: ('perm_storage.ratio_input_2', 29, 74), 2034: ('var_output_ratio_2', 29, 117), 2060: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 29, 143), 2143: ('perm_storage.leftover_cargo_3', 30, 28), 2189: ('perm_storage.ratio_input_3', 30, 74), 2232: ('var_output_ratio_2', 30, 117), 2258: ('var_input_ratio_max_sum * var_output_ratio_max_sum', 30, 143), 2505: ('STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_1}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_1}),\n                STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_2}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_2}),\n                STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_3}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_3}),\n                0\n                ]\n    );', 33, 16), 2528: ('perm_storage.leftover_cargo_1', 33, 39), 2565: ('var_input_ratio_max_sum', 33, 76), 2604: ('var_num_output_cargos', 33, 115), 2632: ('perm_storage.leftover_cargo_1', 33, 143), 2704: ('perm_storage.leftover_cargo_2', 34, 39), 2741: ('var_input_ratio_max_sum', 34, 76), 2780: ('var_num_output_cargos', 34, 115), 2808: ('perm_storage.leftover_cargo_2', 34, 143), 2880: ('perm_storage.leftover_cargo_3', 35, 39), 2917: ('var_input_ratio_max_sum', 35, 76), 2956: ('var_num_output_cargos', 35, 115), 2984: ('perm_storage.leftover_cargo_3', 35, 143), 3096: ('economies', 40, 35), 3116: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_produce_economy_${economy.numeric_id},\n                [', 41, 8), 3149: ('industry.id', 41, 41), 3180: ('economy.numeric_id', 41, 72), 3291: ('STORE_TEMP(${len(industry.get_prod_cargo_types(economy))}, ${var_num_output_cargos}),', 44, 16), 3304: ('len(industry.get_prod_cargo_types(economy))', 44, 29), 3352: ('var_num_output_cargos', 44, 77), 3535: ('STORE_TEMP(${industry.get_output_ratio(1, economy)}, ${var_output_ratio_1}),\n                STORE_TEMP(${industry.get_output_ratio(2, economy)}, ${var_output_ratio_2}),', 46, 16), 3548: ('industry.get_output_ratio(1, economy)', 46, 29), 3590: ('var_output_ratio_1', 46, 71), 3641: ('industry.get_output_ratio(2, economy)', 47, 29), 3683: ('var_output_ratio_2', 47, 71), 3806: ('STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_1}),(waiting_cargo_1 > 0) * current_date), ${perm_storage.date_received_1}),\n                STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_2}),(waiting_cargo_2 > 0) * current_date), ${perm_storage.date_received_2}),\n                STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_3}),(waiting_cargo_3 > 0) * current_date), ${perm_storage.date_received_3}),', 49, 16), 3834: ('perm_storage.date_received_1', 49, 44), 3906: ('perm_storage.date_received_1', 49, 116), 3982: ('perm_storage.date_received_2', 50, 44), 4054: ('perm_storage.date_received_2', 50, 116), 4130: ('perm_storage.date_received_3', 51, 44), 4202: ('perm_storage.date_received_3', 51, 116), 4304: ('STORE_PERM( (waiting_cargo_1 == 0 && waiting_cargo_2 == 0 && waiting_cargo_3 == 0) * LOAD_PERM(${perm_storage.closure_counter}), ${perm_storage.closure_counter}),', 53, 16), 4401: ('perm_storage.closure_counter', 53, 113), 4435: ('perm_storage.closure_counter', 53, 147), 4612: ('STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_1}))', 56, 16), 4652: ('perm_storage.date_received_1', 56, 56), 4685: ('= ${global_constants.secondary_production_span}, ${var_received_timely_1}),\n                STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_2}))', 56, 89), 4689: ('global_constants.secondary_production_span', 56, 93), 4736: ('var_received_timely_1', 56, 140), 4817: ('perm_storage.date_received_2', 57, 56), 4850: ('= ${global_constants.secondary_production_span}, ${var_received_timely_2}),\n                STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_3}))', 57, 89), 4854: ('global_constants.secondary_production_span', 57, 93), 4901: ('var_received_timely_2', 57, 140), 4982: ('perm_storage.date_received_3', 58, 56), 5015: ('= ${global_constants.secondary_production_span}, ${var_received_timely_3}),', 58, 89), 5019: ('global_constants.secondary_production_span', 58, 93), 5066: ('var_received_timely_3', 58, 140), 5196: ('STORE_PERM( ${industry.get_prod_ratio(1,economy)} +\n                            LOAD_TEMP(${var_received_timely_2}) * ${industry.get_boost(2,1,economy)} +\n                            LOAD_TEMP(${var_received_timely_3}) * ${industry.get_boost(3,1,economy)},\n                    ${perm_storage.ratio_input_1}\n                ),\n                STORE_PERM( ${industry.get_prod_ratio(2,economy)} +\n                            LOAD_TEMP(${var_received_timely_1}) * ${industry.get_boost(1,2,economy)} +\n                            LOAD_TEMP(${var_received_timely_3}) * ${industry.get_boost(3,2,economy)},\n                    ${perm_storage.ratio_input_2}\n                ),\n                STORE_PERM( ${industry.get_prod_ratio(3,economy)} +\n                            LOAD_TEMP(${var_received_timely_1}) * ${industry.get_boost(1,3,economy)} +\n                            LOAD_TEMP(${var_received_timely_2}) * ${industry.get_boost(2,3,economy)},\n                    ${perm_storage.ratio_input_3}\n                ),', 61, 16), 5210: ('industry.get_prod_ratio(1,economy)', 61, 30), 5288: ('var_received_timely_2', 62, 40), 5316: ('industry.get_boost(2,1,economy)', 62, 68), 5391: ('var_received_timely_3', 63, 40), 5419: ('industry.get_boost(3,1,economy)', 63, 68), 5475: ('perm_storage.ratio_input_1', 64, 22), 5552: ('industry.get_prod_ratio(2,economy)', 66, 30), 5630: ('var_received_timely_1', 67, 40), 5658: ('industry.get_boost(1,2,economy)', 67, 68), 5733: ('var_received_timely_3', 68, 40), 5761: ('industry.get_boost(3,2,economy)', 68, 68), 5817: ('perm_storage.ratio_input_2', 69, 22), 5894: ('industry.get_prod_ratio(3,economy)', 71, 30), 5972: ('var_received_timely_1', 72, 40), 6000: ('industry.get_boost(1,3,economy)', 72, 68), 6075: ('var_received_timely_2', 73, 40), 6103: ('industry.get_boost(2,3,economy)', 73, 68), 6159: ('perm_storage.ratio_input_3', 74, 22), 6298: ('STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_1}) + waiting_cargo_1, ${perm_storage.leftover_cargo_1}),\n                STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_2}) + waiting_cargo_2, ${perm_storage.leftover_cargo_2}),\n                STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_3}) + waiting_cargo_3, ${perm_storage.leftover_cargo_3}),\n\n                1\n                ]) {\n            ${industry.id}_simple_produce;\n        }', 78, 16), 6322: ('perm_storage.leftover_cargo_1', 78, 40), 6375: ('perm_storage.leftover_cargo_1', 78, 93), 6448: ('perm_storage.leftover_cargo_2', 79, 40), 6501: ('perm_storage.leftover_cargo_2', 79, 93), 6574: ('perm_storage.leftover_cargo_3', 80, 40), 6627: ('perm_storage.leftover_cargo_3', 80, 93), 6714: ('industry.id', 84, 14), 6779: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_produce, economy) {', 88, 4), 6812: ('industry.id', 88, 37), 6884: ('economies', 89, 39), 6908: ('${economy.numeric_id}: ${industry.id}_produce_economy_${economy.numeric_id};', 90, 12), 6910: ('economy.numeric_id', 90, 14), 6933: ('industry.id', 90, 37), 6964: ('economy.numeric_id', 90, 68)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

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
            __append('\n\n\n')

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425916672
            __attrs_139738425916672 = _static_139738431409216
            __backup_var_received_timely_1_139738426974272 = get('var_received_timely_1', __marker)

            # <Value '0' (10:41)> -> __value
            __token = 457
            __value = 0
            econtext['var_received_timely_1'] = __value
            __backup_var_received_timely_2_139738426612368 = get('var_received_timely_2', __marker)

            # <Value '1' (11:40)> -> __value
            __token = 500
            __value = 1
            econtext['var_received_timely_2'] = __value
            __backup_var_received_timely_3_139738426344784 = get('var_received_timely_3', __marker)

            # <Value '2' (12:39)> -> __value
            __token = 543
            __value = 2
            econtext['var_received_timely_3'] = __value
            __backup_var_num_output_cargos_139738425152512 = get('var_num_output_cargos', __marker)

            # <Value '3' (13:38)> -> __value
            __token = 586
            __value = 3
            econtext['var_num_output_cargos'] = __value
            __backup_var_output_ratio_1_139738426002256 = get('var_output_ratio_1', __marker)

            # <Value '4' (14:34)> -> __value
            __token = 626
            __value = 4
            econtext['var_output_ratio_1'] = __value
            __backup_var_output_ratio_2_139738426001776 = get('var_output_ratio_2', __marker)

            # <Value '5' (15:33)> -> __value
            __token = 666
            __value = 5
            econtext['var_output_ratio_2'] = __value
            __backup_var_output_ratio_max_sum_139738427835968 = get('var_output_ratio_max_sum', __marker)

            # <Value '8' (16:38)> -> __value
            __token = 712
            __value = 8
            econtext['var_output_ratio_max_sum'] = __value
            __backup_var_input_ratio_max_sum_139738426002928 = get('var_input_ratio_max_sum', __marker)

            # <Value '8' (17:36)> -> __value
            __token = 757
            __value = 8
            econtext['var_input_ratio_max_sum'] = __value
            __backup_perm_storage_139738426002592 = get('perm_storage', __marker)

            # <Value 'industry.perm_storage' (18:24)> -> __value
            __token = 791
            __value = _lookup_attr(getitem('industry'), 'perm_storage')
            econtext['perm_storage'] = __value
            __append('\n')

            # <Interpolation value=<Substitution '\n    produce (${industry.id}_simple_produce,\n                waiting_cargo_1,\n                waiting_cargo_2,\n                waiting_cargo_3,\n                LOAD_PERM(${perm_storage.leftover_cargo_1}) * LOAD_PERM(${perm_storage.ratio_input_1}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_2}) * LOAD_PERM(${perm_storage.ratio_input_2}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_3}) * LOAD_PERM(${perm_storage.ratio_input_3}) * LOAD_TEMP(${var_output_ratio_1}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}),\n\n                LOAD_PERM(${perm_storage.leftover_cargo_1}) * LOAD_PERM(${perm_storage.ratio_input_1}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_2}) * LOAD_PERM(${perm_storage.ratio_input_2}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}) +\n                LOAD_PERM(${perm_storage.leftover_cargo_3}) * LOAD_PERM(${perm_storage.ratio_input_3}) * LOAD_TEMP(${var_output_ratio_2}) / (${var_input_ratio_max_sum * var_output_ratio_max_sum}),\n                [\n                ' (19:157)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f17633cf790> -> __content_139738435934384
            __token = 986
            __token = 997
            __content_139738435934384 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __token = 1153
            __content_139738435934384_1151 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
            __content_139738435934384_1151 = __quote(__content_139738435934384_1151, '\x00', '&#0;', None, None)
            __token = 1199
            __content_139738435934384_1197 = _lookup_attr(getitem('perm_storage'), 'ratio_input_1')
            __content_139738435934384_1197 = __quote(__content_139738435934384_1197, '\x00', '&#0;', None, None)
            __token = 1242
            __content_139738435934384_1240 = getitem('var_output_ratio_1')
            __content_139738435934384_1240 = __quote(__content_139738435934384_1240, '\x00', '&#0;', None, None)
            __token = 1268
            __content_139738435934384_1266 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_1266 = __quote(__content_139738435934384_1266, '\x00', '&#0;', None, None)
            __token = 1351
            __content_139738435934384_1349 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
            __content_139738435934384_1349 = __quote(__content_139738435934384_1349, '\x00', '&#0;', None, None)
            __token = 1397
            __content_139738435934384_1395 = _lookup_attr(getitem('perm_storage'), 'ratio_input_2')
            __content_139738435934384_1395 = __quote(__content_139738435934384_1395, '\x00', '&#0;', None, None)
            __token = 1440
            __content_139738435934384_1438 = getitem('var_output_ratio_1')
            __content_139738435934384_1438 = __quote(__content_139738435934384_1438, '\x00', '&#0;', None, None)
            __token = 1466
            __content_139738435934384_1464 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_1464 = __quote(__content_139738435934384_1464, '\x00', '&#0;', None, None)
            __token = 1549
            __content_139738435934384_1547 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
            __content_139738435934384_1547 = __quote(__content_139738435934384_1547, '\x00', '&#0;', None, None)
            __token = 1595
            __content_139738435934384_1593 = _lookup_attr(getitem('perm_storage'), 'ratio_input_3')
            __content_139738435934384_1593 = __quote(__content_139738435934384_1593, '\x00', '&#0;', None, None)
            __token = 1638
            __content_139738435934384_1636 = getitem('var_output_ratio_1')
            __content_139738435934384_1636 = __quote(__content_139738435934384_1636, '\x00', '&#0;', None, None)
            __token = 1664
            __content_139738435934384_1662 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_1662 = __quote(__content_139738435934384_1662, '\x00', '&#0;', None, None)
            __token = 1747
            __content_139738435934384_1745 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
            __content_139738435934384_1745 = __quote(__content_139738435934384_1745, '\x00', '&#0;', None, None)
            __token = 1793
            __content_139738435934384_1791 = _lookup_attr(getitem('perm_storage'), 'ratio_input_1')
            __content_139738435934384_1791 = __quote(__content_139738435934384_1791, '\x00', '&#0;', None, None)
            __token = 1836
            __content_139738435934384_1834 = getitem('var_output_ratio_2')
            __content_139738435934384_1834 = __quote(__content_139738435934384_1834, '\x00', '&#0;', None, None)
            __token = 1862
            __content_139738435934384_1860 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_1860 = __quote(__content_139738435934384_1860, '\x00', '&#0;', None, None)
            __token = 1945
            __content_139738435934384_1943 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
            __content_139738435934384_1943 = __quote(__content_139738435934384_1943, '\x00', '&#0;', None, None)
            __token = 1991
            __content_139738435934384_1989 = _lookup_attr(getitem('perm_storage'), 'ratio_input_2')
            __content_139738435934384_1989 = __quote(__content_139738435934384_1989, '\x00', '&#0;', None, None)
            __token = 2034
            __content_139738435934384_2032 = getitem('var_output_ratio_2')
            __content_139738435934384_2032 = __quote(__content_139738435934384_2032, '\x00', '&#0;', None, None)
            __token = 2060
            __content_139738435934384_2058 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_2058 = __quote(__content_139738435934384_2058, '\x00', '&#0;', None, None)
            __token = 2143
            __content_139738435934384_2141 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
            __content_139738435934384_2141 = __quote(__content_139738435934384_2141, '\x00', '&#0;', None, None)
            __token = 2189
            __content_139738435934384_2187 = _lookup_attr(getitem('perm_storage'), 'ratio_input_3')
            __content_139738435934384_2187 = __quote(__content_139738435934384_2187, '\x00', '&#0;', None, None)
            __token = 2232
            __content_139738435934384_2230 = getitem('var_output_ratio_2')
            __content_139738435934384_2230 = __quote(__content_139738435934384_2230, '\x00', '&#0;', None, None)
            __token = 2258
            __content_139738435934384_2256 = (getitem('var_input_ratio_max_sum') * getitem('var_output_ratio_max_sum'))
            __content_139738435934384_2256 = __quote(__content_139738435934384_2256, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    produce (', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), '_simple_produce,\n                waiting_cargo_1,\n                waiting_cargo_2,\n                waiting_cargo_3,\n                LOAD_PERM(', (__content_139738435934384_1151 if (__content_139738435934384_1151 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_1197 if (__content_139738435934384_1197 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_1240 if (__content_139738435934384_1240 is not None) else ''), ') / (', (__content_139738435934384_1266 if (__content_139738435934384_1266 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139738435934384_1349 if (__content_139738435934384_1349 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_1395 if (__content_139738435934384_1395 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_1438 if (__content_139738435934384_1438 is not None) else ''), ') / (', (__content_139738435934384_1464 if (__content_139738435934384_1464 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139738435934384_1547 if (__content_139738435934384_1547 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_1593 if (__content_139738435934384_1593 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_1636 if (__content_139738435934384_1636 is not None) else ''), ') / (', (__content_139738435934384_1662 if (__content_139738435934384_1662 is not None) else ''), '),\n\n                LOAD_PERM(', (__content_139738435934384_1745 if (__content_139738435934384_1745 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_1791 if (__content_139738435934384_1791 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_1834 if (__content_139738435934384_1834 is not None) else ''), ') / (', (__content_139738435934384_1860 if (__content_139738435934384_1860 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139738435934384_1943 if (__content_139738435934384_1943 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_1989 if (__content_139738435934384_1989 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_2032 if (__content_139738435934384_2032 is not None) else ''), ') / (', (__content_139738435934384_2058 if (__content_139738435934384_2058 is not None) else ''), ') +\n                LOAD_PERM(', (__content_139738435934384_2141 if (__content_139738435934384_2141 is not None) else ''), ') * LOAD_PERM(', (__content_139738435934384_2187 if (__content_139738435934384_2187 is not None) else ''), ') * LOAD_TEMP(', (__content_139738435934384_2230 if (__content_139738435934384_2230 is not None) else ''), ') / (', (__content_139738435934384_2256 if (__content_139738435934384_2256 is not None) else ''), '),\n                [\n                ', ))
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

            # <Interpolation value=<Substitution '\n                STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_1}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_1}),\n                STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_2}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_2}),\n                STORE_PERM(LOAD_PERM(${perm_storage.leftover_cargo_3}) % (${var_input_ratio_max_sum} / LOAD_TEMP(${var_num_output_cargos})), ${perm_storage.leftover_cargo_3}),\n                0\n                ]\n    );\n\n    ' (32:158)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f17633cf040> -> __content_139738435934384
            __token = 2505
            __token = 2528
            __content_139738435934384 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __token = 2565
            __content_139738435934384_2563 = getitem('var_input_ratio_max_sum')
            __content_139738435934384_2563 = __quote(__content_139738435934384_2563, '\x00', '&#0;', None, None)
            __token = 2604
            __content_139738435934384_2602 = getitem('var_num_output_cargos')
            __content_139738435934384_2602 = __quote(__content_139738435934384_2602, '\x00', '&#0;', None, None)
            __token = 2632
            __content_139738435934384_2630 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
            __content_139738435934384_2630 = __quote(__content_139738435934384_2630, '\x00', '&#0;', None, None)
            __token = 2704
            __content_139738435934384_2702 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
            __content_139738435934384_2702 = __quote(__content_139738435934384_2702, '\x00', '&#0;', None, None)
            __token = 2741
            __content_139738435934384_2739 = getitem('var_input_ratio_max_sum')
            __content_139738435934384_2739 = __quote(__content_139738435934384_2739, '\x00', '&#0;', None, None)
            __token = 2780
            __content_139738435934384_2778 = getitem('var_num_output_cargos')
            __content_139738435934384_2778 = __quote(__content_139738435934384_2778, '\x00', '&#0;', None, None)
            __token = 2808
            __content_139738435934384_2806 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
            __content_139738435934384_2806 = __quote(__content_139738435934384_2806, '\x00', '&#0;', None, None)
            __token = 2880
            __content_139738435934384_2878 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
            __content_139738435934384_2878 = __quote(__content_139738435934384_2878, '\x00', '&#0;', None, None)
            __token = 2917
            __content_139738435934384_2915 = getitem('var_input_ratio_max_sum')
            __content_139738435934384_2915 = __quote(__content_139738435934384_2915, '\x00', '&#0;', None, None)
            __token = 2956
            __content_139738435934384_2954 = getitem('var_num_output_cargos')
            __content_139738435934384_2954 = __quote(__content_139738435934384_2954, '\x00', '&#0;', None, None)
            __token = 2984
            __content_139738435934384_2982 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
            __content_139738435934384_2982 = __quote(__content_139738435934384_2982, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                STORE_PERM(LOAD_PERM(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') % (', (__content_139738435934384_2563 if (__content_139738435934384_2563 is not None) else ''), ' / LOAD_TEMP(', (__content_139738435934384_2602 if (__content_139738435934384_2602 is not None) else ''), ')), ', (__content_139738435934384_2630 if (__content_139738435934384_2630 is not None) else ''), '),\n                STORE_PERM(LOAD_PERM(', (__content_139738435934384_2702 if (__content_139738435934384_2702 is not None) else ''), ') % (', (__content_139738435934384_2739 if (__content_139738435934384_2739 is not None) else ''), ' / LOAD_TEMP(', (__content_139738435934384_2778 if (__content_139738435934384_2778 is not None) else ''), ')), ', (__content_139738435934384_2806 if (__content_139738435934384_2806 is not None) else ''), '),\n                STORE_PERM(LOAD_PERM(', (__content_139738435934384_2878 if (__content_139738435934384_2878 is not None) else ''), ') % (', (__content_139738435934384_2915 if (__content_139738435934384_2915 is not None) else ''), ' / LOAD_TEMP(', (__content_139738435934384_2954 if (__content_139738435934384_2954 is not None) else ''), ')), ', (__content_139738435934384_2982 if (__content_139738435934384_2982 is not None) else ''), '),\n                0\n                ]\n    );\n\n    ', ))
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

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425913936
            __attrs_139738425913936 = _static_139738431409216
            __backup_economy_139738426997008 = get('economy', __marker)

            # <Value 'economies' (40:35)> -> __iterator
            __token = 3096
            __iterator = getitem('economies')
            (__iterator, ____index_139738425703008, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n        switch (FEAT_INDUSTRIES, SELF, ${industry.id}_produce_economy_${economy.numeric_id},\n                [\n                ' (40:46)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339bdf0> -> __content_139738435934384
                __token = 3116
                __token = 3149
                __content_139738435934384 = _lookup_attr(getitem('industry'), 'id')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 3180
                __content_139738435934384_3178 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139738435934384_3178 = __quote(__content_139738435934384_3178, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s' % ('\n        switch (FEAT_INDUSTRIES, SELF, ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), '_produce_economy_', (__content_139738435934384_3178 if (__content_139738435934384_3178 is not None) else ''), ',\n                [\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_TEMP(${len(industry.get_prod_cargo_types(economy))}, ${var_num_output_cargos}),\n                ' (43:55)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b970> -> __content_139738435934384
                __token = 3291
                __token = 3304
                __content_139738435934384 = len(_lookup_attr(getitem('industry'), 'get_prod_cargo_types')(getitem('economy')))
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 3352
                __content_139738435934384_3350 = getitem('var_num_output_cargos')
                __content_139738435934384_3350 = __quote(__content_139738435934384_3350, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s' % ('\n                STORE_TEMP(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_3350 if (__content_139738435934384_3350 is not None) else ''), '),\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_TEMP(${industry.get_output_ratio(1, economy)}, ${var_output_ratio_1}),\n                STORE_TEMP(${industry.get_output_ratio(2, economy)}, ${var_output_ratio_2}),\n                ' (45:141)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b940> -> __content_139738435934384
                __token = 3535
                __token = 3548
                __content_139738435934384 = _lookup_attr(getitem('industry'), 'get_output_ratio')(1, getitem('economy'))
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 3590
                __content_139738435934384_3588 = getitem('var_output_ratio_1')
                __content_139738435934384_3588 = __quote(__content_139738435934384_3588, '\x00', '&#0;', None, None)
                __token = 3641
                __content_139738435934384_3639 = _lookup_attr(getitem('industry'), 'get_output_ratio')(2, getitem('economy'))
                __content_139738435934384_3639 = __quote(__content_139738435934384_3639, '\x00', '&#0;', None, None)
                __token = 3683
                __content_139738435934384_3681 = getitem('var_output_ratio_2')
                __content_139738435934384_3681 = __quote(__content_139738435934384_3681, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s' % ('\n                STORE_TEMP(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_3588 if (__content_139738435934384_3588 is not None) else ''), '),\n                STORE_TEMP(', (__content_139738435934384_3639 if (__content_139738435934384_3639 is not None) else ''), ', ', (__content_139738435934384_3681 if (__content_139738435934384_3681 is not None) else ''), '),\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_1}),(waiting_cargo_1 > 0) * current_date), ${perm_storage.date_received_1}),\n                STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_2}),(waiting_cargo_2 > 0) * current_date), ${perm_storage.date_received_2}),\n                STORE_PERM( max(LOAD_PERM(${perm_storage.date_received_3}),(waiting_cargo_3 > 0) * current_date), ${perm_storage.date_received_3}),\n                ' (48:84)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339bca0> -> __content_139738435934384
                __token = 3806
                __token = 3834
                __content_139738435934384 = _lookup_attr(getitem('perm_storage'), 'date_received_1')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 3906
                __content_139738435934384_3904 = _lookup_attr(getitem('perm_storage'), 'date_received_1')
                __content_139738435934384_3904 = __quote(__content_139738435934384_3904, '\x00', '&#0;', None, None)
                __token = 3982
                __content_139738435934384_3980 = _lookup_attr(getitem('perm_storage'), 'date_received_2')
                __content_139738435934384_3980 = __quote(__content_139738435934384_3980, '\x00', '&#0;', None, None)
                __token = 4054
                __content_139738435934384_4052 = _lookup_attr(getitem('perm_storage'), 'date_received_2')
                __content_139738435934384_4052 = __quote(__content_139738435934384_4052, '\x00', '&#0;', None, None)
                __token = 4130
                __content_139738435934384_4128 = _lookup_attr(getitem('perm_storage'), 'date_received_3')
                __content_139738435934384_4128 = __quote(__content_139738435934384_4128, '\x00', '&#0;', None, None)
                __token = 4202
                __content_139738435934384_4200 = _lookup_attr(getitem('perm_storage'), 'date_received_3')
                __content_139738435934384_4200 = __quote(__content_139738435934384_4200, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                STORE_PERM( max(LOAD_PERM(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), '),(waiting_cargo_1 > 0) * current_date), ', (__content_139738435934384_3904 if (__content_139738435934384_3904 is not None) else ''), '),\n                STORE_PERM( max(LOAD_PERM(', (__content_139738435934384_3980 if (__content_139738435934384_3980 is not None) else ''), '),(waiting_cargo_2 > 0) * current_date), ', (__content_139738435934384_4052 if (__content_139738435934384_4052 is not None) else ''), '),\n                STORE_PERM( max(LOAD_PERM(', (__content_139738435934384_4128 if (__content_139738435934384_4128 is not None) else ''), '),(waiting_cargo_3 > 0) * current_date), ', (__content_139738435934384_4200 if (__content_139738435934384_4200 is not None) else ''), '),\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_PERM( (waiting_cargo_1 == 0 && waiting_cargo_2 == 0 && waiting_cargo_3 == 0) * LOAD_PERM(${perm_storage.closure_counter}), ${perm_storage.closure_counter}),\n\n                ' (52:53)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339bac0> -> __content_139738435934384
                __token = 4304
                __token = 4401
                __content_139738435934384 = _lookup_attr(getitem('perm_storage'), 'closure_counter')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 4435
                __content_139738435934384_4433 = _lookup_attr(getitem('perm_storage'), 'closure_counter')
                __content_139738435934384_4433 = __quote(__content_139738435934384_4433, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s' % ('\n                STORE_PERM( (waiting_cargo_1 == 0 && waiting_cargo_2 == 0 && waiting_cargo_3 == 0) * LOAD_PERM(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), '), ', (__content_139738435934384_4433 if (__content_139738435934384_4433 is not None) else ''), '),\n\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_1})) ' (55:127)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b820> -> __content_139738435934384
                __token = 4612
                __token = 4652
                __content_139738435934384 = _lookup_attr(getitem('perm_storage'), 'date_received_1')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s' % ('\n                STORE_TEMP( (current_date - LOAD_PERM(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ')) ', ))
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
                __append('<')

                # <Interpolation value=<Substitution '= ${global_constants.secondary_production_span}, ${var_received_timely_1}),\n                STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_2})) ' (56:89)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339bfa0> -> __content_139738435934384
                __token = 4685
                __token = 4689
                __content_139738435934384 = _lookup_attr(getitem('global_constants'), 'secondary_production_span')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 4736
                __content_139738435934384_4734 = getitem('var_received_timely_1')
                __content_139738435934384_4734 = __quote(__content_139738435934384_4734, '\x00', '&#0;', None, None)
                __token = 4817
                __content_139738435934384_4815 = _lookup_attr(getitem('perm_storage'), 'date_received_2')
                __content_139738435934384_4815 = __quote(__content_139738435934384_4815, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s' % ('= ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_4734 if (__content_139738435934384_4734 is not None) else ''), '),\n                STORE_TEMP( (current_date - LOAD_PERM(', (__content_139738435934384_4815 if (__content_139738435934384_4815 is not None) else ''), ')) ', ))
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
                __append('<')

                # <Interpolation value=<Substitution '= ${global_constants.secondary_production_span}, ${var_received_timely_2}),\n                STORE_TEMP( (current_date - LOAD_PERM(${perm_storage.date_received_3})) ' (57:89)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b310> -> __content_139738435934384
                __token = 4850
                __token = 4854
                __content_139738435934384 = _lookup_attr(getitem('global_constants'), 'secondary_production_span')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 4901
                __content_139738435934384_4899 = getitem('var_received_timely_2')
                __content_139738435934384_4899 = __quote(__content_139738435934384_4899, '\x00', '&#0;', None, None)
                __token = 4982
                __content_139738435934384_4980 = _lookup_attr(getitem('perm_storage'), 'date_received_3')
                __content_139738435934384_4980 = __quote(__content_139738435934384_4980, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s' % ('= ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_4899 if (__content_139738435934384_4899 is not None) else ''), '),\n                STORE_TEMP( (current_date - LOAD_PERM(', (__content_139738435934384_4980 if (__content_139738435934384_4980 is not None) else ''), ')) ', ))
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
                __append('<')

                # <Interpolation value=<Substitution '= ${global_constants.secondary_production_span}, ${var_received_timely_3}),\n\n                ' (58:89)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339bcd0> -> __content_139738435934384
                __token = 5015
                __token = 5019
                __content_139738435934384 = _lookup_attr(getitem('global_constants'), 'secondary_production_span')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 5066
                __content_139738435934384_5064 = getitem('var_received_timely_3')
                __content_139738435934384_5064 = __quote(__content_139738435934384_5064, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s' % ('= ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ', ', (__content_139738435934384_5064 if (__content_139738435934384_5064 is not None) else ''), '),\n\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_PERM( ${industry.get_prod_ratio(1,economy)} +\n                            LOAD_TEMP(${var_received_timely_2}) * ${industry.get_boost(2,1,economy)} +\n                            LOAD_TEMP(${var_received_timely_3}) * ${industry.get_boost(3,1,economy)},\n                    ${perm_storage.ratio_input_1}\n                ),\n                STORE_PERM( ${industry.get_prod_ratio(2,economy)} +\n                            LOAD_TEMP(${var_received_timely_1}) * ${industry.get_boost(1,2,economy)} +\n                            LOAD_TEMP(${var_received_timely_3}) * ${industry.get_boost(3,2,economy)},\n                    ${perm_storage.ratio_input_2}\n                ),\n                STORE_PERM( ${industry.get_prod_ratio(3,economy)} +\n                            LOAD_TEMP(${var_received_timely_1}) * ${industry.get_boost(1,3,economy)} +\n                            LOAD_TEMP(${var_received_timely_2}) * ${industry.get_boost(2,3,economy)},\n                    ${perm_storage.ratio_input_3}\n                ),\n\n                ' (60:87)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b220> -> __content_139738435934384
                __token = 5196
                __token = 5210
                __content_139738435934384 = _lookup_attr(getitem('industry'), 'get_prod_ratio')(1, getitem('economy'))
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 5288
                __content_139738435934384_5286 = getitem('var_received_timely_2')
                __content_139738435934384_5286 = __quote(__content_139738435934384_5286, '\x00', '&#0;', None, None)
                __token = 5316
                __content_139738435934384_5314 = _lookup_attr(getitem('industry'), 'get_boost')(2, 1, getitem('economy'))
                __content_139738435934384_5314 = __quote(__content_139738435934384_5314, '\x00', '&#0;', None, None)
                __token = 5391
                __content_139738435934384_5389 = getitem('var_received_timely_3')
                __content_139738435934384_5389 = __quote(__content_139738435934384_5389, '\x00', '&#0;', None, None)
                __token = 5419
                __content_139738435934384_5417 = _lookup_attr(getitem('industry'), 'get_boost')(3, 1, getitem('economy'))
                __content_139738435934384_5417 = __quote(__content_139738435934384_5417, '\x00', '&#0;', None, None)
                __token = 5475
                __content_139738435934384_5473 = _lookup_attr(getitem('perm_storage'), 'ratio_input_1')
                __content_139738435934384_5473 = __quote(__content_139738435934384_5473, '\x00', '&#0;', None, None)
                __token = 5552
                __content_139738435934384_5550 = _lookup_attr(getitem('industry'), 'get_prod_ratio')(2, getitem('economy'))
                __content_139738435934384_5550 = __quote(__content_139738435934384_5550, '\x00', '&#0;', None, None)
                __token = 5630
                __content_139738435934384_5628 = getitem('var_received_timely_1')
                __content_139738435934384_5628 = __quote(__content_139738435934384_5628, '\x00', '&#0;', None, None)
                __token = 5658
                __content_139738435934384_5656 = _lookup_attr(getitem('industry'), 'get_boost')(1, 2, getitem('economy'))
                __content_139738435934384_5656 = __quote(__content_139738435934384_5656, '\x00', '&#0;', None, None)
                __token = 5733
                __content_139738435934384_5731 = getitem('var_received_timely_3')
                __content_139738435934384_5731 = __quote(__content_139738435934384_5731, '\x00', '&#0;', None, None)
                __token = 5761
                __content_139738435934384_5759 = _lookup_attr(getitem('industry'), 'get_boost')(3, 2, getitem('economy'))
                __content_139738435934384_5759 = __quote(__content_139738435934384_5759, '\x00', '&#0;', None, None)
                __token = 5817
                __content_139738435934384_5815 = _lookup_attr(getitem('perm_storage'), 'ratio_input_2')
                __content_139738435934384_5815 = __quote(__content_139738435934384_5815, '\x00', '&#0;', None, None)
                __token = 5894
                __content_139738435934384_5892 = _lookup_attr(getitem('industry'), 'get_prod_ratio')(3, getitem('economy'))
                __content_139738435934384_5892 = __quote(__content_139738435934384_5892, '\x00', '&#0;', None, None)
                __token = 5972
                __content_139738435934384_5970 = getitem('var_received_timely_1')
                __content_139738435934384_5970 = __quote(__content_139738435934384_5970, '\x00', '&#0;', None, None)
                __token = 6000
                __content_139738435934384_5998 = _lookup_attr(getitem('industry'), 'get_boost')(1, 3, getitem('economy'))
                __content_139738435934384_5998 = __quote(__content_139738435934384_5998, '\x00', '&#0;', None, None)
                __token = 6075
                __content_139738435934384_6073 = getitem('var_received_timely_2')
                __content_139738435934384_6073 = __quote(__content_139738435934384_6073, '\x00', '&#0;', None, None)
                __token = 6103
                __content_139738435934384_6101 = _lookup_attr(getitem('industry'), 'get_boost')(2, 3, getitem('economy'))
                __content_139738435934384_6101 = __quote(__content_139738435934384_6101, '\x00', '&#0;', None, None)
                __token = 6159
                __content_139738435934384_6157 = _lookup_attr(getitem('perm_storage'), 'ratio_input_3')
                __content_139738435934384_6157 = __quote(__content_139738435934384_6157, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                STORE_PERM( ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_5286 if (__content_139738435934384_5286 is not None) else ''), ') * ', (__content_139738435934384_5314 if (__content_139738435934384_5314 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_5389 if (__content_139738435934384_5389 is not None) else ''), ') * ', (__content_139738435934384_5417 if (__content_139738435934384_5417 is not None) else ''), ',\n                    ', (__content_139738435934384_5473 if (__content_139738435934384_5473 is not None) else ''), '\n                ),\n                STORE_PERM( ', (__content_139738435934384_5550 if (__content_139738435934384_5550 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_5628 if (__content_139738435934384_5628 is not None) else ''), ') * ', (__content_139738435934384_5656 if (__content_139738435934384_5656 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_5731 if (__content_139738435934384_5731 is not None) else ''), ') * ', (__content_139738435934384_5759 if (__content_139738435934384_5759 is not None) else ''), ',\n                    ', (__content_139738435934384_5815 if (__content_139738435934384_5815 is not None) else ''), '\n                ),\n                STORE_PERM( ', (__content_139738435934384_5892 if (__content_139738435934384_5892 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_5970 if (__content_139738435934384_5970 is not None) else ''), ') * ', (__content_139738435934384_5998 if (__content_139738435934384_5998 is not None) else ''), ' +\n                            LOAD_TEMP(', (__content_139738435934384_6073 if (__content_139738435934384_6073 is not None) else ''), ') * ', (__content_139738435934384_6101 if (__content_139738435934384_6101 is not None) else ''), ',\n                    ', (__content_139738435934384_6157 if (__content_139738435934384_6157 is not None) else ''), '\n                ),\n\n                ', ))
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

                # <Interpolation value=<Substitution '\n                STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_1}) + waiting_cargo_1, ${perm_storage.leftover_cargo_1}),\n                STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_2}) + waiting_cargo_2, ${perm_storage.leftover_cargo_2}),\n                STORE_PERM( LOAD_PERM(${perm_storage.leftover_cargo_3}) + waiting_cargo_3, ${perm_storage.leftover_cargo_3}),\n\n                1\n                ]) {\n            ${industry.id}_simple_produce;\n        }\n    ' (77:74)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339b3a0> -> __content_139738435934384
                __token = 6298
                __token = 6322
                __content_139738435934384 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 6375
                __content_139738435934384_6373 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_1')
                __content_139738435934384_6373 = __quote(__content_139738435934384_6373, '\x00', '&#0;', None, None)
                __token = 6448
                __content_139738435934384_6446 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
                __content_139738435934384_6446 = __quote(__content_139738435934384_6446, '\x00', '&#0;', None, None)
                __token = 6501
                __content_139738435934384_6499 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_2')
                __content_139738435934384_6499 = __quote(__content_139738435934384_6499, '\x00', '&#0;', None, None)
                __token = 6574
                __content_139738435934384_6572 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
                __content_139738435934384_6572 = __quote(__content_139738435934384_6572, '\x00', '&#0;', None, None)
                __token = 6627
                __content_139738435934384_6625 = _lookup_attr(getitem('perm_storage'), 'leftover_cargo_3')
                __content_139738435934384_6625 = __quote(__content_139738435934384_6625, '\x00', '&#0;', None, None)
                __token = 6714
                __content_139738435934384_6712 = _lookup_attr(getitem('industry'), 'id')
                __content_139738435934384_6712 = __quote(__content_139738435934384_6712, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                STORE_PERM( LOAD_PERM(', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ') + waiting_cargo_1, ', (__content_139738435934384_6373 if (__content_139738435934384_6373 is not None) else ''), '),\n                STORE_PERM( LOAD_PERM(', (__content_139738435934384_6446 if (__content_139738435934384_6446 is not None) else ''), ') + waiting_cargo_2, ', (__content_139738435934384_6499 if (__content_139738435934384_6499 is not None) else ''), '),\n                STORE_PERM( LOAD_PERM(', (__content_139738435934384_6572 if (__content_139738435934384_6572 is not None) else ''), ') + waiting_cargo_3, ', (__content_139738435934384_6625 if (__content_139738435934384_6625 is not None) else ''), '),\n\n                1\n                ]) {\n            ', (__content_139738435934384_6712 if (__content_139738435934384_6712 is not None) else ''), '_simple_produce;\n        }\n    ', ))
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
                ____index_139738425703008 -= 1
                if (____index_139738425703008 > 0):
                    __append('')
            if (__backup_economy_139738426997008 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139738426997008

            # <Interpolation value=<Substitution '\n\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_produce, economy) {\n        ' (86:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f17633cfe80> -> __content_139738435934384
            __token = 6779
            __token = 6812
            __content_139738435934384 = _lookup_attr(getitem('industry'), 'id')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s' % ('\n\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), '_produce, economy) {\n        ', ))
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

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738425702384
            __attrs_139738425702384 = _static_139738431409216
            __backup_economy_139738426002976 = get('economy', __marker)

            # <Value 'economies' (89:39)> -> __iterator
            __token = 6884
            __iterator = getitem('economies')
            (__iterator, ____index_139738425703200, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n            ${economy.numeric_id}: ${industry.id}_produce_economy_${economy.numeric_id};\n        ' (89:50)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f176339ba00> -> __content_139738435934384
                __token = 6908
                __token = 6910
                __content_139738435934384 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 6933
                __content_139738435934384_6931 = _lookup_attr(getitem('industry'), 'id')
                __content_139738435934384_6931 = __quote(__content_139738435934384_6931, '\x00', '&#0;', None, None)
                __token = 6964
                __content_139738435934384_6962 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139738435934384_6962 = __quote(__content_139738435934384_6962, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s%s%s' % ('\n            ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ': ', (__content_139738435934384_6931 if (__content_139738435934384_6931 is not None) else ''), '_produce_economy_', (__content_139738435934384_6962 if (__content_139738435934384_6962 is not None) else ''), ';\n        ', ))
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
                ____index_139738425703200 -= 1
                if (____index_139738425703200 > 0):
                    __append('')
            if (__backup_economy_139738426002976 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139738426002976
            __append('\n    }\n')
            if (__backup_perm_storage_139738426002592 is __marker):
                del econtext['perm_storage']
            else:
                econtext['perm_storage'] = __backup_perm_storage_139738426002592
            if (__backup_var_input_ratio_max_sum_139738426002928 is __marker):
                del econtext['var_input_ratio_max_sum']
            else:
                econtext['var_input_ratio_max_sum'] = __backup_var_input_ratio_max_sum_139738426002928
            if (__backup_var_output_ratio_max_sum_139738427835968 is __marker):
                del econtext['var_output_ratio_max_sum']
            else:
                econtext['var_output_ratio_max_sum'] = __backup_var_output_ratio_max_sum_139738427835968
            if (__backup_var_output_ratio_2_139738426001776 is __marker):
                del econtext['var_output_ratio_2']
            else:
                econtext['var_output_ratio_2'] = __backup_var_output_ratio_2_139738426001776
            if (__backup_var_output_ratio_1_139738426002256 is __marker):
                del econtext['var_output_ratio_1']
            else:
                econtext['var_output_ratio_1'] = __backup_var_output_ratio_1_139738426002256
            if (__backup_var_num_output_cargos_139738425152512 is __marker):
                del econtext['var_num_output_cargos']
            else:
                econtext['var_num_output_cargos'] = __backup_var_num_output_cargos_139738425152512
            if (__backup_var_received_timely_3_139738426344784 is __marker):
                del econtext['var_received_timely_3']
            else:
                econtext['var_received_timely_3'] = __backup_var_received_timely_3_139738426344784
            if (__backup_var_received_timely_2_139738426612368 is __marker):
                del econtext['var_received_timely_2']
            else:
                econtext['var_received_timely_2'] = __backup_var_received_timely_2_139738426612368
            if (__backup_var_received_timely_1_139738426974272 is __marker):
                del econtext['var_received_timely_1']
            else:
                econtext['var_received_timely_1'] = __backup_var_received_timely_1_139738426974272
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }