/* Project specific Javascript goes here. */
let botonAgregarRedSocial = document.querySelector(".agregar-red-proveedor");
botonAgregarRedSocial.addEventListener("click", () => {
  let contenedor = document.querySelector("#red-social-proveedor");
  let lastLine = document.querySelector("#red-social-proveedor .last-line");
  lastLine.classList.remove("last-line");
  botonAgregarRedSocial.classList.remove("agregar-red-proveedor");
  botonAgregarRedSocial.classList.remove("btn-primary");
  botonAgregarRedSocial.classList.add("btn-danger");
  botonAgregarRedSocial.innerText = "Eliminar";

  console.log(contenedor);
  console.log(lastLine);
  let newContent = document.createElement("div");
  newContent.classList.add("mb-3");
  newContent.innerHTML = `<div class="one_line_flex last-line">
  <input
    type="text"
    class="form-control"
    id="red_social"
    placeholder="Red social"
    value=""
  />
  <input
    type="text"
    class="form-control need_margin_lef"
    id="red_social_cuenta"
    placeholder="Cuenta"
    value=""
  />
  <div
    class="d-grid gap-2 d-md-flex justify-content-md-end need_margin_lef"
  >
    <button
      class="btn btn-primary me-md-2 agregar-red-proveedor"
      type="button"
    >
      Nueva
    </button>
  </div>
</div>`;
  console.log(newContent);

  contenedor.appendChild(newContent);
});
