buttons = document.getElementsByClassName("signup-button");
for (var button in buttons) {
  button.onclick = function() {
    var http = new XMLHttpRequest();
    http.open("POST", "/projects/signup/", true);
    var params = "project_id=" + button.id.substring(7, button.id.length);
    http.send(params);
  }
}
