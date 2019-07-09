from flask import Flask, request, jsonify, abort
from anna_lib.task import factory

app = Flask(__name__)


def get_namespace() -> str:
	namespace = ''
	if 'namespace' in request.args:
		namespace = request.args['namespace']
		if namespace is list and len(namespace) > 0 and namespace[0] is str:
			namespace = namespace[0]

	return namespace


@app.route('/', methods=['GET'])
def get_tasks():
	if request.data is not None:
		namespace = get_namespace()
		if namespace is None or len(namespace) == 0:
			abort(400)

		tasks = factory.get_tasks(namespace=namespace)
		if tasks is not None:
			return jsonify(tasks)
		abort(404)
	else:
		abort(400)


if __name__ == '__main__':
	app.run(host='tasks.annahub.se', port=5001, debug=False)
