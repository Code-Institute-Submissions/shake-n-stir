/* --Bootstrap form validation-- */

(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.getElementsByClassName('needs-validation');

    // Loop over them and prevent submission
    let validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

$('#password, #confirm_password').on('keyup', function () {
  if ($('#password').val() == $('#confirm_password').val()) {
    $('#confirm_password').addClass("is-valid").removeClass("is-invalid");
  
  } else 
      $('#confirm_password').removeClass("is-valid").addClass("is-invalid");
});

//Cloudinary widget 
const myWidget = cloudinary.createUploadWidget({
  cloudName: 'dx82dshakenstir', 
  uploadPreset: 'yxesuzpw',
  sources: [ 'local', 'url']},
  (error, result) => {//This is the callback to access the link from cloudinary.
      if (!error && result && result.event === "success") { 
        console.log('Done! Here is the image info: ', result.info.secure_url); 
        document.getElementById("cocktail_img").value = result.info.secure_url;
      }
  }
);

//Link button to cloudinary widget
const img_upload_btn = document.getElementById("img_upload_btn");
if (img_upload_btn) {
  img_upload_btn.addEventListener("click", function () {
      myWidget.open();
  }, false
  );
}