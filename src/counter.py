from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}

# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".


@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED

# Create a route for method PUT on endpoint /counters/<name>.


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """update a counter"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS

    COUNTERS[name] = COUNTERS[name] + 1
    return {name: COUNTERS[name]}, status.HTTP_200_OK

# Create a route for method PUT on endpoint /counters/<name>.


@app.route('/counters/<name>', methods=['GET'])
def read_counter(name):
    """read a counter"""
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS

    return {name: COUNTERS[name]}, status.HTTP_200_OK
