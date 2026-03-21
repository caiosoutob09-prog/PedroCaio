window.onload = function () {
  const carousel = document.getElementById('carouselExampleAutoplaying');

  console.log("carousel:", carousel);

  carousel.addEventListener('slide.bs.carousel', function () {
    console.log("ANTES 🔥");
  });

  carousel.addEventListener('slid.bs.carousel', function () {
    console.log("DEPOIS 🔥");
  });
};