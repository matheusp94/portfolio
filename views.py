from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Visitante")

#usando query
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

#imprimindo json
@views.route("/json")
def get_json():
    return jsonify({'name': 'matheus', 'idade': 30})

#recebendo dados json
@views.route("data")
def get_data():
    data = request.json
    return jsonify(data)

#redirecionamento
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))


@views.route("/perfil")
def get_perfil():
    return render_template("perfil.html")

@views.route("/sobre")
def get_sobre():
    return render_template("sobre.html")