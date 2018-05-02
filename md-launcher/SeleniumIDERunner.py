"""
SeleniumIDE file is html table

support :
side json format
html table format
v split table format "|"

example json
{
    "tests": [
        {
            "id": "8662afd4-3629-4338-a416-903edce0342c",
            "name": "Untitled",
            "commands": [
                {
                    "id": "d985f26f-b7c0-4fc1-9a56-7aec000a9fd1",
                    "comment": "",
                    "command": "open",
                    "target": "/",
                    "value": ""
                },
        }
    ]
}
"""
import json
import re

from selenium.webdriver import ActionChains


class SeleniumIDERunner:
    GLOBAL = {}

    @staticmethod
    def locateBy(location):
        emitters = {
            "id": "id",
            "name": "name",
            "link": "link text",
            "css": "css selector",
            "xpath": "xpath"
        }
        # ID = "id"
        # XPATH = "xpath"
        # LINK_TEXT = "link text"
        # PARTIAL_LINK_TEXT = "partial link text"
        # NAME = "name"
        # TAG_NAME = "tag name"
        # CLASS_NAME = "class name"
        # CSS_SELECTOR = "css selector"
        fragments = location.split("=")
        type = fragments.pop(0)
        selector = "=".join(fragments)
        try:
            by = emitters[type]
        except Exception:
            by = selector

        return {"by": by, "key": selector}

    def hump2underline(hunp_str):
        """
        驼峰形式字符串转成下划线形式
        :param hunp_str: 驼峰形式字符串
        :return: 字母全小写的下划线形式字符串
        """
        # 匹配正则，匹配小写字母和大写字母的分界位置
        p = re.compile(r'([a-z]|\d)([A-Z])')
        # 这里第二个参数使用了正则分组的后向引用
        sub = re.sub(p, r'\1_\2', hunp_str).lower()
        return sub

    @staticmethod
    def markdown_to_json(txt):
        # txt = open("../Web/test_example.md", 'r').read()
        arr = txt.split("\n")

        test_cases = []
        current_case = {"name": "example", "commands": []}
        project = {"name": "build", "tests": test_cases, "url": ""}

        for line in arr:
            command = {}
            if line.startswith("# "):
                project['name'] = line.replace("# ", "")
            if line.startswith("## "):
                current_case['name'] = line.replace("## ", "")

            if line.startswith("|"):
                items = line.split("|")

                if "---" in items[1]:
                    commands = []
                    current_case = {"name": "example", "commands": []}
                    test_cases.append(current_case)
                    continue
                command['command'] = items[1].strip()
                command['target'] = items[2].strip()
                command['value'] = items[3].strip()
                if command['command'] == 'url' or command['command'] == 'root':
                    project['url'] = command['target']
                    project['root'] = command['target']
                if command['command'] == "" and command['value'] == "" and command['target'] == "":
                    continue
                # if command['command'] == 'open':
                #   command['target'] += project['root']

                current_case['commands'].append(command)
        return project

    @staticmethod
    def read():
        print("step do nothing\n")

    @staticmethod
    def read_side_json_v1(file_name, driver):
        txt = open(file_name, 'r').read()
        obj = json.loads(txt)
        SeleniumIDERunner.run_project(obj, driver)

    @staticmethod
    def run_project(obj, driver):
        for case in obj['tests']:
            for command in case['commands']:
                if command['command'] == 'open':
                    command['target'] = obj['url'] + command['target']
                SeleniumIDERunner.do_command(driver, command)

    @staticmethod
    def run_side_file(file_name, driver):
        txt = open(file_name, 'r').read()
        obj = json.loads(txt)
        SeleniumIDERunner.run_project(obj, driver)

    @staticmethod
    def run_markdown_file(file_name, driver):
        txt = open(file_name, 'r').read()
        obj = SeleniumIDERunner.markdown_to_json(txt)
        SeleniumIDERunner.run_project(obj, driver)

    @staticmethod
    def do_nothing():
        print("step do nothing\n")

    @staticmethod
    def do_command(driver, command):
        func = getattr(SeleniumIDERunner, SeleniumIDERunner.hump2underline(command['command'].replace(" ", "_")))
        loc = SeleniumIDERunner.locateBy(command['target'])
        print(command)
        if command['command'] in ['open', '']:
            func(driver, command['target'], command['value'])
            return

        try:
            element = driver.find_element(loc['by'], loc['key'])
        except Exception as e:
            print(e.msg + str(command))
            element = command['target']

        func(driver, element, command['value'])

    @staticmethod
    def add_selection(driver, element, value):
        # TODO
        return SeleniumIDERunner.do_nothing()

    @staticmethod
    def answer_on_next_prompt(driver, element, value):
        alert = driver.switchTo().alert()
        alert.accept()

    @staticmethod
    def assert_alert(driver, element, value):
        alert = driver.switchTo().alert()
        alert.accept()

    @staticmethod
    def assert_checked(driver, element, value):
        assert element.is_selected()

    @staticmethod
    def assert_not_checked(driver, element, value):
        assert not element.is_selected()

    @staticmethod
    def assert_confirmation(driver, element, value):
        alert = driver.switchTo().alert()
        assert value == alert.getText()

    @staticmethod
    def assert_editable(driver, element, value):
        element.is_enabled()
        assert element.get_attribute("readonly")

    @staticmethod
    def assert_not_editable(driver, element, value):
        element.is_enabled()
        assert not element.get_attribute("readonly")

    @staticmethod
    def assert_element_present(driver, element, value):
        assert element.length > 0

    @staticmethod
    def assert_element_not_present(driver, element, value):
        assert element.length == 0

    @staticmethod
    def assert_prompt(driver, element, value):
        assert value == driver.switchTo().alert().getText()

    @staticmethod
    def assert_selected_value(driver, element, value):
        assert element.getAttribute("value") == value

    @staticmethod
    def assert_not_selected_value(driver, element, value):
        assert element.getAttribute("value") != value

    @staticmethod
    def assert_text(driver, element, value):
        assert element.get_text() == value

    @staticmethod
    def assert_title(driver, element, value):
        assert driver.get_title() == value

    @staticmethod
    def assert_value(driver, element, value):
        assert element.get_value() == value

    @staticmethod
    def choose_cancel_on_next_confirmation(driver, element, value):
        driver.switchTo().alert().dismiss()

    @staticmethod
    def choose_cancel_on_next_prompt(driver, element, value):
        alert = driver.switchTo().alert()
        alert.sendKeys(value)
        alert.accept()

    @staticmethod
    def choose_ok_on_next_confirmation(driver, element, value):
        driver.switchTo().alert().accept()

    @staticmethod
    def click(driver, element, value):
        element.click()

    @staticmethod
    def click_at(driver, element, value):
        element.click()

    @staticmethod
    def double_click_at(driver, element, value):
        driver.actions().doubleClick(element).perform()

    @staticmethod
    def drag_and_drop_to_object(driver, element, value):
        to_object = driver.findElement(value)
        driver.actions().dragAndDrop(element, to_object).perform()

    @staticmethod
    def echo(driver, element, value):
        print(value)

    @staticmethod
    def edit_content(driver, element, value):
        driver.executeScript("if(arguments[0].contentEditable === 'true') {arguments[0].innerHTML = '{}'}".format(value))

    @staticmethod
    def mouse_down_at(driver, element, value):
        driver.actions().mouseDown(element).perform()

    @staticmethod
    def mouse_move_at(driver, element, value):
        driver.actions().mouseDown(element).perform()

    @staticmethod
    def mouse_out(driver, element, value):
        size = element.size
        offsetx = (size['width'] / 2) + 1
        offsety = (size['height'] / 2) + 1
        action = ActionChains(driver)
        action.move_to_element(element).move_by_offset(offsetx, offsety)

        # driver.actions().mouseOut(element).perform()

    @staticmethod
    def mouse_over(driver, element, value):
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def mouse_up_at(driver, element, value):
        ActionChains(driver).release(element).perform()

    @staticmethod
    def open(driver, element, value):
        driver.get(element)

    @staticmethod
    def pause(driver, element, value):
        from time import sleep
        sleep(value)

    @staticmethod
    def remove_selection(driver, element, value):
        element.click()

    @staticmethod
    def run_script(driver, element, value):
        driver.execute_script(value)

    @staticmethod
    def select(driver, element, value):
        element.option.click()

    @staticmethod
    def select_frame(driver, element, value):
        driver.switchTo().frame(value)

    @staticmethod
    def select_window(driver, element, value):
        driver.switchTo().window(value)

    @staticmethod
    def send_keys(driver, element, value):
        element.send_keys(value)

    @staticmethod
    def set_speed(driver, element, value):
        SeleniumIDERunner.do_nothing()

    @staticmethod
    def store(driver, element, value):
        # driver.execute_script("var {} = '{}';".format(element, value))
        SeleniumIDERunner.GLOBAL[element] = value

    @staticmethod
    def store_text(driver, element, value):
        SeleniumIDERunner.GLOBAL[value] = element.get_text()

    @staticmethod
    def store_title(driver, element, value):
        SeleniumIDERunner.GLOBAL[value] = element.get_text()

    @staticmethod
    def submit(driver, element, value):
        element.submit()

    @staticmethod
    def type(driver, element, value):
        element.send_keys(value)

    @staticmethod
    def verify_checked(driver, element, value):
        assert element.is_selected(value)

    @staticmethod
    def verify_not_checked(driver, element, value):
        assert not element.is_selected(value)

    @staticmethod
    def verify_editable(driver, element, value):
        assert element.is_enabled() or element.get_attribute("readonly")

    @staticmethod
    def verify_not_editable(driver, element, value):
        assert not (element.is_enabled() or element.get_attribute("readonly"))

    @staticmethod
    def verify_element_present(driver, element, value):
        assert element is not None

    @staticmethod
    def verify_element_not_present(driver, element, value):
        assert element is None

    @staticmethod
    def verify_selected_value(driver, element, value):
        assert element.get_attribute("value") == value

    @staticmethod
    def verify_not_selected_value(driver, element, value):
        assert element.get_attribute("value") != value

    @staticmethod
    def verify_text(driver, element, value):
        assert element.get_text() == value

    @staticmethod
    def verify_title(driver, element, value):
        assert element.get_title() == value

    @staticmethod
    def verify_value(driver, element, value):
        assert element.get_attribute("value") == value

    @staticmethod
    def webdriver_answer_on_next_prompt(driver, element, value):
        SeleniumIDERunner.answer_on_next_prompt(driver, element, value)

    @staticmethod
    def webdriver_choose_cancel_on_next_confirmation(driver, element, value):
        SeleniumIDERunner.answer_on_next_prompt(driver, element, value)

    @staticmethod
    def webdriver_choose_cancel_on_next_prompt(driver, element, value):
        SeleniumIDERunner.choose_cancel_on_next_prompt(driver, element, value)

    @staticmethod
    def webdriver_choose_ok_on_next_confirmation(driver, element, value):
        SeleniumIDERunner.choose_ok_on_next_confirmation(driver, element, value)
