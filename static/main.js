buttons = document.getElementsByClassName("signup-button");
for (var i = 0; i < buttons.length; i++) {
  buttons[i].onclick = function() {
    sendSignupRequest(i);
  };
}

function sendSignupRequest(i) {
  var http = new XMLHttpRequest();
  http.open("POST", "/projects/signup/", true);
  var params = "project_id=" + buttons[i].id.substring(7, buttons[i].id.length);
  http.send(params);
}
