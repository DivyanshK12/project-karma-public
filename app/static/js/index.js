window.onload = async function () {
  getposts().then((dat) => putposts(dat));
};

async function getposts() {
  let lastviewed = 0;
  if (localStorage.getItem("lastviewed") == null) {
    localStorage.setItem("lastviewed", 0);
  } else {
    lastviewed = parseInt(localStorage.getItem("lastviewed"));
  }
  let response = await fetch(
    `${location.origin}/api/getposts?lastviewed=${lastviewed}`
  );
  if (response.status === 200) {
    let data = await response.json();
    localStorage.setItem("lastviewed", data[0].id - 1);
    return data;
  }
}
