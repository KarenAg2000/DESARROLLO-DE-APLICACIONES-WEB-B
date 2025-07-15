// Mostrar alerta personalizada
function mostrarAlerta() {
  alert("¡Gracias por visitar MG Electrónica!");
}

// Validación de formulario
document.addEventListener('DOMContentLoaded', () => {
  const formulario = document.getElementById('formularioContacto');

  formulario.addEventListener('submit', function (e) {
    e.preventDefault();

    let valido = true;

    // Validar nombre
    const nombre = document.getElementById('nombre');
    if (nombre.value.trim() === '') {
      nombre.classList.add('is-invalid');
      valido = false;
    } else {
      nombre.classList.remove('is-invalid');
    }

    // Validar email
    const email = document.getElementById('email');
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email.value)) {
      email.classList.add('is-invalid');
      valido = false;
    } else {
      email.classList.remove('is-invalid');
    }

    // Validar mensaje
    const mensaje = document.getElementById('mensaje');
    if (mensaje.value.trim() === '') {
      mensaje.classList.add('is-invalid');
      valido = false;
    } else {
      mensaje.classList.remove('is-invalid');
    }

    // Si es válido, mostrar mensaje
    if (valido) {
      alert("Formulario enviado correctamente 🎉");
      formulario.reset();
    }
  });
});