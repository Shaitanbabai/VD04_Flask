function updateDateTime() {
    const dateTimeContainer = document.getElementById('datetime-container');
    const now = new Date();
    const formattedDateTime = now.toLocaleString();
    dateTimeContainer.textContent = formattedDateTime;
}

// Обновлять дату и время каждую секунду
setInterval(updateDateTime, 1000);

// Инициализация при загрузке страницы
updateDateTime();