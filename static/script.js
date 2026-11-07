const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function displayMessage(message, className) {
  const messageElement = document.createElement("p");

  messageElement.classList.add(className);
  messageElement.textContent = message;

  chatContainer.appendChild(messageElement);
}

sendBtn.addEventListener("click", async function () {
  const message = userInput.value;

  if (message.trim() === "") {
    return;
  }

  displayMessage(message, "user-message");

  userInput.value = "";

  const response = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: message }),
  });
  const data = await response.json();
  displayMessage(data.reply, "bot-message");
});
