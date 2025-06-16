let win = document.getElementById("win");
let c = document.getElementById("computer");
let p = document.getElementById("person");
let score1 = document.getElementById("c_score");
let score2 = document.getElementById("p_score");
let computer_count = 0;
let person_count = 0;

function rock_click() {
  play("rock");
}

function paper_click() {
  play("paper");
}

function scissor_click() {
  play("scissor");
}

function play(user) {
  let n = Math.floor(Math.random() * 3) + 1;
  let t;
  let temp;
  if (n == 1) {
    temp = "rock";
    t =
      user == "rock"
        ? "Match Draw!"
        : user == "paper"
        ? "You won!"
        : "Computer won!";
  } else if (n == 2) {
    temp = "paper";
    t =
      user == "rock"
        ? "Computer won!"
        : user == "paper"
        ? "Match Draw!"
        : "You won!";
  } else {
    temp = "scissor";
    t =
      user == "rock"
        ? "You won!"
        : user == "paper"
        ? "Computer won!"
        : "Match Draw!";
  }
  if (t == "You won!") {
    person_count += 1;
  }
  if (t == "Computer won!") {
    computer_count += 1;
  }

  win.innerHTML = t;
  c.innerHTML = `Computer: ${temp}`;
  p.innerHTML = `Person: ${user}`;
  score1.innerHTML = `Computer Score: ${computer_count}`;
  score2.innerHTML = `Person Score: ${person_count}`;
}

function reset() {
  computer_count = 0;
  person_count = 0;
  c.innerHTML = `Computer:`;
  p.innerHTML = `Person:`;
  score1.innerHTML = `Computer Score: ${computer_count}`;
  score2.innerHTML = `Person Score: ${person_count}`;
}
