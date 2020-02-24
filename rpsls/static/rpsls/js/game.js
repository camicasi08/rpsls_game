function EvalGameWinner(creator_selection, creator, opponent_selection, opponent) {

    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['rock', 'scissors']
    }

    if (creator_selection == opponent_selection) {
        return "Empate"
    }
    console.log(rules[creator_selection])
    var result = rules[creator_selection].includes(opponent_selection)

    if (result == true) {
        return creator
    } else {
        console.log("Winner op")
        return opponent
    }

}