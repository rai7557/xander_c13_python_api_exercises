from flask import Blueprint, jsonify, request
from exercise.complete.app.controllers.interface import ClientInterface


post_blueprint = Blueprint("post", __name__)


@post_blueprint.route("/api/posts", methods=["GET", "POST"])
def user_list():
    """Return all users from JSON Placeholder API"""

    client_interface = ClientInterface("/posts")

    if request.method == "GET":
        return jsonify(client_interface.get_list())
    else:
        return jsonify(client_interface.post(request.json))


@post_blueprint.route("/api/posts/<int:post_id>", methods=["GET"])
def get_single_user(post_id):
    """Return a single user from JSON Placeholder API."""

    client_interface = ClientInterface(f"/posts/{post_id}")
    return jsonify(client_interface.get_item())


@post_blueprint.route("/api/posts/<int:post_id>", methods=["PUT"])
def user_full_update(post_id):
    """Perform full update of user."""

    client_interface = ClientInterface(f"/users/{post_id}")
    return jsonify(client_interface.put(request.json))


@post_blueprint.route("/api/posts/<int:post_id>", methods=["PATCH"])
def user_partial_update(post_id):
    """Perform partial update of user."""

    client_interface = ClientInterface(f"/users/{post_id}")
    return jsonify(client_interface.post(request.json))


@post_blueprint.route("/api/posts/<int:post_id>", methods=["DELETE"])
def delete_user(post_id):
    """Perform DELETE request to delete user."""

    client_interface = ClientInterface(f"/users/{post_id}")
    return jsonify(client_interface.delete())
