var display = document.getElementById('modal');
var btnmenu = document.getElementById('btnmenu');

btnmenu.onclick = function(){
    display.style.display = "flex";
    document.getElementsByTagName("body")[0].style.overflow = 'hidden';
}
function cls(){
    display.style.display = "none";
    document.getElementsByTagName("body")[0].style.overflow = 'scroll';
}

display.onclick = function(event){
    if(event.target == display){
        display.style.display ="none";
        document.getElementsByTagName("body")[0].style.overflow = 'scroll';
    }
}

//-----------------------------------------------//
var btnmenu1 = document.getElementById('btn_sub');
var display2 = document.getElementById('modalOK');

btnmenu1.onclick = function(){
    display.style.display ="none";
    display2.style.display = "flex";
    document.getElementsByTagName("body")[0].style.overflow = 'hidden';
}
function cls1(){
    display2.style.display = "none";
    document.getElementsByTagName("body")[0].style.overflow = 'scroll';
}

display2.onclick = function(event){
    if(event.target == display2){
        display2.style.display ="none";
        document.getElementsByTagName("body")[0].style.overflow = 'scroll';
    }
}