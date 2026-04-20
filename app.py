# Digital Flowers Website (Python - Flask, BTS Themed 💜)

# Install:
# pip install flask

# Run:
# python app.py

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
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
        }

        .card {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            width: 380px;
        }

        .flowers {
            font-size: 40px;
            margin: 20px 0;
        }

        .typewriter {
            font-size: 18px;
            min-height: 50px;
            margin-top: 10px;
        }

        button {
            margin-top: 15px;
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            background: #b026ff;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #d15cff;
        }

        .hidden {
            display: none;
            margin-top: 15px;
            font-size: 16px;
        }
    </style>
</head>
<body>

<div class="card">
    <h2>For Ranjitha 💜</h2>
    <div class="flowers">{{ flower_string }}</div>

    <div class="typewriter" id="type"></div>

    <button onclick="reveal()">Click for surprise ✨</button>

    <div class="hidden" id="secret">
        I’m broke but still sending you flowers 😭💐<br>
        Borahae 💜
    </div>
</div>

<script>
    const text = "Happy Flowers Day Ranjitha 🌸 You deserve soft things, chaos, and BTS-level love 💜";
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
    }

    window.onload = typeWriter;
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
