from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.insert(0, note)
    return render_template("home.html", notes=enumerate(notes))

@app.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        edited_note = request.form.get("edited_note")
        notes[index] = edited_note
        return redirect(url_for('index'))
    return render_template("edit.html", index=index, note=notes[index])

 

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    del notes[index]
    return redirect(url_for('index'))

@app.route('/delete_all', methods=["POST"])
def delete_all():
    notes.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
