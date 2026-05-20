async function checkPassword() {

    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/check-password", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password: password })
    });

    const data = await response.json();

    let score = data.score;
    let strengthText = "";
    let color = "";

    // Strength logic
    if (score >= 6) {
        strengthText = "Strong 💪";
        color = "#22c55e";
    }
    else if (score >= 4) {
        strengthText = "Medium ⚠️";
        color = "#f59e0b";
    }
    else {
        strengthText = "Weak ❌";
        color = "#ef4444";
    }

    // Update progress bar
    document.getElementById("strengthBar").style.width = (score / 6) * 100 + "%";
    document.getElementById("strengthBar").style.background = color;

    // Show result
    document.getElementById("result").innerHTML = `
        <h2 style="color:${color}">${strengthText}</h2>
        <p><b>Score:</b> ${score}/6</p>
        <h4>Suggestions:</h4>
        <ul>
            ${data.feedback.map(f => `<li>${f}</li>`).join("")}
        </ul>
    `;
}