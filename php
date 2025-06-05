<!DOCTYPE html>
<html lang="PT-BR">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Login</title>
</head>
<body>

    <div class="container">
    <h1>CALCULADORA IMC</h1>
    <img src="imc.png" width="100">
    <form method="POST">
        <input type="text" name="nome" placeholder="Digite seu nome" required> <br>
        <input type="decimal" name="peso" placeholder="Digite seu peso" required> <br>
        <input type="decimal" name="altura" placeholder="Digita sua altura" required> <br>
        <button type="submit">Calcular</button>
    </form>
    
        <br>
        <br>
    
    
    <?php

    if($_SERVER["REQUEST_METHOD"] === "POST"){

    $nome = ($_POST['nome']);
    $peso = floatval($_POST['peso']);
    $altura = floatval($_POST['altura']) ;

    $imc = $peso / ($altura * $altura);
    $imcnovo = number_format($imc,2);

    if ($imc < 18.5){
        echo "Olá $nome, seu IMC é $imcnovo e sua classificação é Magreza!";
    }
    elseif ($imc >= 18.5 && $imc <= 24.5){
        echo "Olá $nome, seu IMC é $imcnovo e sua classificação é Normal!";
    }

    else {
        echo "Olá $nome, seu IMC é $imcnovo e sua classificação é Obesidade!";
    }
    }
?>

</body>
</html>
