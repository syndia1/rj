from flask import Flask, render_template_string
import random

app = Flask(__name__)

flowers = ["🌸","🌹","🌼","🌻","🌷","💐","🌺","🪻"]

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>For Ranjitha 💜</title>

    <style>
        body {
            margin: 0;
            font-family: Arial;
            background: linear-gradient(135deg, #1f0036, #5f0a87);
            overflow: hidden;
            color: white;
        }

        .loader {
            position: absolute;
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: black;
            z-index: 10;
        }

        .card {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(255,255,255,0.1);
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            backdrop-filter: blur(10px);
            width: 380px;
            display: none;
        }

        .flowers { font-size: 36px; margin: 15px 0; }
        .typewriter { font-size: 16px; min-height: 40px; }

        button {
            margin-top: 10px;
            padding: 8px 16px;
            border: none;
            border-radius: 10px;
            background: #b026ff;
            color: white;
            cursor: pointer;
        }

        .hidden { display: none; margin-top: 10px; }

        .hearts span {
            position: absolute;
            color: pink;
            animation: float 6s linear infinite;
        }

        @keyframes float {
            from { transform: translateY(100vh); }
            to { transform: translateY(-10vh); }
        }

        .bouquet-builder {
            margin-top: 15px;
        }

        .flower-btn {
            font-size: 20px;
            margin: 3px;
            cursor: pointer;
        }

        .bouquet {
            margin-top: 10px;
            font-size: 28px;
        }
    </style>
</head>
<body>

<div class="loader" id="loader">Loading your flowers... 💐</div>

<div class="card" id="card">
    <h2>For Ranjitha 💜</h2>

    <div class="flowers">{{ flower_string }}</div>

    <div class="typewriter" id="type"></div>

    <button onclick="reveal()">Click for surprise ✨</button>

    <div class="hidden" id="secret">
        Sending you flowers because you deserve it 💐<br>
        Did you eat the speaker that day? 💀<br>
        Borahae 💜<br><br>
        <b>From: your chaotic bestie</b>
    </div>

    <div class="bouquet-builder">
        <p>Make your own bouquet 🌷</p>
        <div>
            <span class="flower-btn" onclick="addFlower('🌸')">🌸</span>
            <span class="flower-btn" onclick="addFlower('🌹')">🌹</span>
            <span class="flower-btn" onclick="addFlower('🌼')">🌼</span>
            <span class="flower-btn" onclick="addFlower('🌻')">🌻</span>
            <span class="flower-btn" onclick="addFlower('🌷')">🌷</span>
        </div>
        <div class="bouquet" id="bouquet"></div>
    </div>
</div>

<div class="hearts" id="hearts"></div>

<audio id="bgMusic" loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3?filename=romantic-background-112191.mp3" type="audio/mpeg">
</audio>

<script>
    const text = "Happy Flowers Day Ranjitha 🌸 You deserve chaos, soft things, and BTS-level love 💜";
    let i = 0;

    function typeWriter() {
        if (i < text.length) {
            document.getElementById("type").innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, 40);
        }
    }

    function reveal() {
        document.getElementById("secret").style.display = "block";
        document.getElementById("bgMusic").play().catch(() => {});
    }

    function loadScreen() {
        setTimeout(() => {
            document.getElementById("loader").style.display = "none";
            document.getElementById("card").style.display = "block";
            typeWriter();
        }, 2000);
    }

    function createHearts() {
        const hearts = document.getElementById("hearts");
        for (let i = 0; i < 20; i++) {
            let span = document.createElement("span");
            span.innerHTML = "💜";
            span.style.left = Math.random() * 100 + "vw";
            span.style.animationDuration = (3 + Math.random() * 5) + "s";
            hearts.appendChild(span);
        }
    }

    function addFlower(flower) {
        document.getElementById("bouquet").innerHTML += flower;
    }

    window.onload = () => {
        loadScreen();
        createHearts();
    };
</script>

</body>
</html>
"""

def generate_flowers():
    return "".join(random.choice(flowers) for _ in range(10))

@app.route("/for-ranjitha")
def ranjitha():
    return render_template_string(html_template, flower_string=generate_flowers())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
