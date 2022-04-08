let btn = document.getElementById('btn')

btn.addEventListener('click', function (){
    let weight = document.getElementById('weight').value;
    let height = document.getElementById('height').value;
    let finalbmi = weight / (height * height) * 703;
    document.getElementById('bmi-output').value = finalbmi.toFixed(2);

})