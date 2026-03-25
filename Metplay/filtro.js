$(document).ready(function () {

    $("#btnação").click(function () {

        $(".Ação").show();
        $(".Terror").hide();
        $(".Aventura").hide();
        $(".Esporte").hide();
        $(".RPG").hide();

    });
     $("#btnaventura").click(function () {

        $(".Aventura").show();
        $(".Terror").hide();
        $(".Ação").hide();
        $(".Esporte").hide();
        $(".RPG").hide();

    });
     $("#btnesp").click(function () {

        $(".Esporte").show();
        $(".Terror").hide();
        $(".Aventura").hide();
        $(".Ação").hide();
        $(".RPG").hide();

    });
     $("#btnrpg").click(function () {

        $(".RPG").show();
        $(".Terror").hide();
        $(".Aventura").hide();
        $(".Esporte").hide();
        $(".Ação").hide();

    });
});