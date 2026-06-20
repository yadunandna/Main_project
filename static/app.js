async function sendMessage() {

    const messageBox = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const message = messageBox.value.trim();

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user-msg">
            <strong>You:</strong> ${message}
        </div>
    `;

    const formData = new FormData();
    formData.append("message", message);

    const response = await fetch("/chat", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="bot-msg">
            <strong>ExamPulse AI:</strong>
            ${data.response}
        </div>
    `;

    messageBox.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}