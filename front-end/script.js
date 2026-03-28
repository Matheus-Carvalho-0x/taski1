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

async function list() {
  try {
    const request = await fetch("http://127.0.0.1:8000/data");
    const response = await request.json();
    console.log(response);

    tasklist.innerHTML = "";

    const data = Object.values(response);
    for (let i = 0; i < data.length; i++) {
      const p = document.createElement("p");
      p.textContent = data[i].task;
      tasklist.appendChild(p);
    }
  } catch (e) {
    tasklist.textContent = "Unable to load content!";
  }
}

list();
