"""Book related routes."""

from app.books import books
from app.attestation.wrappers import attestation_token_required


@books.route('/api/book/test', methods=['POST'])
@attestation_token_required
def book_attestation_route_test():
    """Get all books endpoint."""
    return "Pong."

@books.route('/')
def home():
    return "Pong."
