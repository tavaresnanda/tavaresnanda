<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz de Perguntas</title>
    <link rel="stylesheet" href="style.css">

</head>
<body>

    

    <div class="container">

    <h1>Quiz de Perguntas</h1>

    <h2>1.Qual é a capital do Brasil? </h2>

    <label><input type="radio" name="q1" value="a"> Rio de Janeiro</label>
    <label><input type="radio" name="q1" value="b"> Brasilia</label>
    <label><input type="radio" name="q1" value="c"> São Paulo</label>

    <h2>2.Quem escreveu "Dom Casmurro"?</h2>

    <label><input type="radio" name="q2" value="a"> Clarice Lispector</label>
    <label><input type="radio" name="q2" value="b"> José de Alencar</label>
    <label><input type="radio" name="q2" value="c"> Machado de Assis</label>


   <h2>3.Quanto é 7 x 8?</h2>
 
    <label><input type="radio" name="q3" value="a"> 54 </label>
    <label><input type="radio" name="q3" value="b"> 56 </label>
    <label><input type="radio" name="q3" value="c"> 64 </label>


    <button type="button" onclick="verResultado()"> Resultado</button>

    
    <div id="Resultado"> </div>

    </div>
    <script src="script.js"></script>
</body>
</html>
