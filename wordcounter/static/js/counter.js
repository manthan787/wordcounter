$(document).ready(function () {
    console.log("Attaching handler!");
    $("#text").keyup(function () {
        var data = $('#text').val();
        $.post('/wordcounter', { text: data }, function (result) {
            $("#count").val(result);
        })
    })
})