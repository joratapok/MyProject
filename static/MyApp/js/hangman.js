// HANGMAN

var words = ['car', 'program', 'photo', 'parent', 'yellow', 'tree', 'bastard', 'dick', 'smash', 'pony', 'dazzle'];
var word = words[Math.floor(Math.random() * words.length)];

console.log(word);

var answerArray = [];
for (var i = 0; i < word.length; i++) {
    answerArray[i] = '_';
}
var attempt = 7;
var remainingLetters = word.length;
//console.log(answerArray, word)
while (remainingLetters > 0 && attempt > 0) {
    var som = true
//    alert(answerArray.join(' '));
    var guess = prompt('Type your letter or push cancel to quit the game. Attempt remaining ' +
        attempt + '.  Your word '+ answerArray.join(' '));
    if (guess === null) {
        break;
    } else if (guess.length !== 1) {
        alert('only 1 letter please');
    } else {
        for (var j = 0; j < word.length; j++) {
            if (word[j] === guess.toLowerCase()) {
                if (word[j] === answerArray[j]) {
                    alert('alredy exist!');
                    som = false;
                } else {
                    answerArray[j] = guess.toLowerCase();
                    remainingLetters--;
                    som = false;
                }
            }
        }
        if (som === true) {
            alert('miss. try again');
            attempt--;
        }
    }
}
alert('Game over! Hidden word is ' + word)