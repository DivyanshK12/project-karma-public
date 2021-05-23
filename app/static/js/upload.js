document.getElementById("upload").onchange = function () {
  let src = URL.createObjectURL(this.files[0]);
  let name = this.files[0].name;
  document.getElementById("label_img").innerText = name;
  document.getElementById("image").src = src;
};
