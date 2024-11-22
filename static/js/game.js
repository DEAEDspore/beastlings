function play(choice) {
    const options = ['rock', 'paper', 'scissors'];
    const computerChoice = options[Math.floor(Math.random() * options.length)];
    let result = '';

    if (choice === computerChoice) {
        result = 'Ничья!';
    } else if (
        (choice === 'rock' && computerChoice === 'scissors') ||
        (choice === 'paper' && computerChoice === 'rock') ||
        (choice === 'scissors' && computerChoice === 'paper')
    ) {
        result = 'Вы выиграли!';
    } else {
        result = 'Вы проиграли!';
    }

    document.getElementById('result').textContent = `Компьютер выбрал: ${computerChoice}. ${result}`;
}
