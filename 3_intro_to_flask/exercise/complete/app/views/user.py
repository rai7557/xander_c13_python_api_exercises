from flask import Blueprint, jsonify, request

from exercise.complete.app.controllers.interface import ClientInterface

import json
import requests


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/api/users", methods=["GET", "POST"])
def user_list():
    """Return all users from JSON Placeholder API"""

    client_interface = ClientInterface("/users")

    if request.method == "GET":
        return jsonify(client_interface.get_list())
    else:
        return jsonify(client_interface.post(request.json))


@user_blueprint.route("/api/users/<int:user_id>", methods=["GET"])
def get_single_user(user_id):
    """Return a single user from JSON Placeholder API."""

    client_interface = ClientInterface(f"/users/{user_id}")
    return jsonify(client_interface.get_item())


@user_blueprint.route("/api/users/<int:user_id>", methods=["PUT"])
def user_full_update(user_id):
    """Perform full update of user."""

    client_interface = ClientInterface(f"/users/{user_id}")
    return jsonify(client_interface.put(request.json))


@user_blueprint.route("/api/users/<int:user_id>", methods=["PATCH"])
def user_partial_update(user_id):
    """Perform partial update of user."""

    client_interface = ClientInterface(f"/users/{user_id}")
    return jsonify(client_interface.post(request.json))


@user_blueprint.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Perform DELETE request to delete user."""

    client_interface = ClientInterface(f"/users/{user_id}")
    return jsonify(client_interface.delete())
