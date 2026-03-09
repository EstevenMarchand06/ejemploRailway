from flask import Flask, request, jsonify
from calculator import sumar, restar, multiplicar, dividir

app = Flask(__name__)

@app.route("/")
def home():
    return "API Calculadora funcionando en Railway"

@app.route("/sumar")
def suma():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"resultado": sumar(a,b)})

@app.route("/restar")
def resta():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"resultado": restar(a,b)})

@app.route("/multiplicar")
def multi():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"resultado": multiplicar(a,b)})

@app.route("/dividir")
def div():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"resultado": dividir(a,b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)