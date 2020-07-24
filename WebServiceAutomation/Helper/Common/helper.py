import requests
import string
import random


def get_api_service(params):
    # set the api-endpoint
    api_end_point = "https://restcountries.eu/rest/v2"

    # set the return api with params
    return api_end_point + params


def get_all_countries_response():
    # all countries api
    all_countries_url = get_api_service("/all")

    # sending get request and saving the response as response object
    all_countries_response = requests.get(url=all_countries_url)

    return all_countries_response


def get_specific_country_response(country_code):
    # capture country code and convert in lower case
    get_country_code = country_code.lower()

    # specific country api
    specific_country_url = get_api_service("/alpha/" + get_country_code)

    # sending get request and saving the response as response object
    specific_country_response = requests.get(url=specific_country_url)

    return specific_country_response


def get_country_from_all_countries(country_code):
    # extracting all countries data in json format
    all_countries_data = get_all_countries_response().json()

    # validate if country code for United States,Germany
    # and Unites Kingdom are inside the all countries response
    for country in all_countries_data:
        if country['alpha2Code'] == country_code:
            # return the country response from all countries service
            return country
    return None


def generate_random_country_name():
    # generate a random string with 2 characters
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    return str("".join(random.choice(string.ascii_letters) for x in range(6))).capitalize()


def generate_random_country_code(code_length):
    # generate a random string with 2 characters
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    return str("".join(random.choice(string.ascii_letters) for x in range(code_length)))


def get_diff_country_code_from_all_countries(code_length):
    # extracting all countries data in json format
    all_countries_data = get_all_countries_response().json()

    # get random country 2code
    random_country_code = generate_random_country_code(code_length)

    # initialize get_unique_country_code as None
    get_unique_country_code = None

    # initialize a list to get all country codes
    countries_list = []

    # get a list of all country codes already in the 'all' service
    for country_code in all_countries_data:
        fill_countries = country_code['alpha' + str(code_length) + 'Code'].lower()
        countries_list.append(fill_countries)

    # FIXME: print was made to show all the country code list get from the 'all' response
    print(countries_list)

    # get different country code from all countries in the list
    similar_country_code = True
    while similar_country_code:
        if random_country_code in countries_list:
            # FIXME: print was made to show the similar random country code
            #  comparing with the country list
            print("similar random code = " + random_country_code)

            random_country_code = generate_random_country_code(code_length)

            # FIXME: print was made to show the new random country code to compare
            print("new random code = " + random_country_code)
        else:
            get_unique_country_code = random_country_code

            # FIXME: print was made to show the unique random country code
            print("unique random code = " + get_unique_country_code)

            similar_country_code = False

    return get_unique_country_code
