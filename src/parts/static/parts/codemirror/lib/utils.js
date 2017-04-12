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

function update_code_mode(obj) {
    var choice_id = obj.id;
    var cm_id = choice_id.replace("language", "code");
    if ( window.CodeMirrorInstances != null ) {
        cm = window.CodeMirrorInstances[cm_id];
        cm.setOption("mode", codemapper[obj.value]);
    }
}