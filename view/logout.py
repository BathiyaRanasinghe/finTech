from flask import Blueprint

logout_bp = Blueprint("logout", __name__)


@logout_bp.route("/logout")
def logout():
    # TODO:
    return "<p>Logout</p>"
