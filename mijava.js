

function hsIntro() {
    var lasops = document.getElementById("introiframe")
    if("hidden" in lasops.classList){
        lasops.classList.remove("hidden")

    }else{
      lasops.classList.add("hidden")
    }
}

// Aqui lo de los botones de projects

function filterproj(cate) {
  document.getElementById("projsec").setAttribute("style","opacity:0;");

  // change selected style
  var losbotones = document.querySelectorAll("#navproje .button");

  for(let i = 0;i < losbotones.length;i++){
    if(losbotones[i].innerHTML.includes(cate)){
      losbotones[i].setAttribute("style","border-bottom: 2px solid;");
    }else{
      losbotones[i].removeAttribute("style");
    }
  }

  // todos los proj
  var posTarget = document.querySelectorAll("#projsec .col-md");

  // get second p
  var p2check = document.querySelectorAll("#projsec .fst-italic");


  if(cate != "All"){

    for (let i = 0; i < p2check.length; i++) {
    var mirar = p2check[i].innerHTML.trim();

    if(mirar.includes(cate)){
      setTimeout(function(){
      posTarget[i].setAttribute("style","display: block; opacity:1;");
      },800);
    }else{
      setTimeout(function(){
      posTarget[i].setAttribute("style","display: none; opacity:0;");
      },800);
    }

        }
    } else {  
      for (let i =0; i < p2check.length; i++){
        setTimeout(function(){
        posTarget[i].setAttribute("style","display: block; opacity:1;");
        },800);
      }
    }
  
  setTimeout(function () {document.getElementById("projsec").setAttribute("style","opacity:1;");}, 800);
}

//var onfilterproj = new Event('onfilterproj');
//document.addEventListener('onfilterproj',returnopa);

//function changeopa(valor){
//  document.getElementById("projsec").setAttribute("style","opacity:"+valor+";")
//  }


// año copyright
var ano = new Date().getFullYear()
document.getElementById("elcopy").innerHTML = `© `+ ano+` `




// Color picker

function showCP() {
  var colpan = document.getElementById("colorpanel")

  if(colpan.classList.contains("visually-hidden")){
      colpan.classList.remove("visually-hidden")
  }else{
    colpan.classList.add("visually-hidden")
  }
}

function changeCOL(){
  nuevo = document.getElementById("colorfondo").value
  document.getElementById("colorhex").innerHTML = `Codigo HEX: ${nuevo}`
  console.log(document.getElementById("lgrad"))
  document.getElementById("lgrad").style.backgroundColor = nuevo
  console.log(document.querySelector(".navbar"))
  document.querySelector(".navbar").style.backgroundColor = nuevo
}


















