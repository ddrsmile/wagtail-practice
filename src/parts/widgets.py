from __future__ import absolute_import, unicode_literals
# django
from django.forms import Media, widgets
from django.contrib.staticfiles.templatetags.staticfiles import static
# wagtail
from wagtail.utils.widgets import WidgetWithScript

class CodeTextWidget(WidgetWithScript, widgets.Textarea):
    def render_js_init(self, id_, name, value):
        # default mode is set to python

        jsinit = """
            var code_value_id = "{id!s}"
            var mode_value_id = code_value_id.replace("code", "language");
            var code = document.getElementById(code_value_id);
            var mode = document.getElementById(mode_value_id);

            if (window.CodeMirrorInstances == null) {{
                window.CodeMirrorInstances = {{}};
            }}
            cm = CodeMirror.fromTextArea(
                code,
                {{
                    mode: mode.value,
                    theme: "solarized light",
                    lineNumbers: true,
                    styleActiveLine: true,
                    matchBrackets: true,
                    indentUnit: 4,
                    extraKeys: {{
                        "Tab": function(cm){{
                            cm.replaceSelection("    " , "end");
                        }}
                    }}
                }}
            )
            window.CodeMirrorInstances[code_value_id] = cm;
        """
        return jsinit.format(id=id_)
    
    @property
    def media(self):
        js = [
            static('parts/codemirror/lib/codemirror.js'),
            static('parts/codemirror/lib/utils.js'),
            static('parts/codemirror/mode/python.js'),
            static('parts/codemirror/mode/clike.js'),
            static('parts/codemirror/mode/javascript.js'),
            static('parts/codemirror/mode/css.js'),
            static('parts/codemirror/mode/shell.js'),
        ]
        css = {
            'all': [
                static('parts/codemirror/lib/codemirror.css'),
                static('parts/codemirror/theme/solarized.css'),
        ]}
        return Media(js=js, css=css)

class MarkDownWidget(WidgetWithScript, widgets.Textarea):

    def render_js_init(self, id_, name, value):
        jsinit = """
            if (window.SimpleMDEInstances == null) {{
                window.SimpleMDEInstances = [];
            }}
            sm = new SimpleMDE({{
                element: document.getElementById("{id!s}"),
                forceSync: true,
                spellChecker: false,
                previewRender: latex_support

            }})
            window.SimpleMDEInstances.push(sm);
        """
        return jsinit.format(id=id_)
    
    @property
    def media(self):
        js = [
            static('parts/simplemde/simplemde.min.js'),
            static('parts/simplemde/utils/markdown_latex_support.js'),
        ]
        css = {
            'all': [
                static('parts/simplemde/simplemde.min.css'),
        ]}
        return Media(js=js, css=css)