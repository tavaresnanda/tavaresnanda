function verResultado(){
  const respostac = {
    q1 : "b", //Brasília
    q2 : "c", // Machado de Assis
    q3 : "b" // 56

  };
  
  let pontos = 0;

  for(let q in respostac){
    const respostase = document.querySelector(`input[name = "${q}"]:checked`);
    if (respostase && respostase.value === respostac[q]) {
        pontos ++;
    }

  }

  const perguntas = Object.keys(respostac).length;
  const resultado = document.getElementById("resultado");
  resultado.innerHTML = `Você acertou ${pontos} de ${perguntas} perguntas`

}
