class RidexxCommands:
    """
    side file runner
    """
    GLOBAL = {}

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
        driver.actions().move_to_element(element).move_by_offset(offsetx, offsety)

        # driver.actions().mouseOut(element).perform()

    @staticmethod
    def mouse_over(driver, element, value):
        driver.actions().move_to_element(element).perform()

    @staticmethod
    def mouse_up_at(driver, element, value):
        driver.actions().release(element).perform()

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
