from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Data structure to hold player and match data
match_data = {
    "teams": {
        "teamA": {"players": {}, "score": 0, "wickets": 0},
        "teamB": {"players": {}, "score": 0, "wickets": 0}
    },
    "current_innings": "teamA",
    "overs": 0,
    "balls_remaining": 120  # Assuming 20 overs per team
}

@app.route('/api/register_batsman', methods=['POST'])
def register_batsman():
    data = request.json
    team = data['team']
    player = data['player']
    match_data['teams'][team]["players"][player] = {
        "runs": 0,
        "balls": 0,
        "sixes": 0,
        "fours": 0
    }
    return jsonify({"message": f"Player {player} registered in {team}"}), 200

@app.route('/api/update_score', methods=['POST'])
def update_score():
    data = request.json
    team = data['team']
    player = data['player']
    runs = data['runs']
    match_data['teams'][team]["players"][player]["runs"] += runs
    match_data['teams'][team]["players"][player]["balls"] += 1
    match_data['teams'][team]["score"] += runs
    match_data["balls_remaining"] -= 1
    return jsonify({"message": f"Updated score for {player}"}), 200

@app.route('/api/match_stats', methods=['GET'])
def match_stats():
    return jsonify(match_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
