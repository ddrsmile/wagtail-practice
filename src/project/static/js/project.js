$(document).ready(function(){
    $('.navbar-table td a').hover(function () {
        $(this).parent().toggleClass('td-hover');
    });
});