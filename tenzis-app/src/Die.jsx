export default function Die(props){
   function holdBox(){
    let result = false
    props.setter(prev => (
        prev.map((die) => {
            if (die.id == props.num.id){
                const shouldHold = props.held === 0 || props.held === props.num.rand;
                if (props.held === 0){
                    props.heldSetter(props.num.rand)
                }
                if(shouldHold){
                    return {...die, isHeld : true}
                }
                alert("Select the held Value!")
            }
            return die
        })
    ))
   }
    return (
        <button 
        onClick={holdBox}
        className= {props.num.isHeld ? "held" : "unheld"}
        >
            { props.num.rand }
        </button>
    )
}
