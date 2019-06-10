buttons = document.getElementsByClassName("signup-button");
for (let i = 0; i < buttons.length; i++) {
  buttons[i].onclick = function() {
    console.log(i);
    console.log(buttons);
    console.log(buttons[i]);
    var http = new XMLHttpRequest();
    http.open("POST", "/projects/signup/", true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    var params = "projectid=" + buttons[i].id.substring(7, buttons[i].id.length);
    http.send(params);
  };
}
