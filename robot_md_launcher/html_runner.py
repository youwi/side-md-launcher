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

from ridexx_commands import RidexxCommands


class SeleniumIDEHtmlRunner:
    """
    side file runner
    """
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
        func = getattr(RidexxCommands, SeleniumIDERunner.hump2underline(command['command'].replace(" ", "_")))
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
