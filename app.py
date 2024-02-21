from flask import Flask, request, render_template

app = Flask(__name__)

def process_text(input_text):
    processed_text = input_text.replace(" ", "_").replace("-", "").replace("+", "plus")
    while "__" in processed_text:
        processed_text = processed_text.replace("__", "_")
    if processed_text:
        processed_text = processed_text[0].upper() + processed_text[1:]
    return processed_text

@app.route('/', methods=['GET', 'POST'])
def index():
    vysledky = None
    if request.method == 'POST':
        input_text = request.form.get('inputText', '')
        if input_text:
            processed_text = process_text(input_text)
            descriptions = [
                "Asset folder naming",
                "Targeted DE naming",
                "Source DE naming",
                "Content test journey naming",
                "Audience test journey naming"
            ]
            pripony = ["", "_Target", "_Source", "_Content_TEST", "_Audience_TEST"]
            vysledky = [(descriptions[i], processed_text + pripona) for i, pripona in enumerate(pripony)]
    return render_template('index.html', vysledky=vysledky)
