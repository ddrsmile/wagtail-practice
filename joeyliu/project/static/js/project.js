$(document).ready(function(){
    $('a').hover(function () {
        $(this).parent().toggleClass('td-hover');
    });
});