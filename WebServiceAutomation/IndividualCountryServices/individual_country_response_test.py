# importing necessary libraries
from Helper.Common.helper import get_all_countries_response
from Helper.Common.helper import get_country_from_all_countries
from Helper.Common.helper import get_specific_country_response


def test_all_countries_status_code():
    get_status_code = get_all_countries_response().status_code

    # assert if the all countries request service status code is 200
    assert (get_status_code == 200), "Status code is different from 200:" \
                                     " Request status code is " + str(get_status_code)


def test_de_country_response_data_validation():
    # get DE response inside all countries service
    de_response_from_all_countries = get_country_from_all_countries("DE")

    # get the specific country URL from '/alpha'
    de_alpha_response = get_specific_country_response(de_response_from_all_countries['alpha2Code'])

    # assert if the US request service status code is 200
    assert (de_alpha_response.status_code == 200), "Status code is different from 200:" \
                                                   " Request status code is " + str(de_alpha_response.status_code)

    # extracting DE data in json format
    de_alpha_json_response = de_alpha_response.json()

    # assert if the DE response data inside all countries service is similar
    # to the DE response data inside '/alpha/de' service
    assert (de_response_from_all_countries == de_alpha_json_response), "Responses data between '/all' service and " \
                                                                       "'/alpha/de' service are different"

    # assert that the population for DE inside all countries service is more than 0
    assert (de_response_from_all_countries[
                'population'] > 0), "DE population for all countries service is 0 or less than 0"

    # assert that the population for DE inside 'alpha/de' service is more than 0
    assert (de_alpha_json_response['population'] > 0), "DE population for 'alpha/de' service is 0 or less than 0"

    # FIXME: print to show that the DE alpha service response is handled correctly
    print(de_alpha_json_response)


def test_gb_country_response_data_validation():
    # get GB response inside all countries service
    gb_response_from_all_countries = get_country_from_all_countries("GB")

    # get the specific country URL from '/alpha'
    gb_alpha_response = get_specific_country_response(gb_response_from_all_countries['alpha2Code'])

    # assert if the GB request service status code is 200
    assert (gb_alpha_response.status_code == 200), "Status code is different from 200:" \
                                                   " Request status code is " + str(gb_alpha_response.status_code)

    # extracting GB data in json format
    gb_alpha_json_response = gb_alpha_response.json()

    # assert if the GB response data inside all countries service is similar
    # to the DE response data inside '/alpha/gb' service
    assert (gb_response_from_all_countries == gb_alpha_json_response), "Responses data between '/all' service and " \
                                                                       "'/alpha/gb' service are different"

    # assert that the population for DE inside all countries service is more than 0
    assert (gb_response_from_all_countries[
                'population'] > 0), "GB population for all countries service is 0 or less than 0"

    # assert that the population for DE inside 'alpha/de' service is more than 0
    assert (gb_alpha_json_response['population'] > 0), "GB population for 'alpha/gb' service is 0 or less than 0"

    # FIXME: print to show that the GB alpha service response is handled correctly
    print(gb_alpha_json_response)


def test_us_country_response_data_validation():
    # get US response inside all countries service
    us_response_from_all_countries = get_country_from_all_countries("US")

    # get the specific country URL from '/alpha'
    us_alpha_response = get_specific_country_response(us_response_from_all_countries['alpha2Code'])

    # assert if the US request service status code is 200
    assert (us_alpha_response.status_code == 200), "Status code is different from 200:" \
                                                   " Request status code is " + str(us_alpha_response.status_code)

    # extracting US data in json format
    us_alpha_json_response = us_alpha_response.json()

    # assert if the US response data inside all countries service is similar
    # to the US response data inside '/alpha/us' service
    assert (us_response_from_all_countries == us_alpha_json_response), "Responses data between '/all' service and " \
                                                                       "'/alpha/us' service are different"

    # assert that the population for US inside all countries service is more than 0
    assert (us_response_from_all_countries[
                'population'] > 0), "US population for all countries service is 0 or less than 0"

    # assert that the population for US inside 'alpha/us' service is more than 0
    assert (us_alpha_json_response['population'] > 0), "US population for 'alpha/us' service is 0 or less than 0"

    # FIXME: print to show that the US alpha service response is handled correctly
    print(us_alpha_json_response)
