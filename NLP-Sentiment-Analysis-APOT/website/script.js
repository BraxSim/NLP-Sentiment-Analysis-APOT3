async function analyze() {
    let text = document.getElementById("textInput").value;
    if (!text) {
        alert("Please enter text!");
        return;
    }

    let response = await fetch(`http://127.0.0.1:8000/predict/?text=${encodeURIComponent(text)}`);
    let data = await response.json();
    
    document.getElementById("result").innerText = `Sentiment: ${data.sentiment} (Score: ${data.score.toFixed(4)})`;
}
