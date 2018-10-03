from app import api

# NOTICE : Look At __init__.py
@api.route('/blue')
def sample_blueprint():
    return 'Flask is alive!'