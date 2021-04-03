# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/location_check_macros_industry.pynml'
__tokens = {404: ('industry.location_checks.get_render_tree(incompatible_industries)', 9, 58), 494: ('location_checks', 9, 148), 563: ('location_check.macro', 10, 51), 563: ('location_check.macro', 10, 51), 797: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, water_distance) {\n        0 .. param_max_coastal_distance: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 19, 4), 830: ('location_check.switch_entry_point', 19, 37), 927: ('location_check.switch_result', 20, 43), 1191: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_distance(${location_check.industry_type_numeric_id})) {\n        0 .. ${location_check.distance}: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 28, 4), 1224: ('location_check.switch_entry_point', 28, 37), 1280: ('location_check.industry_type_numeric_id', 28, 93), 1340: ('location_check.distance', 29, 15), 1412: ('location_check.switch_result', 30, 10), 1645: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_industry_max_distance_2, industry_distance(${location_check.industry_type_numeric_id})) {\n        0 .. ${location_check.distance}: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 37, 4), 1678: ('industry.id', 37, 37), 1742: ('location_check.industry_type_numeric_id', 37, 101), 1802: ('location_check.distance', 38, 15), 1830: ('location_check.switch_result', 38, 43), 2220: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_count(${location_check.industry_type_numeric_id})) {\n        0: ${location_check.switch_result};\n        ${industry.id}_check_industry_max_distance_2;\n    }', 44, 4), 2253: ('location_check.switch_entry_point', 44, 37), 2306: ('location_check.industry_type_numeric_id', 44, 90), 2364: ('location_check.switch_result', 45, 13), 2405: ('industry.id', 46, 10), 2604: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point},\n                industry_count(${location_check.industry_type_numeric_id}) >= (${location_check.cluster_factor} * industry_clusters) &&\n                industry_distance(${location_check.industry_type_numeric_id}) > ${location_check.max_distance}\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }', 53, 4), 2637: ('location_check.switch_entry_point', 53, 37), 2706: ('location_check.industry_type_numeric_id', 54, 33), 2754: ('location_check.cluster_factor', 54, 81), 2845: ('location_check.industry_type_numeric_id', 55, 36), 2891: ('location_check.max_distance', 55, 82), 2993: ('location_check.switch_result', 58, 10), 3178: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_town_count(${location_check.industry_type_numeric_id})) {\n        ${location_check.min_count} .. ${location_check.max_count}: ${location_check.switch_result};\n        return string(STR_ERR_LOCATION_LIMIT_1_PER_TOWN);\n    }', 65, 4), 3211: ('location_check.switch_entry_point', 65, 37), 3269: ('location_check.industry_type_numeric_id', 65, 95), 3324: ('location_check.min_count', 66, 10), 3355: ('location_check.max_count', 66, 41), 3384: ('location_check.switch_result', 66, 70), 3825: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, (\n                (extra_callback_info2 == IND_CREATION_FUND) ||\n                (extra_callback_info2 == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }', 78, 4), 3858: ('location_check.switch_entry_point', 78, 37), 4111: ('location_check.switch_result', 84, 10), 4490: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_brick_layouts_only_check_layout, var[0x86]) {\n        3..5: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_brick_layouts_only, extra_callback_info2) {\n        IND_CREATION_GENERATION: ${location_check.switch_result};\n        ${industry.id}_brick_layouts_only_check_layout;\n    }', 96, 4), 4523: ('industry.id', 96, 37), 4642: ('location_check.switch_result', 98, 10), 4716: ('industry.id', 100, 37), 4808: ('location_check.switch_result', 101, 35), 4849: ('industry.id', 102, 10), 4962: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_windmill_layout_only, var[0x86]) {\n        3..5: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }', 105, 4), 4995: ('industry.id', 105, 37), 5059: ('location_check.switch_result', 106, 16), 5267: ('switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, current_year) {\n        0..1869:    ${industry.id}_windmill_layout_only;\n        1870..1900: ${location_check.switch_result};\n        ${industry.id}_brick_layouts_only;\n    }', 111, 4), 5300: ('location_check.switch_entry_point', 111, 37), 5374: ('industry.id', 112, 22), 5431: ('location_check.switch_result', 113, 22), 5472: ('industry.id', 114, 10)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140166499179488 = 'location_check.macro'

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render_render_tree(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __backup_location_checks_140166499179936 = get('location_checks', __marker)

            # <Value 'industry.location_checks.get_render_tree(incompatible_industries)' (9:58)> -> __value
            __token = 404
            __value = _lookup_attr(_lookup_attr(getitem('industry'), 'location_checks'), 'get_render_tree')(getitem('incompatible_industries'))
            econtext['location_checks'] = __value
            __backup_location_check_140166499177360 = get('location_check', __marker)

            # <Value 'location_checks' (9:148)> -> __iterator
            __token = 494
            __iterator = getitem('location_checks')
            (__iterator, ____index_140166499180384, ) = getitem('repeat')('location_check', __iterator)
            econtext['location_check'] = None
            for __item in __iterator:
                econtext['location_check'] = __item
                __append('\n        ')
                __backup_macroname_140166497560264 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f7b0e649be0> name=None at 7f7b0e649588> -> __value
                __value = _static_140166499179488
                econtext['macroname'] = __value

                # <Value 'location_check.macro' (10:51)> -> __macro
                __token = 563
                __macro = _lookup_attr(getitem('location_check'), 'macro')
                __token = 563
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140166497560264 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140166497560264
                __append('\n    ')
                ____index_140166499180384 -= 1
                if (____index_140166499180384 > 0):
                    __append('')
            if (__backup_location_check_140166499177360 is __marker):
                del econtext['location_check']
            else:
                econtext['location_check'] = __backup_location_check_140166499177360
            if (__backup_location_checks_140166499179936 is __marker):
                del econtext['location_checks']
            else:
                econtext['location_checks'] = __backup_location_checks_140166499179936
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_coast_distance(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, water_distance) {\n        0 .. param_max_coastal_distance: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n' (18:53)> braces_required=True translation=False at 7f7b0e649a20> -> __content_140166518101192
            __token = 797
            __token = 830
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 927
            __content_140166518101192_925 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_925 = __quote(__content_140166518101192_925, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', water_distance) {\n        0 .. param_max_coastal_distance: ', (__content_140166518101192_925 if (__content_140166518101192_925 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n', ))
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


    def render_check_industry_min_distance(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_distance(${location_check.industry_type_numeric_id})) {\n        0 .. ${location_check.distance}: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n' (27:67)> braces_required=True translation=False at 7f7b0e649b70> -> __content_140166518101192
            __token = 1191
            __token = 1224
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1280
            __content_140166518101192_1278 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_1278 = __quote(__content_140166518101192_1278, '\x00', '&#0;', None, False)
            __token = 1340
            __content_140166518101192_1338 = _lookup_attr(getitem('location_check'), 'distance')
            __content_140166518101192_1338 = __quote(__content_140166518101192_1338, '\x00', '&#0;', None, False)
            __token = 1412
            __content_140166518101192_1410 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_1410 = __quote(__content_140166518101192_1410, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', industry_distance(', (__content_140166518101192_1278 if (__content_140166518101192_1278 is not None) else ''), ')) {\n        0 .. ', (__content_140166518101192_1338 if (__content_140166518101192_1338 is not None) else ''), ': return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_1410 if (__content_140166518101192_1410 is not None) else ''), ';\n    }\n', ))
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


    def render_check_industry_max_distance(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_check_industry_max_distance_2, industry_distance(${location_check.industry_type_numeric_id})) {\n        0 .. ${location_check.distance}: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n    ' (36:67)> braces_required=True translation=False at 7f7b0e649438> -> __content_140166518101192
            __token = 1645
            __token = 1678
            __content_140166518101192 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 1742
            __content_140166518101192_1740 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_1740 = __quote(__content_140166518101192_1740, '\x00', '&#0;', None, False)
            __token = 1802
            __content_140166518101192_1800 = _lookup_attr(getitem('location_check'), 'distance')
            __content_140166518101192_1800 = __quote(__content_140166518101192_1800, '\x00', '&#0;', None, False)
            __token = 1830
            __content_140166518101192_1828 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_1828 = __quote(__content_140166518101192_1828, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), '_check_industry_max_distance_2, industry_distance(', (__content_140166518101192_1740 if (__content_140166518101192_1740 is not None) else ''), ')) {\n        0 .. ', (__content_140166518101192_1800 if (__content_140166518101192_1800 is not None) else ''), ': ', (__content_140166518101192_1828 if (__content_140166518101192_1828 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n    ', ))
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_count(${location_check.industry_type_numeric_id})) {\n        0: ${location_check.switch_result};\n        ${industry.id}_check_industry_max_distance_2;\n    }\n' (43:135)> braces_required=True translation=False at 7f7b0e649668> -> __content_140166518101192
            __token = 2220
            __token = 2253
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 2306
            __content_140166518101192_2304 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_2304 = __quote(__content_140166518101192_2304, '\x00', '&#0;', None, False)
            __token = 2364
            __content_140166518101192_2362 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_2362 = __quote(__content_140166518101192_2362, '\x00', '&#0;', None, False)
            __token = 2405
            __content_140166518101192_2403 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_2403 = __quote(__content_140166518101192_2403, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', industry_count(', (__content_140166518101192_2304 if (__content_140166518101192_2304 is not None) else ''), ')) {\n        0: ', (__content_140166518101192_2362 if (__content_140166518101192_2362 is not None) else ''), ';\n        ', (__content_140166518101192_2403 if (__content_140166518101192_2403 is not None) else ''), '_check_industry_max_distance_2;\n    }\n', ))
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


    def render_cluster(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point},\n                industry_count(${location_check.industry_type_numeric_id}) >= (${location_check.cluster_factor} * industry_clusters) &&\n                industry_distance(${location_check.industry_type_numeric_id}) > ${location_check.max_distance}\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n' (52:60)> braces_required=True translation=False at 7f7b0e6496d8> -> __content_140166518101192
            __token = 2604
            __token = 2637
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 2706
            __content_140166518101192_2704 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_2704 = __quote(__content_140166518101192_2704, '\x00', '&#0;', None, False)
            __token = 2754
            __content_140166518101192_2752 = _lookup_attr(getitem('location_check'), 'cluster_factor')
            __content_140166518101192_2752 = __quote(__content_140166518101192_2752, '\x00', '&#0;', None, False)
            __token = 2845
            __content_140166518101192_2843 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_2843 = __quote(__content_140166518101192_2843, '\x00', '&#0;', None, False)
            __token = 2891
            __content_140166518101192_2889 = _lookup_attr(getitem('location_check'), 'max_distance')
            __content_140166518101192_2889 = __quote(__content_140166518101192_2889, '\x00', '&#0;', None, False)
            __token = 2993
            __content_140166518101192_2991 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_2991 = __quote(__content_140166518101192_2991, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ',\n                industry_count(', (__content_140166518101192_2704 if (__content_140166518101192_2704 is not None) else ''), ') >= (', (__content_140166518101192_2752 if (__content_140166518101192_2752 is not None) else ''), ' * industry_clusters) &&\n                industry_distance(', (__content_140166518101192_2843 if (__content_140166518101192_2843 is not None) else ''), ') > ', (__content_140166518101192_2889 if (__content_140166518101192_2889 is not None) else ''), '\n            ) {\n        1: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_2991 if (__content_140166518101192_2991 is not None) else ''), ';\n    }\n', ))
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


    def render_town_industry_count(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, industry_town_count(${location_check.industry_type_numeric_id})) {\n        ${location_check.min_count} .. ${location_check.max_count}: ${location_check.switch_result};\n        return string(STR_ERR_LOCATION_LIMIT_1_PER_TOWN);\n    }\n' (64:55)> braces_required=True translation=False at 7f7b0e6497f0> -> __content_140166518101192
            __token = 3178
            __token = 3211
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 3269
            __content_140166518101192_3267 = _lookup_attr(getitem('location_check'), 'industry_type_numeric_id')
            __content_140166518101192_3267 = __quote(__content_140166518101192_3267, '\x00', '&#0;', None, False)
            __token = 3324
            __content_140166518101192_3322 = _lookup_attr(getitem('location_check'), 'min_count')
            __content_140166518101192_3322 = __quote(__content_140166518101192_3322, '\x00', '&#0;', None, False)
            __token = 3355
            __content_140166518101192_3353 = _lookup_attr(getitem('location_check'), 'max_count')
            __content_140166518101192_3353 = __quote(__content_140166518101192_3353, '\x00', '&#0;', None, False)
            __token = 3384
            __content_140166518101192_3382 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_3382 = __quote(__content_140166518101192_3382, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', industry_town_count(', (__content_140166518101192_3267 if (__content_140166518101192_3267 is not None) else ''), ')) {\n        ', (__content_140166518101192_3322 if (__content_140166518101192_3322 is not None) else ''), ' .. ', (__content_140166518101192_3353 if (__content_140166518101192_3353 is not None) else ''), ': ', (__content_140166518101192_3382 if (__content_140166518101192_3382 is not None) else ''), ';\n        return string(STR_ERR_LOCATION_LIMIT_1_PER_TOWN);\n    }\n', ))
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


    def render_check_founder(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, (\n                (extra_callback_info2 == IND_CREATION_FUND) ||\n                (extra_callback_info2 == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ${location_check.switch_result};\n    }\n' (77:7)> braces_required=True translation=False at 7f7b0e543a58> -> __content_140166518101192
            __token = 3825
            __token = 3858
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 4111
            __content_140166518101192_4109 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_4109 = __quote(__content_140166518101192_4109, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', (\n                (extra_callback_info2 == IND_CREATION_FUND) ||\n                (extra_callback_info2 == IND_CREATION_PROSPECT)\n                )\n            ) {\n        1: return CB_RESULT_LOCATION_ALLOW;\n        ', (__content_140166518101192_4109 if (__content_140166518101192_4109 is not None) else ''), ';\n    }\n', ))
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


    def render_flour_mill_layouts_by_date(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __append('\n\n    ')

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_brick_layouts_only_check_layout, var[0x86]) {\n        3..5: return CB_RESULT_LOCATION_DISALLOW;\n        ${location_check.switch_result};\n    }\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_brick_layouts_only, extra_callback_info2) {\n        IND_CREATION_GENERATION: ${location_check.switch_result};\n        ${industry.id}_brick_layouts_only_check_layout;\n    }\n    ' (95:113)> braces_required=True translation=False at 7f7b0e5436a0> -> __content_140166518101192
            __token = 4490
            __token = 4523
            __content_140166518101192 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 4642
            __content_140166518101192_4640 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_4640 = __quote(__content_140166518101192_4640, '\x00', '&#0;', None, False)
            __token = 4716
            __content_140166518101192_4714 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_4714 = __quote(__content_140166518101192_4714, '\x00', '&#0;', None, False)
            __token = 4808
            __content_140166518101192_4806 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_4806 = __quote(__content_140166518101192_4806, '\x00', '&#0;', None, False)
            __token = 4849
            __content_140166518101192_4847 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_4847 = __quote(__content_140166518101192_4847, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), '_brick_layouts_only_check_layout, var[0x86]) {\n        3..5: return CB_RESULT_LOCATION_DISALLOW;\n        ', (__content_140166518101192_4640 if (__content_140166518101192_4640 is not None) else ''), ';\n    }\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192_4714 if (__content_140166518101192_4714 is not None) else ''), '_brick_layouts_only, extra_callback_info2) {\n        IND_CREATION_GENERATION: ', (__content_140166518101192_4806 if (__content_140166518101192_4806 is not None) else ''), ';\n        ', (__content_140166518101192_4847 if (__content_140166518101192_4847 is not None) else ''), '_brick_layouts_only_check_layout;\n    }\n    ', ))
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${industry.id}_windmill_layout_only, var[0x86]) {\n        3..5: ${location_check.switch_result};\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n    ' (104:56)> braces_required=True translation=False at 7f7b0e543da0> -> __content_140166518101192
            __token = 4962
            __token = 4995
            __content_140166518101192 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 5059
            __content_140166518101192_5057 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_5057 = __quote(__content_140166518101192_5057, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), '_windmill_layout_only, var[0x86]) {\n        3..5: ', (__content_140166518101192_5057 if (__content_140166518101192_5057 is not None) else ''), ';\n        return CB_RESULT_LOCATION_DISALLOW;\n    }\n    ', ))
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

            # <Interpolation value=<Substitution '\n    switch (FEAT_INDUSTRIES, SELF, ${location_check.switch_entry_point}, current_year) {\n        0..1869:    ${industry.id}_windmill_layout_only;\n        1870..1900: ${location_check.switch_result};\n        ${industry.id}_brick_layouts_only;\n    }\n' (110:56)> braces_required=True translation=False at 7f7b0e543be0> -> __content_140166518101192
            __token = 5267
            __token = 5300
            __content_140166518101192 = _lookup_attr(getitem('location_check'), 'switch_entry_point')
            __content_140166518101192 = __quote(__content_140166518101192, '\x00', '&#0;', None, False)
            __token = 5374
            __content_140166518101192_5372 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_5372 = __quote(__content_140166518101192_5372, '\x00', '&#0;', None, False)
            __token = 5431
            __content_140166518101192_5429 = _lookup_attr(getitem('location_check'), 'switch_result')
            __content_140166518101192_5429 = __quote(__content_140166518101192_5429, '\x00', '&#0;', None, False)
            __token = 5472
            __content_140166518101192_5470 = _lookup_attr(getitem('industry'), 'id')
            __content_140166518101192_5470 = __quote(__content_140166518101192_5470, '\x00', '&#0;', None, False)
            __content_140166518101192 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_INDUSTRIES, SELF, ', (__content_140166518101192 if (__content_140166518101192 is not None) else ''), ', current_year) {\n        0..1869:    ', (__content_140166518101192_5372 if (__content_140166518101192_5372 is not None) else ''), '_windmill_layout_only;\n        1870..1900: ', (__content_140166518101192_5429 if (__content_140166518101192_5429 is not None) else ''), ';\n        ', (__content_140166518101192_5470 if (__content_140166518101192_5470 is not None) else ''), '_brick_layouts_only;\n    }\n', ))
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
            __append('\n\n')
            __token = None
            render_render_tree(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __append('\n\n')
            __token = None
            render_coast_distance(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_check_industry_min_distance(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_check_industry_max_distance(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_cluster(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_town_industry_count(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_check_founder(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n')
            __token = None
            render_flour_mill_layouts_by_date(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_render_tree': render_render_tree, 'render_coast_distance': render_coast_distance, 'render_check_industry_min_distance': render_check_industry_min_distance, 'render_check_industry_max_distance': render_check_industry_max_distance, 'render_cluster': render_cluster, 'render_town_industry_count': render_town_industry_count, 'render_check_founder': render_check_founder, 'render_flour_mill_layouts_by_date': render_flour_mill_layouts_by_date, 'render': render, }