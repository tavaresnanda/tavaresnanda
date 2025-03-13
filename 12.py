*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: sans-serif;
}

body{
    background-color: #f3f3f3;
    color: #333;
    line-height: 1.6;
}

header{
    background: #333;
    color: #fff;
    border: 2px solid red;
    padding: 20px;
    text-align: center;
}

nav ul{
    list-style: none;
    padding: 0;
}
nav ul li {
    display: inline;
}
nav ul li a {
    color: #fff;
    text-decoration: none;
}
main{
    display: flex;
    justify-content: space-between;
    padding: 20px;
}

.posts{
   /* border: 3px solid red;*/
    width: 70%;
}
.post{
    background: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
}
.post h2{
margin-bottom: 10px;
}

.btn{
    display: inline-block;
    margin-top: 10px;
    padding: 10px 15px;
    background: linear-gradient(90deg,#e66465,#9198e5);
    border-radius: 10px;
    color:#fff;
    text-decoration: none;
}
