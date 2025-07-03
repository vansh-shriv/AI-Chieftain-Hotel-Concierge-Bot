from flask import Flask, request, jsonify
from bot_logic import concierge_bot

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    # user_message = request.json.get("message")
    # # user_message = "Can I book a spa appoin/tment at 6PM?"
    # if not user_message:
    #     return jsonify({"error": "No message provided"}), 400
    
    # bot_reply = concierge_bot.run(user_message)
    # return jsonify({"response": bot_reply})
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        bot_reply = concierge_bot.run(user_message)
        return jsonify({"response": bot_reply})
    except Exception as e:
        # Print the error to console for debugging
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
