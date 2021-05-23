// That form submits and stores data on forebase and refreshes the page
document.getElementById("submitbtn").onclick = getcomment;
let database = firebase.database();
let postdata;

window.onload = function () {
  load_image()
    .then((data) => (postdata = data))
    .then(() => load_comments(postdata))
    .then(() => load_caption(postdata));
};

async function getcomment() {
  let commentForm = document.getElementById("comment_form");
  let formData = new FormData(commentForm);
  let comment = formData.get("comment");
  commentForm.reset();
  let item = document.createElement("li");
  item.classList.add(
    "list-group-item",
    "text-white",
    "fw-bold",
    "d-flex",
    "justify-content-between",
    "align-items-center"
  );

  let response = await fetch(`${location.origin}/api/karma?text=${comment}`);
  if (response.status === 200) {
    let data = await response.json();
    item.style.background = data.color;
    let newCommentKey = database
      .ref(postdata.post_path)
      .child("comments")
      .push().key;
    let updates = {};
    updates[`/comments/${newCommentKey}`] = {
      color: data.color,
      comment: comment,
      commenter: data.sender,
    };
    database.ref(postdata.post_path).update(updates);
  }
  // will already be stored for next use, hence can use the data received here as well
  item.innerText = comment;
  let commentList = document.getElementById("comment-bar");
  commentList.append(item);
}

async function load_image() {
  let address = location.href.split("/");
  let imgId = address.pop();
  let img = document.getElementById("main-img");
  let response = await fetch(`${location.origin}/api/getimage?id=${imgId}`);
  let storageRef = firebase.storage().ref();
  if (response.status === 200) {
    let data = await response.json();
    storageRef
      .child(data.post_path)
      .getDownloadURL()
      .then((url) => {
        img.setAttribute("src", url);
      })
      .catch((error) => {
        // Handle any errors
        console.log(error);
      });
    return data;
  }
}

function load_comments(data) {
  let commentList = document.getElementById("comment-bar");
  database
    .ref(data.post_path + "/comments")
    .get()
    .then(function (snapshot) {
      if (snapshot.exists()) {
        let comments = snapshot.val();
        for (let item in comments) {
          let comment = document.createElement("li");
          comment.classList.add(
            "list-group-item",
            "text-white",
            "fw-bold",
            "d-flex",
            "justify-content-between",
            "align-items-center"
          );
          comment.style.background = comments[item].color;
          comment.innerText = comments[item].comment;

          let commenter = document.createElement("span");
          commenter.classList.add("badge", "bg-dark", "float-end");
          commenter.innerText = comments[item].commenter;
          comment.appendChild(commenter);
          commentList.appendChild(comment);
        }
      } else {
        console.log("No data available");
      }
    })
    .catch(function (error) {
      console.error(error);
    });
}

function load_caption(data) {
  let cap = document.getElementById("cap");
  database
    .ref(data.post_path + "/caption")
    .get()
    .then(function (snapshot) {
      if (snapshot.exists()) {
        let caption = snapshot.val();
        cap.innerText = caption;
      } else {
        console.log("No caption available");
      }
    })
    .catch(function (error) {
      console.error(error);
    });
}
