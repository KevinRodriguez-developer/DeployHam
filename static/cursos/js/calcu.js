var operandoa;
var operandob;
var operandoc;


function init() {
	var resultado = document.getElementById("resultado");
	var uno = document.getElementById("uno");
	var dos = document.getElementById("dos");
	var tres = document.getElementById("tres");
	var cuatro = document.getElementById("cuatro");
	var cinco = document.getElementById("cinco");
	var seis = document.getElementById("seis");
	var siete = document.getElementById("siete");
	var ocho = document.getElementById("ocho");
	var nueve = document.getElementById("nueve");
	var diez = document.getElementById("diez");
	var cero = document.getElementById("cero");


	uno.onclick = function(e){
		resultado.textContent = resultado.textContent + "ONE";
	}
	dos.onclick = function(e){
		resultado.textContent = resultado.textContent + "TWO";
	}
	tres.onclick = function(e){
		resultado.textContent = resultado.textContent + "THREE";
	}
	cuatro.onclick = function(e){
		resultado.textContent = resultado.textContent + "FOUR";
	}
	cinco.onclick = function(e){
		resultado.textContent = resultado.textContent + "FIVE";
	}
	seis.onclick = function(e){
		resultado.textContent = resultado.textContent + "SIX";
	}
	siete.onclick = function(e){
		resultado.textContent = resultado.textContent + "SEVEN";
	}
	ocho.onclick = function(e){
		resultado.textContent = resultado.textContent + "EIGHT";
	}
	nueve.onclick = function(e){
		resultado.textContent = resultado.textContent + "NINE";
	}
	diez.onclick = function(e){
		resultado.textContent = resultado.textContent + "TEN";
	}
	cero.onclick = function(e){
		resultado.textContent = resultado.textContent + "ZERO";
	}

	suma.onclick = function(e){
		operandoa = resultado.textContent;
		operacion = "+";
		limpiar();
	}



}

function limpiar(){
	resultado.textContent= "";
}