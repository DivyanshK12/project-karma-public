let storageRef = firebase.storage().ref();
// let test = storage.ref("WikiFirebase.png").getDownloadURL();
// document.querySelector('img').src = test;
let username = sessionStorage.getItem("username");
let filename = document.getElementById("filename").innerText;
storageRef
  .child(username + "/" + filename)
  .getDownloadURL()
  .then((url) => {
    // `url` is the download URL for 'images/stars.jpg'
    // Or inserted into an <img> element
    let img = document.getElementById("myimg");
    img.setAttribute("src", url);
  })
  .catch((error) => {
    // Handle any errors
    console.log(error);
  });

// match /users/{userId}/profilePicture.png {
//     allow read;
//     allow write: if request.auth.uid == userId;
//   }// Only a user can upload their profile picture, but anyone can view it
