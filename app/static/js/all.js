window.onload = async function () {
  allposts().then((dat) => putposts(dat));
};

async function allposts() {
  let response = await fetch(`${location.origin}/api/getposts?lastviewed=0`);
  if (response.status === 200) {
    let data = await response.json();
    return data;
  }
}
