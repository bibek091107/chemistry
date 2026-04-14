import sys
import os

# Add the project root to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Import the Flask app instance from the root app.py.
# Vercel's Python runtime will invoke this WSGI app.
from app import app as application

app = application
