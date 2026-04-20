from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>For Ranjitha 💜</title>

<style>
body {
    margin: 0;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    color: white;
    font-family: Arial;
    overflow: hidden;
}

/* 💜 glowing aesthetic background */
body::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, #5f0a87aa, black 70%);
    z-index: 0;
}

/* container */
.container {
    text-align: center;
    z-index: 2;
}

/* image animation */
.img {
    width: 260px;
    border-radius: 15px;
    opacity: 0;
    transform: scale(0.9);
    transition: all 0.8s ease;
}

.show {
    opacity: 1;
    transform: scale(1);
}

/* 🎶 glowing text */
.text {
    margin-top: 15px;
    font-size: 18px;
    text-shadow: 0 0 10px #b026ff, 0 0 20px #b026ff;
}

/* button */
button {
    margin-top: 20px;
    padding: 10px 20px;
    background: #b026ff;
    border: none;
    border-radius: 10px;
    color: white;
    cursor: pointer;
}

/* 💜 floating hearts */
.hearts {
    pointer-events: none;
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: 1;
}

.hearts span {
    position: absolute;
    animation: floatUp linear infinite;
}

@keyframes floatUp {
    from {
        transform: translateY(100vh);
        opacity: 1;
    }
    to {
        transform: translateY(-10vh);
        opacity: 0;
    }
}

/* ✨ sparkle */
.sparkle {
    position: absolute;
    font-size: 20px;
    animation: sparkle 1s ease forwards;
}

@keyframes sparkle {
    from {
        opacity: 1;
        transform: scale(1);
    }
    to {
        opacity: 0;
        transform: scale(2);
    }
}

/* 🎬 fade out */
.fade-out {
    animation: fadeOut 2s forwards;
}

@keyframes fadeOut {
    to {
        opacity: 0;
    }
}
</style>
</head>

<body>

<div class="hearts" id="hearts"></div>

<!-- MUSIC -->
<audio id="bgMusic" preload="auto">
  <source src="/static/bts.mp3" type="audio/mpeg">
</audio>

<div class="container">

    <img id="slide" class="img" src="">

    <div id="text" class="text"></div>

    <button onclick="start()">Click here💜</button>

</div>

<script>

/* images */
const images = [
    "/static/bts1.jpg",
    "/static/bts2.jpg",
    "/static/bts3.jpg",
    "/static/bts4.jpg",
    "/static/bts6.jpg",
    "/static/bts11.jpg",
    "/static/bts12.jpg",
    "/static/bts13.jpg",
    "/static/bts14.jpg",
    "/static/bts15.jpg",
    "/static/bts16.jpg",
    "/static/bts17.jpg",
    "/static/bts18.jpg",
    "/static/bts19.jpg",
    "/static/bts20.jpg",
    
];

/* captions */
const captions = [
    "Happy Flowers Day Ranjitha 💜",
    "You deserve all the flowers 🌸",    
];

/* 💜 hearts */
function createHearts() {
    const container = document.getElementById("hearts");

    for (let i = 0; i < 25; i++) {
        const span = document.createElement("span");
        span.innerHTML = "💜";

        span.style.left = Math.random() * 100 + "vw";
        span.style.animationDuration = (3 + Math.random() * 5) + "s";
        span.style.fontSize = (14 + Math.random() * 10) + "px";

        container.appendChild(span);
    }
}

/* ✨ sparkle */


/* slideshow + music */
function start() {
    const music = document.getElementById("bgMusic");

    music.pause();
    music.currentTime = 0;
    music.muted = false;
    music.play().catch(()=>{});

    document.querySelector("button").style.display = "none";

    let i = 0;
    const img = document.getElementById("slide");
    const text = document.getElementById("text");

    function showNext() {
        if (i >= images.length) {
            setTimeout(() => {
                document.body.classList.add("fade-out");
            }, 2000);
            return;
        }

        img.classList.remove("show");

        setTimeout(() => {
            img.src = images[i];
            text.innerHTML = captions[i] || "";
            img.classList.add("show");

            

            i++;
            setTimeout(showNext, 2500);
        }, 300);
    }

    showNext();
}

/* run hearts */
window.onload = createHearts;

</script>

</body>
</html>
"""

@app.route("/for-ranjitha")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
