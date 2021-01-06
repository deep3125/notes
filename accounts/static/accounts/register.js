function Show_tips(x){
    var ele = document.getElementById('passwordPoints');
    if (x){
        ele.style.alignSelf="normal";
        ele.style.transition="0.1s"
        ele.style.visibility="visible";
        ele.style.display="table";
    }
    else{
        ele.style.transition="1s";
        ele.style.visibility="hidden";
        ele.style.display="none";
    }
}