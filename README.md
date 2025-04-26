# Text Autocomplete Web App
This is a simple web application built with Flask that provides word autocomplete functionality using a Trie data structure.
Users can also add new words to the dictionary, which will be saved persistently in a dictionary.txt file.

## Features
🌟 Autocomplete words as you type
➕ Add new words dynamically
💾 Persist new words to a file (dictionary.txt)
🧠 Fast lookup using Trie structure

## Setup Instructions
1. Clone the repository
git clone https://github.com/Vedant-Gidra/Text-Auto-Completer


2. Install dependencies
Make sure you have Python installed 
pip install flask

3. Create a dictionary file (if it doesn't exist)
touch dictionary.txt
(You can manually add some words here to initialize your dictionary.)

4. Ensure you have a trie.py file
The Trie class should implement insert(word) and autocomplete(prefix) methods.

5. Run the server
python app.py

6. Open your browser
Visit http://127.0.0.1:5000/ to use the application.
