$(document).ready(function () {

    $("#btnCalcular").click(function () {

        let quantidade = parseFloat($("#quantidade_filmes").val());

        let horas = quantidade * 2;

        $("#resultado").val(horas + " horas assistidas");

    });

});