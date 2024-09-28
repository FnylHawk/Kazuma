from flask import Flask, jsonify, request

app = Flask(__name__)

def movesetOptimization(monstersNumArray):
    monsters = monstersNumArray['monstersArray']
    efficiency = 0
    n = len(monsters)

    i = 0
    while i < n:
        if i < n - 1 and monsters[i] < monsters[i + 1]:  # Prepare transmutation circle only when monsters increase
            efficiency -= monsters[i]  # Pay protection cost for preparing the circle
            efficiency += monsters[i + 1]  # Gain efficiency from attacking the next set of monsters
            i += 2  # After attacking, skip the next turn due to cooldown
        else:
            i += 1  # Move to the next time frame if no transmutation circle is prepared

    return efficiency

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def evaluate_endpoint():
    # Get JSON data from the request
    data = request.get_json()

    efficiency = []  # Initialize empty list for efficiencies

    for monsters in data:
        # Create a dictionary to pass to the optimization function
        monsters_data = {'monstersArray': monsters['monsters']}
        optimalMoves = movesetOptimization(monsters_data)
        efficiency.append({"efficiency": optimalMoves})

    print(efficiency)
    return jsonify(efficiency)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
