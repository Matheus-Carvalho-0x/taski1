const tasklist = document.getElementById("tasklist");
const input = document.getElementById("input");
const savebutton = document.getElementById("save");

savebutton.addEventListener("click", async () => {
  const request = await fetch("http://127.0.0.1:8000/insert", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ Content: input.value }),
  });
  const response = await request.json();
  console.log(response);
});
