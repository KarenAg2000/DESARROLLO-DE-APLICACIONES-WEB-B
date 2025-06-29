const imageInput = document.getElementById('imageURL');
const addButton = document.getElementById('addImageBtn');
const removeButton = document.getElementById('removeImageBtn');
const gallery = document.getElementById('gallery');
let selectedImage = null;

addButton.addEventListener('click', () => {
  const url = imageInput.value.trim();
  if (!url) {
    alert('Por favor ingresa una URL válida.');
    return;
  }

  const col = document.createElement('div');
  col.className = 'col';

  const img = document.createElement('img');
  img.src = url;
  img.alt = 'Imagen agregada';
  img.className = 'img-fluid rounded';

  img.addEventListener('click', () => selectImage(img));

  img.style.opacity = 0;
  col.appendChild(img);
  gallery.appendChild(col);

  setTimeout(() => {
    img.style.transition = 'opacity 0.5s';
    img.style.opacity = 1;
  }, 10);

  imageInput.value = '';
});

function selectImage(img) {
  const allImages = gallery.querySelectorAll('img');
  allImages.forEach(im => im.classList.remove('selected'));
  img.classList.add('selected');
  selectedImage = img;
}

removeButton.addEventListener('click', () => {
  if (selectedImage) {
    const colToRemove = selectedImage.parentElement;
    selectedImage = null;
    colToRemove.style.transition = 'opacity 0.4s';
    colToRemove.style.opacity = 0;
    setTimeout(() => colToRemove.remove(), 400);
  } else {
    alert('Selecciona una imagen para eliminar.');
  }
});

imageInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') addButton.click();
});
