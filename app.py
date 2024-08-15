from flask import Flask, request, render_template
from datetime import date
import random
import string

app = Flask(__name__)

datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d_%B_%Y")

@app.route('/')
def home():
    return render_template('home.html', datetoday2=datetoday2)

@app.route('/genpass', methods=['POST'])
def genpass():
    minpasslen = 8
    maxpasslen = 30

    passlen = int(request.form.get('passlen', 0))
    if passlen < minpasslen:
        return render_template('home.html', datetoday2=datetoday2, mess=f'Password must be at least {minpasslen} characters long.')
    if passlen > maxpasslen:
        return render_template('home.html', datetoday2=datetoday2, mess=f'Password must be no more than {maxpasslen} characters long.')

    include_spaces = request.form.get('includespaces')
    include_numbers = request.form.get('includenumbers')
    include_special_chars = request.form.get('includespecialchars')
    include_uppercase_letters = request.form.get('includeuppercaseletters')

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    char_sets = [lowercase_letters]
    if include_spaces == 'on':
        char_sets.append(' ')
    if include_numbers == 'on':
        char_sets.append(digits)
    if include_special_chars == 'on':
        char_sets.append(special_chars)
    if include_uppercase_letters == 'on':
        char_sets.append(uppercase_letters)

    all_chars = ''.join(char_sets)
    
    if not all_chars:
        return render_template('home.html', datetoday2=datetoday2, mess='No character sets selected.')

    password = ''.join(random.choice(all_chars) for _ in range(passlen))

    return render_template('home.html', datetoday2=datetoday2, generatedpassword=password)

if __name__ == '__main__':
    app.run(debug=True)
