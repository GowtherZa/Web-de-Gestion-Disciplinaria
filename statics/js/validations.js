function validate(event){
    let form = document.getElementById("form")

    let inputs = [...form.querySelectorAll("*[data-rules]")]

    inputs.map((input)=>{

        console.log(input.id)

        if ( Iodine.is(input.value,JSON.parse(input.dataset.rules)) !== true){
            event.preventDefault()
            input.classList.add("is-danger")

            let error = document.getElementById(`${input.id}_error`)
            console.log(error)
            error.classList.remove("error_hidden")
        }
        else{
            input.classList.remove("is-danger")
            let error = document.getElementById(`${input.id}_error`)
            error.classList.add("error_hidden")
        }
    })
}