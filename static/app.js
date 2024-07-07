let is_auto = false;
let intervalAuto = null;
const $btnAUTO = document.querySelector('#toggle-automatic') 
const $btnGirar = document.querySelector('.btn-girar') 
const $betSelected = document.querySelector('select') 
const $btnResetSaldo = document.querySelector('.reset-saldo') 

const enableAuto = () => {
    is_auto = true
    drawAuto()
    intervalAuto = setInterval(() => {
        $btnGirar.click()
    }, 1000)
}
const disableAuto = () => {
    is_auto = false
    drawAuto()
    clearInterval(intervalAuto)
}
const toggleAuto = ()=> {
    if (is_auto) disableAuto()
    else enableAuto()
}

const drawAuto = () => {
    $btnAUTO.innerText = is_auto ? 'STOP':'AUTO'
}

const resetSaldo = async () => {
    const r = await fetch(`/reset-saldo`)
    const response = await r.json()
    console.log(response)
    document.querySelector('#player-saldo').innerText = response.saldo
}

$btnAUTO.addEventListener('click', (ev) => {
    toggleAuto()
})

$btnGirar.addEventListener('click', async (ev) => {
    const bet_price = $betSelected.value
    const r = await fetch(`/girar?bet_price=${bet_price}`, {
        method: 'POST',
    })
    if (r.status == 200) {
        const response = await r.text()
        document.querySelector('.game').innerHTML = response
        document.querySelector('.logs ul').scrollIntoView(false);
    } else {
        if (is_auto) {
            disableAuto()
            await resetSaldo()
            enableAuto()
        }
    }
})

$btnResetSaldo.addEventListener('click', async (ev) => {
    await resetSaldo()
})
