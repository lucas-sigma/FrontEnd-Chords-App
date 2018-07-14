function setup() {
    createCanvas(450, 200);
    //background(0);
}

function draw() {
    pentagrama();
    notas(2, 70, 55);
}

function pentagrama() {
    fill(255);
    rect(30, 20, 455, 55);
    line(30, 35, 485, 35);
    line(30, 45, 485, 45);
    line(30, 55, 485, 55);
    line(30, 65, 485, 65);
}

function notas(fracao, x, y) {
    if(fracao == 1)
        ellipse(x, y, 10, 7);  // Semibreve
    else if(fracao == 2) {
        // Minima
        line(x + 5, y, x + 5, y / 2);
        notas(1, x, y);
    } else if(fracao == 4) {
        // Seminima
        fill(0);
        notas(2);
    } else if(fracao == 8) {
        // Colcheia
        notas(4);
        line(80, 25, 90, 40);
    } else if(fracao == 16) {
        // Semicolcheia
        notas(8);
        line(80, 35, 90, 40);
    } else if(fracao == 32) {
        // Fusa
        notas(16);
        line(80, 45, 90, 40);
    } else {
        alert("Nota sem fração correta. Por favor, verifique os parâmetros.");
    }
}