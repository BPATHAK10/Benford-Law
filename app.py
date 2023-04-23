from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import pandas as pd
from collections import Counter
import math
import json

@view_config(
    route_name='home', renderer='templates/home.jinja2')
def home(request):
    return{'a': 1, 'b': 2}



@view_config(route_name='benford', request_method='POST', renderer='json')
def benford(request):
    # Get the uploaded CSV file
    csv_file = request.POST['csv-file'].file
    
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file, header=None)
    print(df.head())

    return {
        'success': 'file sent'
    }
    

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_static_view(name='static',path='static')
        config.include('pyramid_debugtoolbar')
        config.add_route('home', '/')
        config.add_route('benford','/benford')
        config.scan()
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
