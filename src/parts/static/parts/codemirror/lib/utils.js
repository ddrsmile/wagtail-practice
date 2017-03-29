var codemapper = {
    'cpp': 'text/x-c++src',
    'java': 'text/x-java',
    'python': 'python',
    'python3': 'python',
    'bash': 'text/x-sh',
    'html': 'text/html',
    'javascript': 'text/javascript',
    'css': 'text/css',
}

function update_mode(obj) {
    var choice_id = obj.id;
    var id_num = choice_id.split("-")[1]
    var textarea_editor_name = "code_editor_" + id_num.toString();
    var textarea_editor = window[textarea_editor_name];
    textarea_editor.setOption("mode", codemapper[obj.value]);
}