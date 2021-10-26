"""Attestation wrappers module."""

from functools import wraps
from flask import abort, request


def attestation_token_required(func):
    """Attestation token required wrapper."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """Decorate function."""
        attestation_token = request.headers.get("Attestation")
        if attestation_token is None:
            abort(401)

        # Validate attestation token here
        # if not valid_attestation(attestation_token):
        #     abort(401)

        return func(*args, **kwargs)
    return decorated_function
