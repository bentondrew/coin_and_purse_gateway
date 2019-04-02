from flask import (Flask,
                   request,
                   Response,
                   json)
import requests
application = Flask(__name__)


@application.route('/', defaults={'path': ''})
@application.route('/<path:path>',
                   methods=['GET',
                            'HEAD',
                            'POST',
                            'PUT',
                            'DELETE',
                            'CONNECT',
                            'OPTIONS',
                            'TRACE',
                            'PATCH'])
def route_forwarding(path):
    forward_path = ('http://{}/{}')
    host = ''
    if 'ledger' in path:
        host = 'ledgerapi:8080'
    if host:
        forward_path = forward_path.format(host, path)
        forward_response = requests.request(
            method=request.method,
            url=forward_path,
            headers={key: value
                     for (key, value) in request.headers
                     if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)
        return Response(forward_response.content,
                        forward_response.status_code,
                        headers=forward_response.raw.headers.items())
    else:
        problem = {'status': 404,
                   'title': 'Not Found',
                   'detail': '/{} not found'.format(path),
                   'type': 'about:blank'}
        return Response(json.dumps(problem),
                        status=404,
                        mimetype='application/problem+json')
