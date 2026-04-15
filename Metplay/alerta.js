$(document).ready(function () {

    $("#btndesejo").click(function () { 
        
        Swal.fire({
            title: "Adicionado à lista de desejos!",
            icon: "success",
            draggable: true
        });

    });

});