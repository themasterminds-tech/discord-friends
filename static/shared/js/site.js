$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();

    $(".nav-tabs a").click(function () {
        $(this).tab('show');
    })
});