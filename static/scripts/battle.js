let playerWins = 0;
let botWins = 0;

// Генерация случайного хода бота
function botChoice() {
    const choices = ["Камень", "Ножницы", "Бумага"];
    return choices[Math.floor(Math.random() * choices.length)];
}

// Логика игры
document.querySelectorAll('.controls button').forEach(button => {
    button.addEventListener('click', () => {
        const playerChoice = button.textContent;
        const botMove = botChoice();

        // Показываем выборы игрока и бота
        document.getElementById('player-choice').textContent = `Вы выбрали: ${playerChoice}`;
        document.getElementById('bot-choice').textContent = `Бот выбрал: ${botMove}`;

        // Проверяем результаты хода
        if ((playerChoice === "Камень" && botMove === "Ножницы") ||
            (playerChoice === "Ножницы" && botMove === "Бумага") ||
            (playerChoice === "Бумага" && botMove === "Камень")) {
            playerWins++;
            document.getElementById('player-wins').textContent = `Победы: ${playerWins}`;
        } else if (playerChoice !== botMove) {
            botWins++;
            document.getElementById('bot-wins').textContent = `Победы: ${botWins}`;
        }

        // Проверяем, достигнуто ли 3 победы у игрока
        if (playerWins === 3) {
            document.getElementById('result-message').textContent = "Победа!";
            document.getElementById('result-overlay').classList.add('show');
            setTimeout(() => {
                window.location.href = "/main_menu";
            }, 2000); // Перенаправление через 2 секунды
        }

        // Проверяем, достигнуто ли 3 победы у бота
        if (botWins === 3) {
            document.getElementById('result-message').textContent = "Поражение!";
            document.getElementById('result-overlay').classList.add('show');
            setTimeout(() => {
                window.location.href = "/main_menu";
            }, 2000); // Перенаправление через 2 секунды
        }
    });
});
