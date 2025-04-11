from flask import Flask, request, jsonify, render_template
from trie import Trie
import os

app = Flask(__name__)
trie = Trie()
dictionary_file = 'dictionary.txt'
word_set = set()

def load_words_from_file(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            if word:
                trie.insert(word)
                word_set.add(word)

load_words_from_file(dictionary_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete')
def autocomplete():
    prefix = request.args.get('prefix', '').lower()
    suggestions = trie.autocomplete(prefix)
    return jsonify(suggestions)

@app.route('/check_and_add', methods=['POST'])
def check_and_add():
    data = request.get_json()
    word = data.get('word', '').lower()
    if word and word not in word_set:
        trie.insert(word)
        word_set.add(word)
        with open(dictionary_file, 'a') as f:
            f.write(word + '\n')
    return jsonify({'message': 'Checked'})


if __name__ == '__main__':
    print("🚀 Server is starting...")
    app.run(debug=True)
