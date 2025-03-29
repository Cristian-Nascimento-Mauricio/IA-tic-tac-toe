
const player = {
    type:'X',
    canIPlay:true
    
}

async function myMove(pos){
    if(!player.canIPlay) return
    
    let element = document.getElementById(`pos${pos.row}-${pos.col}`)

    if (element.getAttribute("data") != "") return

    player.canIPlay = false

    element.textContent = "X"
    element.setAttribute("data","X")

    await delay(100)

    let resul = didAnyoneWin(getBoard());
    
    if (resul) {
        alert("O X venceu!");
        return
    }

    postMove()
    .then(res => {
        if(res.status == 422){
            alert('Tabuleiro cheio')
            error()

        }

        return res.json()
    })
    .then(async data =>{        
        iaMove(data)
        
        await delay(100)

        let resul = didAnyoneWin(getBoard());
        
        if (resul) {
            alert("O O venceu!");
            return
        }
        
        player.canIPlay = true

    })
    .catch((res)=>{
        console.error(res)
        alert("Erro de conexão, renicie o jogo !")

    })

}

function iaMove(pos){

    let element = document.getElementById(`pos${pos.row}-${pos.col}`)

    element.textContent = "O"
    element.setAttribute("data","O")

}

function getBoard(){

    let row = []

    for(let i = 0; i < 3;i++){
        let col = []

        for(let j = 0; j < 3;j++)
            col.push( document.getElementById(`pos${i}-${j}`).getAttribute('data') )
        
        row.push(col)
    }

    return row
}

function postMove(){
    return fetch('/api/test',{
        method:'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify( getBoard() )
    })

}

function didAnyoneWin(borad){

    //Column
    for (let row = 0; row < 3; row++) 
        if(borad[row][0] != "" && borad[row][0] == borad[row][1] && borad[row][1] == borad[row][2] )
            return true

    //Row
    for (let col = 0; col < 3; col++) 
        if(borad[0][col] != "" && borad[0][col] == borad[1][col] && borad[1][col] == borad[2][col] )
            return true

    
    if(borad[0][0] != "" && borad[0][0] == borad[1][1] && borad[1][1] == borad[2][2] )
        return true

        
    if(borad[0][2] != "" && borad[0][2] == borad[1][1] && borad[1][1] == borad[2][0] )
        return true

    return false

}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}