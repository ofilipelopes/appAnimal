async function buscar() {
    const response = await axios.get('http://localhost:8000/animais')

    const animais = response.data

    const id_animal = document.getElementById('id')

    const form_mostrar = document.getElementById('mostrar-animal')

    form_mostrar.onsubmit = async (event) => {
        event.preventDefault()
        let encontrado = false
        
        for (let animal of animais)
        {
            if (animal.id == id_animal.value) {
                encontrado = true
                window.location.href = `http://127.0.0.1:8000/animais/${id_animal.value}`
                break
            }
        }
        if (encontrado == false) {
            alert('ID não encontrado')
        }
    }
}


function app() {
    console.log('Mostrar animal iniciado')
    buscar()
}


app()
