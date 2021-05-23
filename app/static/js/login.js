document.getElementById("submitbtn").onclick = login;

function login() {
  let myForm = document.getElementById("login_form");
  let formData = new FormData(myForm);
  const email = formData.get("email");
  const password = formData.get("password");
  firebase
    .auth()
    .signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      let user = userCredential.user;
      getdata("true", user.uid).then((state) => {
        if (state) {
          location.href = "/home";
        }
      });
    })
    .catch((error) => {
      let errorCode = error.code;
      let errorMessage = error.message;
      console.log(errorMessage, errorCode);
      alert("Login Failed");
    });
}

async function getdata(state, uid) {
  if (state == "true") {
    let response = await fetch(`${location.origin}/api/getuser?uid=${uid}`, {
      method: "POST",
    });
    if (response.status === 200) {
      console.log("Successful");
      return true;
    } else {
      throw new Error("Failed to get username from database");
    }
  }
}
