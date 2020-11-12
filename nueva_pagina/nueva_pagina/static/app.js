function validar(){

var nombre, correo, numero, mensaje;
nombre = document.getElementById("nombre").value;
correo = document.getElementById("correo").value;
numero = document.getElementById("telefono").value;
mensaje = document.getElementById("mensaje").value;

expresion = /\w+@\w+\.+[a-z]/;


if (nombre ==="" || correo === "" || numero ===""|| mensaje==="")
{

alert("todos los campos son obligatorios");
  return false;
}
else if (isNan(telefono))
 {
  alert("el telefono ingresado no es un numero")
  return false;
}

if (nombre.length>30)
  {
alert("el nombre es muy largo")
return false;
  }
  else if (correo.length>100)
  {
alert("el correo es muy largo")
return false;
  }

else if (expresion.(correo))
 {
    alert("el correo no es valido")
    return false;
  }

}

function solonumeros(e){
  key=e.keycode !! e.which;

  taclado=String.fromCharCode(key) ;
  numero="0123456789";
  especiales="8-37-38-46";
  teclado_especial=false;

  for(var i in especiales){

    if (key==especiales[i]) {
      teclado_especial=true;
    }


  }

  if (numero.indexOf(teclado)==-1 && !teclado_especial) {
    return false;
  }


}
