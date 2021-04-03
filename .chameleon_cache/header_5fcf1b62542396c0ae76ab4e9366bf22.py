# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/firs-3.0.10-source/bundle_dir/src/src/templates/header.pynml'
__tokens = {0: ('grf {\n\tgrfid: "\\F1%\\00\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {', 1, 0), 125: ('repo_vars.repo_revision', 6, 12), 318: ('economy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {', 10, 2), 457: ('len(economies)-1', 14, 16), 532: ('economies', 16, 44), 564: ('${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});', 17, 20), 566: ('repeat.economy.index', 17, 22), 624: ('economy.id', 17, 80), 1447: ('param 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}', 52, 1), 2061: ('global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 74, 16), 2331: ('5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 83, 16)}

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

            # <Interpolation value=<Substitution 'grf {\n\tgrfid: "\\F1%\\00\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ' (1:0)> braces_required=True translation=False at 7f7ef3b2a9e8> -> __content_140183249773656
            __token = 0
            __token = 125
            __content_140183249773656 = _lookup_attr(getitem('repo_vars'), 'repo_revision')
            __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
            __content_140183249773656 = ('%s%s%s' % ('grf {\n\tgrfid: "\\F1%\\00\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ';\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ', ))
            if (__content_140183249773656 is None):
                pass
            else:
                if (__content_140183249773656 is False):
                    __content_140183249773656 = None
                else:
                    __tt = type(__content_140183249773656)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140183249773656 = str(__content_140183249773656)
                    else:
                        if (__tt is bytes):
                            __content_140183249773656 = decode(__content_140183249773656)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140183249773656 = __content_140183249773656.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140183249773656)
                                    __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                else:
                                    __content_140183249773656 = __content_140183249773656()
            if (__content_140183249773656 is not None):
                __append(__content_140183249773656)

            # <Interpolation value=<Substitution '\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {\n\t\t\t    ' (9:122)> braces_required=True translation=False at 7f7ef3b2aac8> -> __content_140183249773656
            __token = 318
            __token = 457
            __content_140183249773656 = (len(getitem('economies')) - 1)
            __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
            __content_140183249773656 = ('%s%s%s' % ('\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
            if (__content_140183249773656 is None):
                pass
            else:
                if (__content_140183249773656 is False):
                    __content_140183249773656 = None
                else:
                    __tt = type(__content_140183249773656)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140183249773656 = str(__content_140183249773656)
                    else:
                        if (__tt is bytes):
                            __content_140183249773656 = decode(__content_140183249773656)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140183249773656 = __content_140183249773656.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140183249773656)
                                    __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                else:
                                    __content_140183249773656 = __content_140183249773656()
            if (__content_140183249773656 is not None):
                __append(__content_140183249773656)
            __backup_economy_140183257336296 = get('economy', __marker)

            # <Value 'economies' (16:44)> -> __iterator
            __token = 532
            __iterator = getitem('economies')
            (__iterator, ____index_140183231179912, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n                    ${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});\n\t\t\t    ' (16:55)> braces_required=True translation=False at 7f7ef3b2acc0> -> __content_140183249773656
                __token = 564
                __token = 566
                __content_140183249773656 = _lookup_attr(_lookup_attr(getitem('repeat'), 'economy'), 'index')
                __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
                __token = 624
                __content_140183249773656_622 = _lookup_attr(getitem('economy'), 'id')
                __content_140183249773656_622 = __quote(__content_140183249773656_622, '\x00', '&#0;', None, False)
                __content_140183249773656 = ('%s%s%s%s%s' % ('\n                    ', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ': string(STR_PARAM_VALUE_ECONOMIES_', (__content_140183249773656_622 if (__content_140183249773656_622 is not None) else ''), ');\n\t\t\t    ', ))
                if (__content_140183249773656 is None):
                    pass
                else:
                    if (__content_140183249773656 is False):
                        __content_140183249773656 = None
                    else:
                        __tt = type(__content_140183249773656)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140183249773656 = str(__content_140183249773656)
                        else:
                            if (__tt is bytes):
                                __content_140183249773656 = decode(__content_140183249773656)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140183249773656 = __content_140183249773656.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140183249773656)
                                        __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                    else:
                                        __content_140183249773656 = __content_140183249773656()
                if (__content_140183249773656 is not None):
                    __append(__content_140183249773656)
                ____index_140183231179912 -= 1
                if (____index_140183231179912 > 0):
                    __append('')
            if (__backup_economy_140183257336296 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140183257336296
            __append('\n\t\t\t};\n\t\t}\n\t}\n\tparam 2 {\n\t\t')
            __append('\n\t\t')
            __append('\n\t\tallow_close_secondary {\n\t\t\tname: string(STR_PARAM_NAME_SECONDARY_NEVER_CLOSE);\n\t\t\tdesc: string(STR_PARAM_DESC_SECONDARY_NEVER_CLOSE);\n\t\t\ttype: bool;\n\t\t\tbit: 1;\n\t\t}\n\t\trestrict_open_during_gameplay {\n\t\t\tname: string(STR_PARAM_NAME_NO_OPENINGS);\n\t\t\tdesc: string(STR_PARAM_DESC_NO_OPENINGS);\n\t\t\ttype: bool;\n\t\t\tbit: 2;\n\t\t}\n\t}\n\t')
            __append('\n\t')

            # <Interpolation value=<Substitution '\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n' (51:6)> braces_required=True translation=False at 7f7ef3b2ad30> -> __content_140183249773656
            __token = 1447
            __token = 2061
            __content_140183249773656 = _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT')
            __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
            __token = 2331
            __content_140183249773656_2329 = (5 * _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT'))
            __content_140183249773656_2329 = __quote(__content_140183249773656_2329, '\x00', '&#0;', None, False)
            __content_140183249773656 = ('%s%s%s%s%s' % ('\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_140183249773656_2329 if (__content_140183249773656_2329 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n', ))
            if (__content_140183249773656 is None):
                pass
            else:
                if (__content_140183249773656 is False):
                    __content_140183249773656 = None
                else:
                    __tt = type(__content_140183249773656)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140183249773656 = str(__content_140183249773656)
                    else:
                        if (__tt is bytes):
                            __content_140183249773656 = decode(__content_140183249773656)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140183249773656 = __content_140183249773656.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140183249773656)
                                    __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                else:
                                    __content_140183249773656 = __content_140183249773656()
            if (__content_140183249773656 is not None):
                __append(__content_140183249773656)
            __append('\nif (param[6] == 0) { param[6] = 100; }\nif (param[7] == 0) { param[7] = 100; }\nif (param[8] == 0) { param[8] = 400; }\nif (param[9] == 0) { param[9] = 300; }\n\n')
            __append('\ndisable_item(FEAT_INDUSTRIES, 0, 36);\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }