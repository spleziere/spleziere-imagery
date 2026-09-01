const images = [
  "images/photography/photo-01-01.jpg",
  "images/photography/photo-04-04.jpg",
  "images/photography/photo-06.jpg",
  "images/photography/photo-08.jpg",
  "images/photography/photo-09.jpg",
  "images/photography/photo-11.jpg",
  "images/photography/photo-12-01.jpg",
  "images/photography/photo-13-01.jpg",
  "images/photography/photo-15-01.jpg",
  "images/photography/photo-19-03.jpg"
];

const img = document.getElementById("introImage");
if(img){

  img.src = images[Math.floor(Math.random() * images.length)];
}
