function nameValidation(){
    var nama = document.getElementById('nama').value;
    // TODO minimal dua kata
    if(nama.length <= 0) {
        alert('Nama belum diisi atau tidak lengkap')
        return false;
    }
    else {
        var splitted = nama.split(' ');
        var len = splitted.length
        if(len <= 1) {
            alert('Nama belum diisi atau tidak lengkap')
            return false;
        }
    }
    return true;
}

function emailValidation (){
    // TODO belakang nya @gmail.com
    var email = document.getElementById('email').value;
    var splitted = email.split('@') 
    if(email.length <= 0){
        alert('email harus diisi dan mengikuti format "@gmail.com" dibelakang')
        return false
    }
    else if(splitted.length != 2){
        alert('email harus diisi dan mengikuti format "@gmail.com" dibelakang')
        return false
    }
    else if(splitted[1] != 'gmail.com'){
        alert('email harus diisi dan mengikuti format "@gmail.com" dibelakang')
        return false
    }
    return true;
}

function phoneValidation(){
    var phone = document.getElementById('telp').value;
    // ! numeric
    // ! 08
    if(phone.length <= 0){
        alert('nomor telepon harus diisi')
        return false
    }
    else if(isNaN(phone)){
        alert('nomor telepon harus numerik')
        return false
    }
    else if(phone[0] != '0' && phone[1] != '8'){
        alert('depannya harus 08')
        return false
    }
    return true;
}

function genderValidation (){
    var genders = document.getElementsByName('gender')
    for(var i = 0; i < genders.length; i++){
        if(genders[i].checked) return true;
    }
    alert('harus diisi gender')
    return false
}

function saranValidation(){
    var saran = document.getElementById('saran').value
    if(saran.length <= 0){
        alert('saran mohon diisi untuk membantu aplikasi dan toko kami')
        return false
    }
    return true
}

function preferensiValidation (){
    var preferences = document.getElementsByName('ramen')
    for(var i = 0; i < preferences.length; i++){
        if(preferences[i].checked) return true 
    }

    alert('Preferensi Ramen Harus Diisi')
    return false
}

function pedasValidation(){
    var levels = document.getElementsByName('pedas')
    for(var i = 0; i < levels.length; i++){
        if(levels[i].checked) return true 
    }
    alert('Level Kepedasan harus diisi')
    return false
}

function validation () {
    if(!nameValidation()){
        return false;
    }
    else if(!emailValidation()){
        return false;
    }
    else if(!phoneValidation()){
        return false;
    }
    else if(!genderValidation()){
        return false
    }
    else if(!saranValidation()){
        return false
    }
    else if(!preferensiValidation()){
        return false
    }
    else if(!pedasValidation()){
        return false
    }
    else {
        alert('sukses');
        return true;
    }
}