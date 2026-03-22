

const carousel = document.getElementById('carouselExampleAutoplaying');

carousel.addEventListener('slid.bs.carousel', function (event) {
    const i = event.to;

    if (i == 0) {
        document.getElementById("cardTitle").innerText = "Outono Chegou!";
        document.getElementById("cardText").innerText = "Descontos de até 70% em jogos incríveis. Corre que é por tempo limitado!";
        document.getElementById("cardImg").src = "capaoutono.png";
    }
    if (i == 1) {
        document.getElementById("cardTitle").innerText = "Forza Horizon 5";
        document.getElementById("cardText").innerText = "Explore as paisagens vibrantes de mundo aberto do México com diversão e velocidade sem limites com os melhores carros do mundo.";
        document.getElementById("cardImg").src = "capa1.jpg";
    }
    if (i == 2) {
        document.getElementById("cardTitle").innerText = "Resident Evil: Requiem";
        document.getElementById("cardText").innerText = "Réquiem para os mortos. Pesadelo para os vivos. Prepare-se para escapar da morte em uma experiência arrepiante e de tirar o fôlego.";
        document.getElementById("cardImg").src = "capa2.jpg";
    }
    if (i == 3) {
        document.getElementById("cardTitle").innerText = "The Elder Scrolls V: Skyrim";
        document.getElementById("cardText").innerText = "Vencedor de mais de 200 prêmios de Jogo do Ano, The Elder Scrolls V: Skyrim Special Edition traz vida à fantasia épica com detalhes deslumbrantes.";
        document.getElementById("cardImg").src = "capa3.jpg";
    }

});