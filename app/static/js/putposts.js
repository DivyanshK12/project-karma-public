let storageRef = firebase.storage().ref();

function putposts(data) {
  let mainPage = document.getElementById("main-page");
  let row = document.createElement("div");
  row.classList.add("row", "row-cols-2", "my-5");
  for (let i = 0; i < data.length; i++) {
    // dynamically put posts
    // need to use lazy loading on images
    let col = document.createElement("div");
    col.classList.add(
      "col-4",
      "border",
      "d-flex",
      "justify-content-md-center",
      "align-items-center"
    );
    let img = document.createElement("img");
    img.style.maxHeight = "40vh";
    img.classList.add("img-fluid");
    storageRef
      .child(data[i].post_path)
      .getDownloadURL()
      .then((url) => {
        img.setAttribute("src", url);
      })
      .catch((error) => {
        // Handle any errors
        console.log(error);
      });
    let a = document.createElement("a"); // anchor tag that surrounds the image
    a.href = "/" + data[i].poster_name + "/" + data[i].id;
    a.appendChild(img);
    col.appendChild(a);
    row.appendChild(col);
    // can modify element here
  }
  mainPage.appendChild(row);
}
