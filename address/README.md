# address cli

A CLI tool for interaction with french Open Gouv address API


## Install

```sh 
pip install ea-address
```

## Develop

```sh
pip install --editable .
```

Then, enjoy the simplicyty of launching your module by calling it on the command line.

## Install

Using pip

```sh
pip install --editable .
```

## Usage

### With no arguments

It displays the basic help and show available commands

```sh
$ ea-address
Usage: ea-address [OPTIONS] COMMAND [ARGS]...

  CLI commands that search and fetch addresses

Options:
  -v, --verbose
  --help         Show this message and exit.

Commands:
  search  Send a request to Open API Address and format the responses The...
```

### Help

General help :

```sh
$ ea-address --help
Usage: ea-address [OPTIONS] COMMAND [ARGS]...

  CLI commands that search and fetch addresses

Options:
  -v, --verbose
  --help         Show this message and exit.

Commands:
  search  Send a request to Open API Address and format the responses The...

```

Help on 'search' command :

```sh
$ ea-address search --help
Usage: ea-address search [OPTIONS] [FRAGMENT]

  Send a request to Open API Address and format the responses The error is
  accessible through the verbose mode

Options:
  --help  Show this message and exit.
```

### Data model


The command line serves csv records.

- id : a unique identifier for this address
- full_address : the full_address it self
- longitude : the float represetaion of the longitude of this address
- latitude : the float represetaion of the latitude of this address
- zipcode : the postal code 
- city : the city
- context: the context of the address which is the department number, name and region's name
- url : a Google Map url that you can click on to open a browser 

"91377_1610_00012";"12 Rue du Chemin des Femmes 91300 Massy";"2.266108";"48.726848";"0.956422";"91300";"Massy";"91, Essonne, Île-de-France";"https://www.google.fr/maps/place/12+Rue+du+Chemin+des+Femmes,+91300+Massy/@48.726848,2.266108,18z"


### Simplest search

The 'search' will show you the adress you're looking for in 2 formats : CSV and even JSON

Without any argument, the response is e-Attestations address

```sh
$ ea-address search
"91377_1610_00012";"12 Rue du Chemin des Femmes 91300 Massy";"2.266108";"48.726848";"0.956422";"91300";"Massy";"91, Essonne, Île-de-France";"https://www.google.fr/maps/place/12+Rue+du+Chemin+des+Femmes,+91300+Massy/@48.726848,2.266108,18z"
```

### Argumented search

With an address as an argument you're looking for surounded by quotes or double-quotes, you'll have a single line

```sh
$ ea-address search "12 Rue du Chemin des Femmes 91300 Massy" 
"91377_1610_00012";"12 Rue du Chemin des Femmes 91300 Massy";"2.266108";"48.726848";"0.956422";"91300";"Massy";"91, Essonne, Île-de-France";"https://www.google.fr/maps/place/12+Rue+du+Chemin+des+Femmes,+91300+Massy/@48.726848,2.266108,18z"
```

### Search gives up to 5 responses

With an address that gives more than one response from the API, you'll have csv formated records

```sh
$ ea-address search "Chateau, Versailles"
"03230_b023";"Chateau de Verseilles 03300 Saint-Étienne-de-Vicq";"3.537768";"46.153765";"0.584470";"03300";"Saint-Étienne-de-Vicq";"03, Allier, Auvergne-Rhône-Alpes";"https://www.google.fr/maps/place/Chateau+de+Verseilles,+03300+Saint-Étienne-de-Vicq/@46.153765,3.537768,18z"
"11253_z7skxn";"Château du Petit Versailles 11170 Montolieu";"2.217006";"43.302861";"0.563825";"11170";"Montolieu";"11, Aude, Occitanie";"https://www.google.fr/maps/place/Château+du+Petit+Versailles,+11170+Montolieu/@43.302861,2.217006,18z"
"37063_b033";"Le Petit Versailles 37110 Château-Renault";"0.897810";"47.588413";"0.445982";"37110";"Château-Renault";"37, Indre-et-Loire, Centre-Val de Loire";"https://www.google.fr/maps/place/Le+Petit+Versailles,+37110+Château-Renault/@47.588413,0.897810,18z"
"37063_0430";"Rue du Petit Versailles 37110 Château-Renault";"0.899719";"47.589995";"0.402920";"37110";"Château-Renault";"37, Indre-et-Loire, Centre-Val de Loire";"https://www.google.fr/maps/place/Rue+du+Petit+Versailles,+37110+Château-Renault/@47.589995,0.899719,18z"
"85060_0515";"Rue du Petit Versailles 85340 Les Sables-d'Olonne";"-1.719095";"46.476289";"0.363056";"85340";"Les Sables-d'Olonne";"85, Vendée, Pays de la Loire";"https://www.google.fr/maps/place/Rue+du+Petit+Versailles,+85340+Les Sables-d'Olonne/@46.476289,-1.719095,18z"

```

### Augmented search

More advanced usage by redirecting the json result but display our banner

