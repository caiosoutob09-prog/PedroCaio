$(document).ready(function () {

    $(".amigos").hide();

    $("#btnjogos").click(function () {

        $(".jogos").show();
        $(".amigos").hide();

        $("#btnjogos").addClass("active");
        $("#btnamigos").removeClass("active");

    });
    $("#btnamigos").click(function () {

        $(".amigos").show();
        $(".jogos").hide();

        $("#btnamigos").addClass("active");
        $("#btnjogos").removeClass("active");
    });
});