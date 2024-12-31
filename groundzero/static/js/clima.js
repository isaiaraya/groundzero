let key = '21988eae753990fcccf5164f7511ca1c'
let ciudad = document.getElementById('city');
let resultado = document.getElementById('resultado');
let boton= document.getElementById('btnclima');

let get_clima = () => {
    let city_name = ciudad.value;
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&lang=es&appid=${key}&units=metric`
    fetch(url).then((resp) => resp.json()).then(data => {
        console.log("la temperatua es :" + (data.main.temp)+'º');
        
        console.log(data);
        resultado.innerHTML = `<h4> El clima de ${data.name} es de ${data.main.temp}°C y esta con el  ${data.weather[0].description}</h4>`
    });
}
boton.addEventListener('click', get_clima);