let key = document.getElementsByClassName('key')[0];

function keyChangeText() {
    // let symbols = ['⨒','⦔','⫮','▸'];
    if (key.textContent === "ɱȩʈąƈɍɏƥɧą"){
        key.textContent = "Metacrypha"
    }else{
        key.textContent = "ɱȩʈąƈɍɏƥɧą";
    }
}

key.addEventListener('pointerover', keyChangeText);




