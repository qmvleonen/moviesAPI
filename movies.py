from flask import Flask, jsonify, request
app = Flask(__name__)
movies = [
    {
        "name": "The Nun Part 2",
        "casts": ["Bonnie Aarons", "Taissa Frmiga", " Anna Popplewell", "Patrick Wilson",  "Vera Farmiga"],
        "genre": ["Horror"]
    },
    {   
        "name": "Spider-Man: No Way Home",
        "casts": ["Tom Holland", "Zendeya", "Benedict strange"],
        "genre": ["Action, Adventure"]
    }
]

@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'D movie has been deleted', 200

if __name__=='__main__':
    app.run()
