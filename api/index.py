# api/index.py
import os, sys

# Add project root (parent of /api) to the import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import the Flask app you already wrote
from main import app as app  # <- Vercel looks for "app" (a WSGI callable)
