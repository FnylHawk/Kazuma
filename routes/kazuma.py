from flask import Blueprint, request, jsonify

efficient_hunter_kazuma = Blueprint('efficient_hunter_kazuma', __name__)

@efficient_hunter_kazuma.route('/efficient-hunter-kazuma', methods=['POST'])
def kazuma_efficiency():
    data = request.get_json()

    result = []
    for entry in data:
        monsters = entry['monsters']
        efficiency = calculate_max_efficiency(monsters)  # Using the recursive solution
        result.append({"efficiency": efficiency})
    
    return jsonify(result)

def calculate_max_efficiency(monsters):
    total_monsters = len(monsters)

    def recursive_solution(i, circle_prepared, in_cooldown, gold_earned, protection_cost):
        if i >= total_monsters:
            return gold_earned - protection_cost  # Base case: end of the list

        max_efficiency = float('-inf')

        if in_cooldown:
            # Cooldown ends, continue with next turn without doing anything
            max_efficiency = max(max_efficiency, recursive_solution(i + 1, False, False, gold_earned, protection_cost))
        elif circle_prepared:
            # Attack if the circle is prepared
            if monsters[i] > 0:
                # After attacking, we enter cooldown
                max_efficiency = max(max_efficiency, recursive_solution(i + 1, False, True, gold_earned + monsters[i], protection_cost))
            # Alternatively, continue waiting
            max_efficiency = max(max_efficiency, recursive_solution(i + 1, True, False, gold_earned, protection_cost))
        else:
            # Option to prepare the circle if there are no monsters
            if monsters[i] == 0:
                max_efficiency = max(max_efficiency, recursive_solution(i + 1, True, False, gold_earned, protection_cost))
            # Option to prepare a circle with protection cost if monsters are present
            elif monsters[i] > 0:
                max_efficiency = max(max_efficiency, recursive_solution(i + 1, True, False, gold_earned, protection_cost + monsters[i]))
            # Alternatively, skip this turn and back out
            max_efficiency = max(max_efficiency, recursive_solution(i + 1, False, False, gold_earned, protection_cost))

        return max_efficiency

    return max(0, recursive_solution(0, False, False, 0, 0))
