from kobin import Kobin, Response

app = Kobin()


@app.route('/')
def index():
    return Response('Hello World')

