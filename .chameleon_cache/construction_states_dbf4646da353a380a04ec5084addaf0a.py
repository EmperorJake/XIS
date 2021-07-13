# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/XIS/src/templates/construction_states.pynml'
__tokens = {}

from sys import exc_info as _exc_info

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
            __append('/* *******************************************************\n * Construction states shared by many (not all) industries\n * *******************************************************/\n\n')
            __append('\nspriteset(spriteset_default_construction_states) {\n\ttmpl_building_sprite_filename(10, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(80, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(150, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(220, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(290, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(360, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(430, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(500, 10, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(10, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(80, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(150, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(220, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(290, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(360, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(430, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n\ttmpl_building_sprite_filename(500, 100, 64, -33, "src/graphics/other/default_construction_states.png")\n}\n\nspritelayout spritelayout_default_construction_states {\n\tground {\n\t\tsprite: spriteset_default_construction_states(random_bits % 16);\n\t\trecolour_mode: RECOLOUR_REMAP;\n\t\tpalette: 0;\n\t}\n}\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }