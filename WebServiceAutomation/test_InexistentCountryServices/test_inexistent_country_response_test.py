# importing necessary libraries
from Helper.Common.helper import get_specific_country_response
from Helper.Common.helper import get_diff_country_code_from_all_countries


def test_inexistent_country_response():
    # get inexistent country api-endpoint
    inexistent_country = get_specific_country_response(get_diff_country_code_from_all_countries(2))

    # get status code
    inexistent_country_status_code = inexistent_country.status_code

    # extracting inexistent country data in json format
    inexistent_json_country = inexistent_country.json()

    # assert if the inexistent country request service status code is 401
    assert (inexistent_country_status_code == 404), "Status code is different from 404:" \
                                                    " Request status code is " + str(inexistent_country_status_code)

    # assert inexistent country message response
    assert (inexistent_json_country['message'] == "Not Found"), "Message is different from 'Not Found':" \
                                                                " Current message is " + inexistent_json_country[
                                                                'message']
