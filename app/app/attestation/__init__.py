"""Attestation init."""

from flask import Blueprint


attestation = Blueprint('attestation',
                           __name__,
                           template_folder="templates")
