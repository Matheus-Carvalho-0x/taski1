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
});

function createItem(id, text) {
  const container = document.createElement("div");

  const p = document.createElement("p");
  p.textContent = text;

  const btnDelete = document.createElement("button");
  btnDelete.textContent = "Delete";

  container.appendChild(p);
  container.appendChild(btnDelete);

  btnDelete.addEventListener("click", async () => {
    const request = await fetch("http://127.0.0.1:8000/delete", {
      method: "DELETE",
      body: JSON.stringify({ Content: id }),
    });
  });

  return container;
}

async function list() {
  try {
    const request = await fetch("http://127.0.0.1:8000/data");
    const response = await request.json();

    tasklist.innerHTML = "";

    const data = Object.values(response);
    for (let i = 0; i < data.length; i++) {
      const container = createItem(data[i].id, data[i].task);
      tasklist.appendChild(container);
    }
  } catch (e) {
    tasklist.textContent = "Unable to load content!";
  }
}

list();
