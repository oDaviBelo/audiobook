limit = 200
num_char = document.querySelector('.text_area')
num_char_html = document.querySelector('.num_char')

function limitador(event){
    num_char_html.innerHTML = num_char.value.length+'/200'

}



document.addEventListener('keyup',()=>{
    setTimeout(limitador,0.001)
})
document.addEventListener('keypress',()=>{
    setTimeout(limitador,0.001)
})
document.addEventListener('keyup',()=>{
    if (num_char.value.length>limit){
        console.log('ativou')
        x = []
        for(let i = 0;i<=limit;i++){
            x.push(num_char.value[i])
        }
        while(x.length>limit){
            x.pop()
            
        }
        num_char.value= x.join('')
    }
})

function pt_br(){
    if(window.location.href!='/pt_br'){
        window.location.assign('/pt_br')
    }
}

function en(){
    if(window.location.href!='/en'){
        window.location.assign('/en')
    }
}
document.addEventListener('DOMContentLoaded',()=>{
    if(window.location.href=='http://127.0.0.1:5000/pt_br'){
        about = document.querySelector('.about').innerHTML = 'Sobre'
        contact = document.querySelector('.contact').innerHTML = 'Contato'
        label_main = document.querySelector('.label_main').innerHTML = 'Texto para Áudio (máx: 200 caracteres)'
        submit = document.querySelector('.submit').value = 'Transforme'
    }
})
