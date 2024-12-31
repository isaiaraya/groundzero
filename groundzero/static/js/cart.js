// Array para almacenar los productos del carrito
let cart = [];

// Función para cargar el carrito desde localStorage
function loadCart() {
  const storedCart = localStorage.getItem('cart');
  if (storedCart) {
    cart = JSON.parse(storedCart);
  }
  updateCartDisplay();
  updateCartTotal(); // Llamar a la función para actualizar el total del carrito
}

// Función para guardar el carrito en localStorage
function saveCart() {
  localStorage.setItem('cart', JSON.stringify(cart));
}

// Función para agregar un producto al carrito
function addToCart(product) {
  cart.push(product);
  saveCart();
  updateCartDisplay();
  updateCartTotal(); // Llamar a la función para actualizar el total del carrito
}

// Función para actualizar la visualización del carrito
function updateCartDisplay() {
  const cartItemsContainer = document.getElementById('cart-items');
  const cartCountElement = document.getElementById('cart-count');

  cartItemsContainer.innerHTML = '';

  cart.forEach((product, index) => {
    const productElement = document.createElement('div');
    productElement.className = 'cart-item';
    productElement.innerHTML = `
      <div class="d-flex justify-content-between align-items-center">
        <div>
          <img src="${product.image}" alt="${product.title}" style="width: 50px; height: 50px; object-fit: cover;">
        </div>
        <div>
          <h6>${product.title}</h6>
          <p>${formatPrice(product.price)}</p>
        </div>
        <button class="btn btn-danger btn-sm remove-from-cart" data-index="${index}">Eliminar</button>
      </div>
    `;
    cartItemsContainer.appendChild(productElement);
  });

  cartCountElement.textContent = cart.length;

  document.querySelectorAll('.remove-from-cart').forEach(button => {
    button.addEventListener('click', (event) => {
      const index = event.target.dataset.index;
      removeFromCart(index);
    });
  });
}

// Función para actualizar el total del carrito
function updateCartTotal() {
  const cartTotalElement = document.getElementById('cart-total');
  let total = 0;

  cart.forEach(product => {
    total += product.price; // Sumar el precio numérico al total
  });

  // Formatear el total con separador de miles y símbolo $
  const formattedTotal = formatPrice(total);

  cartTotalElement.textContent = formattedTotal;
}

// Función para eliminar un producto del carrito
function removeFromCart(index) {
  cart.splice(index, 1);
  saveCart();
  updateCartDisplay();
  updateCartTotal(); // Llamar a la función para actualizar el total del carrito
}

// Función para formatear el precio con separador de miles y símbolo $
function formatPrice(price) {
  return price.toLocaleString('es-CL', {
    style: 'currency',
    currency: 'CLP'
  });
}

// Añadir eventos de clic a los botones "Agregar al carrito"
document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', (event) => {
    const card = event.target.closest('.card');
    const title = card.querySelector('.card-title').innerText;
    const priceText = card.querySelector('.card-price').innerText.trim(); // Obtener el texto del precio y eliminar espacios adicionales
    const numericPrice = parseInt(priceText.replace(/\D/g, '')); // Extraer solo los dígitos numéricos

    const image = card.querySelector('.card-img-top').src;

    const product = {
      title: title,
      price: numericPrice,
      image: image
    };

    addToCart(product);
  });
});

// Evento para el botón de finalizar compra (checkout)
document.getElementById('checkout-button').addEventListener('click', () => {
  alert('Compra finalizada!');
  cart = [];
  saveCart();
  updateCartDisplay();
  updateCartTotal(); // Llamar a la función para actualizar el total del carrito
});

// Cargar el carrito al cargar la página
document.addEventListener('DOMContentLoaded', loadCart);