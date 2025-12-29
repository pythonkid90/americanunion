from colony import colony_stats
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/stats')
def stats():
    return render_template('stats.html', colony_stats=colony_stats)

# if __name__ == '__main__':
#     app.run(debug=True)