from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                return list1 + ["*"] + list2, True
    return list1 + ["*"] + list2, False

def flames_game(p1, p2):
    p1 = p1.lower().replace(" ", "")
    p2 = p2.lower().replace(" ", "")
    p1_list = list(p1)
    p2_list = list(p2)

    proceed = True
    while proceed:
        combined, proceed = remove_match_char(p1_list, p2_list)
        star_index = combined.index("*")
        p1_list = combined[:star_index]
        p2_list = combined[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    flames = ["F", "L", "A", "M", "E", "S"]
    meanings = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Siblings"
    }

    deletions = []
    temp = flames[:]
    while len(temp) > 1:
        idx = (count % len(temp)) - 1
        if idx >= 0:
            deletions.append(temp[idx])
            temp = temp[idx+1:] + temp[:idx]
        else:
            deletions.append(temp[-1])
            temp = temp[:-1]

    final = temp[0]
    return meanings[final], deletions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    name1 = data['name1']
    name2 = data['name2']
    result, deletions = flames_game(name1, name2)
    return jsonify({'result': result, 'deletions': deletions})

if __name__ == '__main__':
    app.run(debug=True)
