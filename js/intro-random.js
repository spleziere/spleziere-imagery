const images = [
  "images/photography/web/photo-01-01.webp",
  "images/photography/web/photo-04-04.webp",
  "images/photography/photo-06.jpg",
  "images/photography/photo-08.jpg",
  "images/photography/photo-09.jpg",
  "images/photography/photo-11.jpg",
  "images/photography/web/photo-12-01.webp",
  "images/photography/web/photo-13-01.webp",
  "images/photography/web/photo-15-01.webp",
  "images/photography/web/photo-19-03.webp"
];

const img = document.getElementById("introImage");
if(img){

  img.src = images[Math.floor(Math.random() * images.length)];
}
