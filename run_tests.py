import os
import sys
import pytest
from datetime import datetime
#from core.base_test import BaseTest            #it should be added?


if __name__ == "__main__":
    arguments = dict()
    for arg in sys.argv[1:]:
        key, value = arg.split('=')
        arguments[key] = value

    # Create directory for the report
    directory = 'allure-report/' + datetime.today().strftime("%Y-%m-%d_%H-%M-%S")
    if not os.path.exists(directory):
        os.makedirs(directory)

    pytest.main('tests/{0} --alluredir {1}/xml'.format(arguments['suite'], directory))
    os.system('allure generate {0}/xml -o {0}/html'.format(directory))