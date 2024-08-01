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




