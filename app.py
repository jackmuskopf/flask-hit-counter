from flask import Flask, jsonify
from multiprocessing import Value
import random

adjectives = [
	"rampant",
	"cool",
	"fabulous",
	"magical",
	"wondering",
	"chill",
	"frank",
	"forwards",
	"backwards",
	"upside-down",
	"rolling",
	"jubilant",
	"dancing"
]

nouns = [
	"tesla",
	"einstein",
	"planck",
	"curie",
	"sandman",
	"carrot",
	"maxwell",
	"aristotle",
	"jayz",
	"future",
	"kanye"
]

random_name = "_".join([random.choice(adjectives), random.choice(nouns)])

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
    return jsonify(count=counter.value, random_name=random_name)

if __name__ == '__main__':
	app.run(processes=8)