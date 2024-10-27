from tests.test_home import *
from tests.test_blogs import *
# Run the test
if __name__ == "__main__":
    #run test case 001
    #asyncio.run(testcase001_check_about_us_page())

    #asyncio.run(test_scenario_001())     #For demo without test report

    #subprocess.run(["npx", "playwright", "test", "--reporter=html"])
    #run all regression test case
    # pytest - m  regression

#==============================================================================

    # Run tests and generate allure results
    subprocess.run(["pytest", "--alluredir=allure-results"])
    # Generate and open the Allure report
    subprocess.run(["allure", "serve", "allure-results"])
