document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los elementos de las tarjetas
    const cards = document.querySelectorAll(".card");

    // Obtener el elemento select del filtro por precio
    const priceFilter = document.getElementById("price-filter");

    // Escuchar el cambio en el filtro
    priceFilter.addEventListener("change", function() {
        const selectedPrice = parseInt(this.value); // Obtener el valor seleccionado y convertirlo a número

        // Iterar sobre cada tarjeta
        cards.forEach(card => {
            const cardPriceText = card.querySelector(".card-price").textContent; // Obtener el precio de la tarjeta como texto
            const cardPrice = parseFloat(cardPriceText.replace(/[^\d.-]/g, '')); // Convertir el precio a número eliminando comas

            // Mostrar u ocultar la tarjeta según el filtro de precio
            if (selectedPrice === 0) {
                card.style.display = "block"; // Mostrar todas las tarjetas si se selecciona "All"
            } else if (selectedPrice === 1 && cardPrice >= 100000) {
                card.style.display = "inline-block"; // Mostrar las tarjetas con precio mayor o igual a $100,000
            } else if (selectedPrice === 2 && cardPrice < 100000) {
                card.style.display = "block"; // Mostrar las tarjetas con precio menor a $100,000
            } else {
                card.style.display = "none"; // Ocultar las tarjetas que no cumplen con el filtro
            }
        });
    });
});