# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/parameters.pynml'
__tokens = {1252: ('economies', 21, 35), 1268: ('if (economy_selection == ${repeat.economy.index}) {\n        economy = ${economy.numeric_id};\n    }', 22, 4), 1295: ('repeat.economy.index', 22, 31), 1340: ('economy.numeric_id', 23, 20)}

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
            __append('// parameters also referenced by action 14 stuff - likely to be found in header.pynml, unless it got moved\n\n// map_size is total number of tiles on the map\n// compute relative size of the map, compared to 256*256\nrelative_map_size = map_size / (256 * 256);\n// number of industry closures is proportional to map size (maps ')
            __append('<')
            __append("= 256x256 will have 1 cluster)\nindustry_clusters = (relative_map_size / 2) + 1;\n\nparam_max_coastal_distance = marine_industry_max_coastal_distance;\nif (marine_industry_max_coastal_distance == 0) {\n\tparam_max_coastal_distance = 255;\n}\n\n// I want to specify the order of the economies in parameter menu without worrying about breaking savegames etc\n// but action 14 can't separate parameter value and position in menu for economies\n// so here we remap selected economy to actual numeric value\n// !! having tested, this doesn't actually prevent savegame breaking\n// !! as the selected value in the action 14 UI remains constant (thereby changing which economy is active)\n// !! there is zero chance of it being worthwhile to write a migration for existing savegames\n// !! therefore rethink this - whether it's worthwhile, or whether to just reset economy order every time when adding new economies\n")
            __backup_economy_139703132007280 = get('economy', __marker)

            # <Value 'economies' (21:35)> -> __iterator
            __token = 1252
            __iterator = getitem('economies')
            (__iterator, ____index_139703106015304, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n    if (economy_selection == ${repeat.economy.index}) {\n        economy = ${economy.numeric_id};\n    }\n' (21:46)> braces_required=True translation=False at 7f0f2a021198> -> __content_139703124559104
                __token = 1268
                __token = 1295
                __content_139703124559104 = _lookup_attr(_lookup_attr(getitem('repeat'), 'economy'), 'index')
                __content_139703124559104 = __quote(__content_139703124559104, '\x00', '&#0;', None, False)
                __token = 1340
                __content_139703124559104_1338 = _lookup_attr(getitem('economy'), 'numeric_id')
                __content_139703124559104_1338 = __quote(__content_139703124559104_1338, '\x00', '&#0;', None, False)
                __content_139703124559104 = ('%s%s%s%s%s' % ('\n    if (economy_selection == ', (__content_139703124559104 if (__content_139703124559104 is not None) else ''), ') {\n        economy = ', (__content_139703124559104_1338 if (__content_139703124559104_1338 is not None) else ''), ';\n    }\n', ))
                if (__content_139703124559104 is None):
                    pass
                else:
                    if (__content_139703124559104 is False):
                        __content_139703124559104 = None
                    else:
                        __tt = type(__content_139703124559104)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139703124559104 = str(__content_139703124559104)
                        else:
                            if (__tt is bytes):
                                __content_139703124559104 = decode(__content_139703124559104)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139703124559104 = __content_139703124559104.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139703124559104)
                                        __content_139703124559104 = (str(__content_139703124559104) if (__content_139703124559104 is __converted) else __converted)
                                    else:
                                        __content_139703124559104 = __content_139703124559104()
                if (__content_139703124559104 is not None):
                    __append(__content_139703124559104)
                ____index_139703106015304 -= 1
                if (____index_139703106015304 > 0):
                    __append('')
            if (__backup_economy_139703132007280 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_139703132007280
            __append('\n\n// production bonuses are expressed as absolute % of base production in parameters menu,\n// but we need them as bonus amounts, to be added on top of base production, so net off 100\nprimary_level1_bonus = primary_level1_produced_percent - 100;\nprimary_level2_bonus = primary_level2_produced_percent - 100;\n\n// the tree for the food market is a climate-dependent special case, re-using base set sprites\n// it has to be handled here as a parameter, no elegant way to include it in the industry\nmarket_tree = 1639;\nif (climate == CLIMATE_ARCTIC) { market_tree = 1737; }\nif (climate == CLIMATE_TROPICAL) { market_tree = 1891; }\nmarket_tree_snow = 1793;\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }