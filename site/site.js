$(document).ready(function () {


    Swal.fire({
        title: "Good job!",
        text: "You clicked the button!",
        icon: "success"
    });

    $("#btninfo").click(function () {

        $("#titulo_info").hide();
        $("#titulo_danger").show();



    });

    $("#btndanger").click(function () {

        $("#titulo_info").show();
        $("#titulo_danger").hide();



    });

});
