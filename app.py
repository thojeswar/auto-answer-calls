import os
from flask import Flask, Response, request

app = Flask(__name__)

# Edit this message, or set the GREETING env var on your host
GREETING = os.environ.get(
    "GREETING",
    "Hi, you have reached Thojeswar . I am currently not available to take calls. "
    "If this is regarding a project allocation or any official matter, "
    "please send me an email or message with the details, and I will get back to you. "
    "Thank you.",
)


@app.route("/voice", methods=["POST", "GET"])
def voice():
    # Twilio-style TwiML response: speak the message, then hang up
    print("Incoming call from:", request.values.get("From"))
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="Polly.Aditi" language="en-IN">{GREETING}</Say>
    <Hangup/>
</Response>"""
    return Response(twiml, mimetype="text/xml")


@app.route("/")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
