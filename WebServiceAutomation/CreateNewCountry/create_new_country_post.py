# importing necessary libraries
import requests
from Helper.Common.helper import generate_random_country_name
from Helper.Common.helper import generate_random_country_code


def test_create_new_country_post():
    # all countries api-endpoint
    all_countries_url = "https://restcountries.eu/rest/v2/all"

    # get random country name
    get_random_country_name = generate_random_country_name()

    # get random country code with 2 digits
    get_random_country_2code = generate_random_country_code(2)

    # get random country code with 3 digits
    get_random_country_3code = generate_random_country_code(3)

    # data to be send using post
    new_country_data = {
        "name": get_random_country_name,
        "alpha2_code": get_random_country_2code,
        "alpha3_code": get_random_country_3code,
    }

    # sending post request and saving response as response object
    create_new_country = requests.post(url=all_countries_url, data=new_country_data)

    # get post status code
    post_status_code = create_new_country.status_code

    # assert is the post request service status code is 201
    assert (post_status_code == 201), "Status code is different from 201:" \
                                      " Request status code is " + str(post_status_code)

    # convert post request into a json
    response_json = create_new_country.json()

    # get country name from service
    country_name = response_json['name']

    # get country 2 digits code from service
    country_2digits_code = response_json['alpha2_code']

    # get country 3 digits code from service
    country_3digits_code = response_json['alpha3_code']

    # assert that the new country name is created correctly
    assert (get_random_country_name == country_name), "New country name was not created correctly"

    # assert that the new country 2 digits code is created correctly
    assert (get_random_country_2code == country_2digits_code), "New country 2 digits code was not created correctly"

    # assert that the new country 3 digits code is created correctly
    assert (get_random_country_3code == country_3digits_code), "New country 3 digits code was not created correctly"
