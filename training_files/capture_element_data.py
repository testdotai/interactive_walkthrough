import logging, json

log = logging.getLogger(__name__)


def run(context):

    # Log marker to show when the script starts:
    log.info('{0} STARTING SCRIPT {0}'.format('*'*50))


    # Capture element with dynamic content
    element = context.find_element('<insert_element_label_here>')

    # Extract text information from the element
    element_text = element['text'].strip() # it's a good idea to trim whitespace from captured elements
    log.info("The text from this element is: {}".format(element_text))

    # use this code to run a basic assertion against the element text
    # assert element_text=="25% Off On All Products", "Offer message doesn't match"

    # Log marker to show when the script ends:
    log.info('{0} ENDING SCRIPT {0}'.format('*'*50))


def run_from_json_file(context):

    # Log marker to show when the script starts:
    log.info('{0} STARTING SCRIPT {0}'.format('*'*50))

    # Capture element with dynamic content
    element = context.find_element('<insert_element_label_here>')

    # Extract text information from the element
    element_text = element['text'].strip() # it's a good idea to trim whitespace from captured elements
    log.info("The text from this element is: {}".format(element_text))

    # open an external json file from the lkg/scripts/ directory
    file_path = context.get_file_path("resources/test_json_data.json")

    # extract data from csv file as JSON:
    json_data = []
    with open(file_path) as file:
        json_data = json.load(file)

    # Extract text information from the element
    validation_text=json_data['expected_offer']
    log.info("The text from this element is: {}".format(validation_text))

    # use this code to compare against json data

    assert element['text'] == json_data['expected_offer'], 'Offer text ({}) does not match expected offer ({})'.format(element_text, validation_text)

    # Log marker to show when the script ends:
    log.info('{0} ENDING SCRIPT {0}'.format('*'*50))


def run_with_dynamic_content(context):

    # Capture element with dynamic content
    element = context.find_element('<insert_element_label_here>', dynamic=True)

    # Extract text information from the element
    element_text = element['text'].strip() # it's a good idea to trim whitespace from captured elements
    log.info("The text from this element is: {}".format(element_text))

    # use this code to run a basic assertion against the element text
    assert element_text=="Welcome auto test (autotst)", "Welcome message doesn't match"


def run_with_params(context):

    # Capture element with dynamic content
    element = context.find_element('<insert_element_label_here>', dynamic=True)

    # Extract text information from the element
    element_text = element['text'].strip() # it's a good idea to trim whitespace from captured elements
    log.info("The text from this element is: {}".format(element_text))

    # use this code to compare against parameterized data
    data = context.get_test_case().get('param_values')
    validation_text = data['{expected_message}']

    assert element_text==validation_text, "Welcome message ({}) doesn't match expected message ({})".format(element_text, validation_text)
