import React from "react"
import Die from './Die'
import ConfettiEffect from './ConfettiEffect'

export default function App(){

  const [held, setHeld] = React.useState(0)

  const numbers = (prev = null) => {
    let diceArray = [];
    for(let i = 0; i < 10; i ++){
      let randomNum = Math.ceil(Math.random()*6)
      diceArray.push(prev && prev[i].isHeld ? prev[i] : {id:i, rand : randomNum, isHeld:false})
    }
    return diceArray;
  }

  const [dice, setDice] = React.useState(numbers())

  const diceArray = dice.map(number => <Die num = {number} setter = {setDice} held = {held} heldSetter = {setHeld}/>)

  function rollDice(){
    setDice(prev => numbers(prev))
  }
  let isTenzies = false
  for(let die of dice){
    if(!die.isHeld){
      isTenzies = false
      break
    }
    else{
      isTenzies = true
    }
  }


  return (
    <>
      <main>
        <div>Roll a Dice</div>
        <div> <p>Tenzies is a fun dice game.Roll until all dice show the same number.Click a die to hold its value while you roll the rest!</p>
        </div>
       

        <div id="container">
          {diceArray}
        </div>
        <button onClick={ rollDice }>Roll</button>
      </main>
      { isTenzies && <ConfettiEffect /> }
    </>
  )
}