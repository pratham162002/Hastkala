const slides = document.querySelectorAll(".slide");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");
let currentSlide = 0;

// Function to show the current slide
function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove("active");
    if (i === index) {
      slide.classList.add("active");
    }
  });
}

// Show the first slide initially
showSlide(currentSlide);

// Next Button
nextBtn.addEventListener("click", () => {
  currentSlide = (currentSlide +1) % slides.length;
  showSlide(currentSlide);
});

// Previous Button
prevBtn.addEventListener("click", () => {
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  showSlide(currentSlide);
});


// -------------------------------------------
// -=--------------------------------------------
