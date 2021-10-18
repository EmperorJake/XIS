# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/XIS/src/templates/header.pynml'

__tokens = {0: ('grf {\n\tgrfid: "\\4A\\44\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 9050;\n\tparam 0 {', 1, 0), 127: ('repo_vars.repo_revision', 6, 12), 320: ('economy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {', 10, 2), 459: ('len(economies)-1', 14, 16), 534: ('economies', 16, 44), 566: ('${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});', 17, 20), 568: ('repeat.economy.index', 17, 22), 626: ('economy.id', 17, 80), 1449: ('param 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}', 52, 1), 2063: ('global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 74, 16), 2333: ('5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 83, 16)}

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

            # <Interpolation value=<Substitution 'grf {\n\tgrfid: "\\4A\\44\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 9050;\n\tparam 0 {\n\t    ' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763693190> -> __content_139738435934384
            __token = 0
            __token = 127
            __content_139738435934384 = _lookup_attr(getitem('repo_vars'), 'repo_revision')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s' % ('grf {\n\tgrfid: "\\4A\\44\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ';\n\tmin_compatible_version: 9050;\n\tparam 0 {\n\t    ', ))
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

            # <Interpolation value=<Substitution '\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {\n\t\t\t    ' (9:122)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763693250> -> __content_139738435934384
            __token = 320
            __token = 459
            __content_139738435934384 = (len(getitem('economies')) - 1)
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s' % ('\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
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

            # <Static value=<_ast.Dict object at 0x7f176390cc40> name=None at 7f176390ca60> -> __attrs_139738428814528
            __attrs_139738428814528 = _static_139738431409216
            __backup_economy_139738447009488 = get('economy', __marker)

            # <Value 'economies' (16:44)> -> __iterator
            __token = 534
            __iterator = getitem('economies')
            (__iterator, ____index_139738428814768, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n                    ${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});\n\t\t\t    ' (16:55)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763693700> -> __content_139738435934384
                __token = 566
                __token = 568
                __content_139738435934384 = _lookup_attr(_lookup_attr(getitem('repeat'), 'economy'), 'index')
                __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
                __token = 626
                __content_139738435934384_624 = _lookup_attr(getitem('economy'), 'id')
                __content_139738435934384_624 = __quote(__content_139738435934384_624, '\x00', '&#0;', None, None)
                __content_139738435934384 = ('%s%s%s%s%s' % ('\n                    ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ': string(STR_PARAM_VALUE_ECONOMIES_', (__content_139738435934384_624 if (__content_139738435934384_624 is not None) else ''), ');\n\t\t\t    ', ))
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
                ____index_139738428814768 -= 1
                if (____index_139738428814768 > 0):
                    __append('')
            if (__backup_economy_139738447009488 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139738447009488
            __append('\n\t\t\t};\n\t\t}\n\t}\n\tparam 2 {\n\t\t\n\t\t\n\t\tallow_close_secondary {\n\t\t\tname: string(STR_PARAM_NAME_SECONDARY_NEVER_CLOSE);\n\t\t\tdesc: string(STR_PARAM_DESC_SECONDARY_NEVER_CLOSE);\n\t\t\ttype: bool;\n\t\t\tbit: 1;\n\t\t}\n\t\trestrict_open_during_gameplay {\n\t\t\tname: string(STR_PARAM_NAME_NO_OPENINGS);\n\t\t\tdesc: string(STR_PARAM_DESC_NO_OPENINGS);\n\t\t\ttype: bool;\n\t\t\tbit: 2;\n\t\t}\n\t}\n\t\n\t')

            # <Interpolation value=<Substitution '\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n' (51:6)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f1763693670> -> __content_139738435934384
            __token = 1449
            __token = 2063
            __content_139738435934384 = _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT')
            __content_139738435934384 = __quote(__content_139738435934384, '\x00', '&#0;', None, None)
            __token = 2333
            __content_139738435934384_2331 = (5 * _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT'))
            __content_139738435934384_2331 = __quote(__content_139738435934384_2331, '\x00', '&#0;', None, None)
            __content_139738435934384 = ('%s%s%s%s%s' % ('\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_139738435934384 if (__content_139738435934384 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_139738435934384_2331 if (__content_139738435934384_2331 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n', ))
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
            __append('\nif (param[6] == 0) { param[6] = 100; }\nif (param[7] == 0) { param[7] = 100; }\nif (param[8] == 0) { param[8] = 400; }\nif (param[9] == 0) { param[9] = 300; }\n\n\ndisable_item(FEAT_INDUSTRIES, 0, 36);\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }