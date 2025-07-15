const productos = [
  {
    nombre: "Arreglos de Equipo de Sonido",
    precio: "$50",
    descripcion: "Servicio profesional para reparación y mantenimiento de equipos de sonido.",
    imagen: "Arreglos de Equipo de Sonido.jpeg"
  },
  {
    nombre: "Cambio de Pantalla",
    precio: "$30",
    descripcion: "Reemplazo de pantallas para dispositivos electrónicos.",
    imagen: "Cambio de Pantalla.webp"
  },
  {
    nombre: "Cargadores",
    precio: "$15",
    descripcion: "Venta de cargadores para diversos dispositivos electrónicos.",
    imagen: "Cargadores.jpeg"
  },
  {
    nombre: "Protoboard",
    precio: "$5",
    descripcion: "Tablero para prototipos electrónicos sin soldadura.",
    imagen: "Protoboard.jpg"
  },
  {
    nombre: "Sensor LM35",
    precio: "$7",
    descripcion: "Sensor de temperatura analógico con alta precisión.",
    imagen: "Sensor LM35.jpg"
  }
];

function renderizarProductos() {
  const lista = document.getElementById("productList");
  lista.innerHTML = "";

  productos.forEach(producto => {
    const item = document.createElement("li");
    item.className = "list-group-item d-flex align-items-start";

    const img = producto.imagen
      ? `<img src="${producto.imagen}" class="product-img" alt="${producto.nombre}">`
      : "";

    item.innerHTML = `
      ${img}
      <div>
        <strong>${producto.nombre}</strong> - ${producto.precio}<br>
        <em>${producto.descripcion}</em>
      </div>
    `;
    lista.appendChild(item);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderizarProductos();
});
