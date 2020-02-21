import requests
import json
import click
from colorama import init, Fore, Style

# The API used in the French gouv open addresses API
URI = 'https://api-adresse.data.gouv.fr/search/?q='


def getAddress(fragment, verbose):
    """Function that calls the Open API for addresses """

    out = ""

    r = requests.get(URI + fragment)

    if (r.ok):
        response = r.json()

        if (verbose):
            click.echo(Fore.RED +
                       json.dumps(response, indent=2, ensure_ascii=True),
                       err=True)
            click.echo(Style.RESET_ALL)

        for feature in response['features']:
            id = feature['properties']['id']
            longitude = feature['geometry']['coordinates'][0]
            latitude = feature['geometry']['coordinates'][1]
            address = feature['properties']['label']
            name = feature['properties']['name']
            score = feature['properties']['score']
            postcode = feature['properties']['postcode']
            city = feature['properties']['city']
            context = feature['properties']['context']
            s_name = name.replace(' ', '+')
            url = "https://www.google.fr/maps/place/%s,+%s+%s/@%f,%f,18z" % (
                s_name, postcode, city, latitude, longitude)

            out = out + "\"%s\";\"%s\";\"%f\";\"%f\";\"%f\";\"%s\";\"%s\";\"%s\";\"%s\"" % (
                id, address, longitude, latitude, score, postcode, city,
                context, url) + "\n"

        return out
