from flask import Flask, render_template
import psutil   # pip install psutil

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    message = None
    if cpu > 85 or mem > 85:
        message = "⚠️ High resource usage detected!"

    return render_template(
        "index.html",
        cpu_metric=cpu,
        mem_metric=mem,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
