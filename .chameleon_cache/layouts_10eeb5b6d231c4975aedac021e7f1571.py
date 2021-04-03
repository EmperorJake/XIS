# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/layouts.pynml'
__tokens = {658: ('python:industry.industry_layouts', 8, 64), 697: ('tilelayout ${industry_layout.id}_tilelayout {', 9, 4), 710: ('industry_layout.id', 9, 17), 793: ('industry_layout.layout', 10, 50), 830: ('${layout[0]}, ${layout[1]}: ${layout[2]};', 11, 12), 832: ('layout[0]', 11, 14), 846: ('layout[1]', 11, 28), 860: ('layout[2]', 11, 42)}

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
            __backup_industry_layout_140383635219232 = get('industry_layout', __marker)

            # <Value 'python:industry.industry_layouts' (8:64)> -> __iterator
            __token = 658
            __iterator = _lookup_attr(getitem('industry'), 'industry_layouts')
            (__iterator, ____index_140383636839728, ) = getitem('repeat')('industry_layout', __iterator)
            econtext['industry_layout'] = None
            for __item in __iterator:
                econtext['industry_layout'] = __item

                # <Interpolation value=<Substitution '\n    tilelayout ${industry_layout.id}_tilelayout {\n        ' (8:98)> braces_required=True translation=False at 7fad9cce5e80> -> __content_140383655711776
                __token = 697
                __token = 710
                __content_140383655711776 = _lookup_attr(getitem('industry_layout'), 'id')
                __content_140383655711776 = __quote(__content_140383655711776, '\x00', '&#0;', None, False)
                __content_140383655711776 = ('%s%s%s' % ('\n    tilelayout ', (__content_140383655711776 if (__content_140383655711776 is not None) else ''), '_tilelayout {\n        ', ))
                if (__content_140383655711776 is None):
                    pass
                else:
                    if (__content_140383655711776 is False):
                        __content_140383655711776 = None
                    else:
                        __tt = type(__content_140383655711776)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140383655711776 = str(__content_140383655711776)
                        else:
                            if (__tt is bytes):
                                __content_140383655711776 = decode(__content_140383655711776)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140383655711776 = __content_140383655711776.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140383655711776)
                                        __content_140383655711776 = (str(__content_140383655711776) if (__content_140383655711776 is __converted) else __converted)
                                    else:
                                        __content_140383655711776 = __content_140383655711776()
                if (__content_140383655711776 is not None):
                    __append(__content_140383655711776)
                __backup_layout_140383635192464 = get('layout', __marker)

                # <Value 'industry_layout.layout' (10:50)> -> __iterator
                __token = 793
                __iterator = _lookup_attr(getitem('industry_layout'), 'layout')
                (__iterator, ____index_140383636837488, ) = getitem('repeat')('layout', __iterator)
                econtext['layout'] = None
                for __item in __iterator:
                    econtext['layout'] = __item

                    # <Interpolation value=<Substitution '\n            ${layout[0]}, ${layout[1]}: ${layout[2]};\n        ' (10:74)> braces_required=True translation=False at 7fad9cce5a58> -> __content_140383655711776
                    __token = 830
                    __token = 832
                    __content_140383655711776 = getitem('layout')[0]
                    __content_140383655711776 = __quote(__content_140383655711776, '\x00', '&#0;', None, False)
                    __token = 846
                    __content_140383655711776_844 = getitem('layout')[1]
                    __content_140383655711776_844 = __quote(__content_140383655711776_844, '\x00', '&#0;', None, False)
                    __token = 860
                    __content_140383655711776_858 = getitem('layout')[2]
                    __content_140383655711776_858 = __quote(__content_140383655711776_858, '\x00', '&#0;', None, False)
                    __content_140383655711776 = ('%s%s%s%s%s%s%s' % ('\n            ', (__content_140383655711776 if (__content_140383655711776 is not None) else ''), ', ', (__content_140383655711776_844 if (__content_140383655711776_844 is not None) else ''), ': ', (__content_140383655711776_858 if (__content_140383655711776_858 is not None) else ''), ';\n        ', ))
                    if (__content_140383655711776 is None):
                        pass
                    else:
                        if (__content_140383655711776 is False):
                            __content_140383655711776 = None
                        else:
                            __tt = type(__content_140383655711776)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140383655711776 = str(__content_140383655711776)
                            else:
                                if (__tt is bytes):
                                    __content_140383655711776 = decode(__content_140383655711776)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140383655711776 = __content_140383655711776.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140383655711776)
                                            __content_140383655711776 = (str(__content_140383655711776) if (__content_140383655711776 is __converted) else __converted)
                                        else:
                                            __content_140383655711776 = __content_140383655711776()
                    if (__content_140383655711776 is not None):
                        __append(__content_140383655711776)
                    ____index_140383636837488 -= 1
                    if (____index_140383636837488 > 0):
                        __append('')
                if (__backup_layout_140383635192464 is __marker):
                    del econtext['layout']
                else:
                    econtext['layout'] = __backup_layout_140383635192464
                __append('\n    }\n')
                ____index_140383636839728 -= 1
                if (____index_140383636839728 > 0):
                    __append('')
            if (__backup_industry_layout_140383635219232 is __marker):
                del econtext['industry_layout']
            else:
                econtext['industry_layout'] = __backup_industry_layout_140383635219232
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }