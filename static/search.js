var searchForm = document.getElementById("searchForm");
searchForm.onsubmit = function() {
  var latInput = document.getElementById("latInput");
  var longInput = document.getElementById("longInput");

  function getCurrentLocation() {
    navigator.geolocation.getCurrentPosition(setPosition);
  }

  function setPosition(position) {
    latInput.value = position.coords.latitude;
    longInput.value = position.coords.longitude;
  }
}
