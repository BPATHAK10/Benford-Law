from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.stats import chi2


@view_config(
    route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'a': 1, 'b': 2}


@view_config(route_name='benford', request_method='POST', renderer='templates/benford.jinja2')
def benford(request):
    # Get the uploaded CSV file
    csv_file = request.POST['csv-file'].file

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file, encoding="utf-8", names=["numbers"])

    # Create a column with the first digit of each views
    df['first-digit'] = df['numbers'].astype(str).str[0].astype(int)

    # Calculate the expected frequencies
    expected_freqs = np.log10(1+1/np.arange(1, 10))

    # Calculate the observed frequencies
    observed_freqs = df['first-digit'].value_counts(
        normalize=True).sort_index()

    observed_freqs = observed_freqs.reindex(range(1, 10), fill_value=0)

    # Perform chi square test
    chi_square = (((observed_freqs - expected_freqs)**2) /
                  expected_freqs).sum()
    p_value = 1 - chi2.cdf(chi_square, df=8)
    conforms_to_benford = p_value > 0.05

    # Plot the distribution of first digits
    fig, ax = plt.subplots()
    ax.bar(observed_freqs.index, observed_freqs.values,
           align='center', alpha=0.5)
    ax.plot(expected_freqs, 'r--', label='Expected')
    ax.set_xticks(observed_freqs.index)
    ax.set_xticklabels(observed_freqs.index.astype(str))
    ax.set_xlabel('First Digit')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of First Digits')
    ax.legend()
    plt.savefig('static/benford_plot.png')

    # # Return a JSON response with the Benford test results and the path to the plot image
    return  {'conforms_to_benford': str(conforms_to_benford),
                    #  'expected distribution': expected_freqs.tolist(),
                    #  'observed distribution': observed_freqs.tolist(),
                     'plot_path': 'static/benford_plot.png'}

    # return {'json_data': json.dumps(response_data), 'plot_path': 'static/benford_plot.png'}


if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        config.add_static_view(name='static', path='static')
        config.include('pyramid_debugtoolbar')
        config.add_route('home', '/')
        config.add_route('benford', '/benford')
        config.scan()
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
