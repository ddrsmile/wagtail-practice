from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import hooks
from django.contrib.staticfiles.templatetags.staticfiles import static

@hooks.register('insert_editor_js')
def codemirror_mode_js():
    js = [
        static('parts/codemirror/lib/codemirror.js'),
        static('parts/codemirror/lib/utils.js'),
        static('parts/codemirror/mode/python.js'),
        static('parts/codemirror/mode/clike.js'),
        static('parts/codemirror/mode/javascript.js'),
        static('parts/codemirror/mode/css.js'),
        static('parts/codemirror/mode/shell.js'),
    ]

    js_includes = '\n'.join(['\n<script type="text/javascript" src="{filename}"></script>'.format(filename=filename) for filename in js])
    return js_includes

@hooks.register('insert_editor_css')
def codemirror_style_css():
    css = [
        static('parts/codemirror/lib/codemirror.css'),
        static('parts/codemirror/theme/solarized.css'),
    ]

    css_includes = '\n'.join(['\n<link type="text/css" rel="stylesheet" href="{filename}">'.format(filename=filename) for filename in css])
    return css_includes