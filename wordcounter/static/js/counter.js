$(document).ready(function () {
    console.log("Attaching handler!");
    $("#text").keyup(function () {
        var data = $('#text').val();
        $.post('/wordcounter', { text: data }, function (result) {
            $("#count").val(result);
        })
    })

    $("#text").keyup(function() {
        var data = $('#text').val().trim();
        $('#charcount').html(data.length + " / 50");
        if (data.length > 50) {
            $('#text').val(data.substr(0, 50));
            // alert("You have exceeded the character limit of 50");
        }
    })
})