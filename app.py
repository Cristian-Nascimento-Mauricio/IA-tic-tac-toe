from flask import Flask , render_template , jsonify , request 
from algorithm import voidSpace, bestAction

app = Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/api/test', methods=['POST'])
def get_dados():
    
    board = request.json
    
    pos = bestAction(board)

    return jsonify({"row":pos[0],"col":pos[1]})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80) 


def isOverflowBoard(board):


    
    for row in board:
        for col in row:
            if col == "":
                return False
            
    return True           