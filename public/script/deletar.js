async function deletar() {
    const response = await axios.get('http://localhost:8000/animais')

    const animais = response.data

    const id_animal = document.getElementById('id')

    const form_del = document.getElementById('deletar-animal')

    form_del.onsubmit = async (event) => {
        event.preventDefault()
        let encontrado = false
        
        for (let animal of animais)
        {
            if (animal.id == id_animal.value) {
                await axios.delete(`http://localhost:8000/animais/${id_animal.value}`)
                alert('Animal deletado')
                encontrado = true
                break
            }
        }
        if (encontrado == false) {
            alert('ID não encontrado')
        }
    }
}


function app() {
    console.log('Deletar iniciado')
    deletar()
}


app()