```sh
$ ea-address -v search "Palais de l'Elysée, PARIS" 2> result.json
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ║
║  e-Attestations.com - Third-Party Management Solutions & Services                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ║
║  All right reserved/Tous droits réservés                                                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ║
║                  _   _            _        _   _                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓,     ▓  ║
║             /\  | | | |          | |      | | (@)                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓.     ▓▓  ║
║  ___       /  \ | |_| |_ ___  ___| |_ __ _| |_ _  ___  _ __  ___   ___ ___  _ __ ___    ▓▓▓▓▓▓▓▓▓▓▓▓▓,      ▓▓▓  ║
║ / _ \  __ / /\ \| __| __/ _ \/ __| __/ _` | __| |/ _ \| '_ \/ __| / __/ _ \| '_ ` _ \   ▓▓▓▓▓▓▓▓▓▓▓▓,     .▓▓▓▓  ║
║|  __//__ / ____ \ |_| ||  __/\__ \ || (_| | |_| | (_) | | | \__ \| (_| (_) | | | | | |   .▓▓▓▓▓▓▓▓▓.     ,▓▓▓▓▓  ║
║ \___/   /_/    \_\__|\__\___||___/\__\__,_|\__|_|\___/|_| |_|___(_)___\___/|_| |_| |_|      .▓▓▓▓▓      ,▓▓▓▓▓▓  ║
║                                                                                                .,      .▓▓▓▓▓▓▓  ║
║                                                                                         ▓,           ,▓▓▓▓▓▓▓▓▓  ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
:: e-Attestations.com (https://www.e-attestations.com) :: \ö/ ★★★★ 😎
Looking for address Palais de l'Elysée, PARIS


"75108_3190";"Rue de l'Elysée 75008 Paris";"2.316664";"48.868921";"0.580867";"75008";"Paris";"75, Paris, Île-de-France";"https://www.google.fr/maps/place/Rue+de+l'Elysée,+75008+Paris/@48.868921,2.316664,18z"
"75120_3192";"Rue de l'Elysée Ménilmontant 75020 Paris";"2.386009";"48.869068";"0.410182";"75020";"Paris";"75, Paris, Île-de-France";"https://www.google.fr/maps/place/Rue+de+l'Elysée+Ménilmontant,+75020+Paris/@48.869068,2.386009,18z"
"75101_7010";"Place du Palais Royal 75001 Paris";"2.336185";"48.862728";"0.369503";"75001";"Paris";"75, Paris, Île-de-France";"https://www.google.fr/maps/place/Place+du+Palais+Royal,+75001+Paris/@48.862728,2.336185,18z"
"75108_1733";"Avenue des Champs Elysées 75008 Paris";"2.316523";"48.866220";"0.368868";"75008";"Paris";"75, Paris, Île-de-France";"https://www.google.fr/maps/place/Avenue+des+Champs+Elysées,+75008+Paris/@48.866220,2.316523,18z"
"75119_7011";"Cité du Palais Royal de Belleville 75019 Paris";"2.390407";"48.876027";"0.362410";"75019";"Paris";"75, Paris, Île-de-France";"https://www.google.fr/maps/place/Cité+du+Palais+Royal+de+Belleville,+75019+Paris/@48.876027,2.390407,18z"
```

The json file produces is in this case result.json :

```json
{
  "type": "FeatureCollection",
  "version": "draft",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          2.316664,
          48.868921
        ]
      },
      "properties": {
        "label": "Rue de l'Elys\u00e9e 75008 Paris",
        "score": 0.5808668359870147,
        "id": "75108_3190",
        "type": "street",
        "x": 649873.53,
        "y": 6863427.23,
        "importance": 0.5049198112417776,
        "name": "Rue de l'Elys\u00e9e",
        "postcode": "75008",
        "citycode": "75108",
        "city": "Paris",
        "district": "Paris 8e Arrondissement",
        "context": "75, Paris, \u00cele-de-France"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          2.386009,
          48.869068
        ]
      },
      "properties": {
        "label": "Rue de l'Elys\u00e9e M\u00e9nilmontant 75020 Paris",
        "score": 0.41018152807588115,
        "id": "75120_3192",
        "type": "street",
        "x": 654960.39,
        "y": 6863401.82,
        "importance": 0.5889198857577701,
        "name": "Rue de l'Elys\u00e9e M\u00e9nilmontant",
        "postcode": "75020",
        "citycode": "75120",
        "city": "Paris",
        "district": "Paris 20e Arrondissement",
        "context": "75, Paris, \u00cele-de-France"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          2.336185,
          48.862728
        ]
      },
      "properties": {
        "label": "Place du Palais Royal 75001 Paris",
        "score": 0.3695031396574084,
        "id": "75101_7010",
        "type": "street",
        "x": 651299.69,
        "y": 6862726.42,
        "importance": 0.4645345362314921,
        "name": "Place du Palais Royal",
        "postcode": "75001",
        "citycode": "75101",
        "city": "Paris",
        "district": "Paris 1er Arrondissement",
        "context": "75, Paris, \u00cele-de-France"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          2.316523,
          48.86622
        ]
      },
      "properties": {
        "label": "Avenue des Champs Elys\u00e9es 75008 Paris",
        "score": 0.36886830819901323,
        "id": "75108_1733",
        "type": "street",
        "x": 649860.62,
        "y": 6863126.95,
        "importance": 0.5049198112417776,
        "name": "Avenue des Champs Elys\u00e9es",
        "postcode": "75008",
        "citycode": "75108",
        "city": "Paris",
        "district": "Paris 8e Arrondissement",
        "context": "75, Paris, \u00cele-de-France"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          2.390407,
          48.876027
        ]
      },
      "properties": {
        "label": "Cit\u00e9 du Palais Royal de Belleville 75019 Paris",
        "score": 0.36240983460758064,
        "id": "75119_7011",
        "type": "street",
        "x": 655288.98,
        "y": 6864173.09,
        "importance": 0.5865081806833872,
        "name": "Cit\u00e9 du Palais Royal de Belleville",
        "postcode": "75019",
        "citycode": "75119",
        "city": "Paris",
        "district": "Paris 19e Arrondissement",
        "context": "75, Paris, \u00cele-de-France"
      }
    }
  ],
  "attribution": "BAN",
  "licence": "ETALAB-2.0",
  "query": "Palais de l'Elys\u00e9e, PARIS",
  "limit": 5
}
```
