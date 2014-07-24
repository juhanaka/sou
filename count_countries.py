import re
import json

COUNTRIES_FILEPATH = './countries_map.json'
SPEECHES_FILEPATH = './speeches.json'
OUTFILE = './country_frequencies.csv'
SEPARATOR = '[^a-zA-Z0-9_\-]'


def main():
    with open(COUNTRIES_FILEPATH) as countries_json:
        countries = json.load(countries_json)
    with open(SPEECHES_FILEPATH) as speeches_json:
        speeches = json.load(speeches_json)

    with open(OUTFILE, 'w') as outfile:
        for date, document in speeches.iteritems():
            frequency_dict = {}
            for old, modern in countries.iteritems():
                frequency = len(re.findall(SEPARATOR + old + SEPARATOR, document))
                if frequency:
                    for country in modern:
                        frequency_dict[country] = frequency_dict.get(country, 0) + frequency

            for country, value in frequency_dict.iteritems():
                outfile.write('{0},{1},{2}\n'.format(date[-4:],
                                                     country,
                                                     value))

if __name__ == '__main__':
    main()
