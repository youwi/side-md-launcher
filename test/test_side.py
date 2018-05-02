from selenium import webdriver

from robot_md_launcher import SeleniumIDERunner

driver = webdriver.Chrome()
# SeleniumIDERunner.read_side_json_v1("json_v1.side", driver)


SeleniumIDERunner.run_markdown_file("./test_example.md", driver)
