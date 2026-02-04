function time (){
    const date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();
    let day = date.getDate();
    let month = date.getMonth() + 1;
    let year = date.getFullYear();
    document.getElementById("time").innerHTML = hours + ":" + minutes + ":" + seconds;
    document.getElementById("date").innerHTML = month + "/" + day + "/" + year;
    

}  
setInterval(time, 1000);