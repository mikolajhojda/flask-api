from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))

    sum = x + y
    prediction = 1 if sum > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {"x": x, "y": y}
    })

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)