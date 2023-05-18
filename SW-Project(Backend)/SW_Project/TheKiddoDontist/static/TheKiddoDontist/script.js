
var images = [
  "{% static 'TheKiddoDontist/best-pediatric-dentist.jpg' %}",
  "{% static 'TheKiddoDontist/Back-to-School-Dental-Checkup-Pleasant-St-Dental-East-Longmeadow-Ma-e1597064370762.jpg' %}",
  "{% static 'TheKiddoDontist/back3 (2).jpg' %}"
  ];
  
  var currentIndex = 0;
  var slideshowElement = document.getElementById("slideshow");
  
  function showImage(index) {
    var image = document.createElement("img");
    image.src = images[index];
    image.onload = function() {
      slideshowElement.appendChild(image);
      setTimeout(function() {
        image.style.opacity = 1;
      }, 100);
    };
  }
  
  function hideImage(image) {
    setTimeout(function() {
      image.style.opacity = 0;
      setTimeout(function() {
        slideshowElement.removeChild(image);
      }, 1000);
    }, 5000);
  }
  
  showImage(currentIndex);
  
  setInterval(function() {
    var image = slideshowElement.querySelector("img");
    currentIndex = (currentIndex + 1) % images.length;
    var nextImage = document.createElement("img");
    nextImage.src = images[currentIndex];
    nextImage.onload = function() {
      slideshowElement.appendChild(nextImage);
      setTimeout(function() {
        image.style.opacity = 0;
        nextImage.style.opacity = 1;
        setTimeout(function() {
          slideshowElement.removeChild(image);
        }, 1000);
      }, 100);
    };
  }, 5000);
  