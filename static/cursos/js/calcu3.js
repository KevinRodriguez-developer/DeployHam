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
	once.onclick = function(e){
		resultado.textContent = resultado.textContent + "ELEVEN";
	}
	doce.onclick = function(e){
		resultado.textContent = resultado.textContent + " TWELVE";
	}
	trece.onclick = function(e){
		resultado.textContent = resultado.textContent + "THIRTEEN ";
	}
	catorce.onclick = function(e){
		resultado.textContent = resultado.textContent + "FOURTEEN";
	}
	quince.onclick = function(e){
		resultado.textContent = resultado.textContent + " FIFTEEN";
	}
	dieciseis.onclick = function(e){
		resultado.textContent = resultado.textContent + "SIXTEEN";
	}
	diecisiete.onclick = function(e){
		resultado.textContent = resultado.textContent + "SEVENTEEN";
	}
	dieciocho.onclick = function(e){
		resultado.textContent = resultado.textContent + "EIGHTTEEN";
	}
	diecinueve.onclick = function(e){
		resultado.textContent = resultado.textContent + " NINETEEN";
	}
	veinte.onclick = function(e){
		resultado.textContent = resultado.textContent + "WENTY";
	}
	cien.onclick = function(e){
		resultado.textContent = resultado.textContent + "ONE HUNDRED ";
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