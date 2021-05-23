const ref = firebase.storage().ref();

document.getElementById("submit").onclick = upload_img;

async function upload_img() {
  let file = document.getElementById("upload").files[0];
  let caption = document.getElementById("caption").innerText;
  let filename;
  let response = await fetch(
    `${location.origin}/api/putfile?caption=${caption}`,
    {
      method: "POST",
    }
  );
  if (response.status === 200) {
    let data = await response.json();
    filename = data.path;
  }
  let metadata = {
    contentType: file.type,
  };
  let task = ref.child(filename).put(file, metadata);
  // need to put caption and relative filepath to database too
  task.then(() => location.pathname = '/all').catch(console.error);
}
