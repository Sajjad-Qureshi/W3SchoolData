from w3School_github.GeneralThings.HelperClass import Helper
from w3School_github.GeneralThings.Models import ReferenceModel


class Data:

    def headings_sub_headings(self):

        help = Helper("https://www.w3schools.com/")

        try:
            reference_btn = help.getElement("//a[@title='References']", "xpath")
            help.clickElement("//a[@title='References']", "xpath")
        except:
            print("Invalid Locator/Type or Element does not exist (At least till now)")

        try:
            programming_element = help.getElement("//nav[@id='nav_references']//h3[text()='Programming']", "xpath")
            print("..." + help.getElementText("//nav[@id='nav_references']//h3[text()='Programming']", "xpath") + "...")
        except:
            print("Invalid Locator/Type or Element does not exist (At least till now)")

        try:
            reference_elements = help.getListOfElementText(
                "//nav[@id='nav_references']//h3[text()='Programming']//following-sibling::a", "xpath")
            for element in reference_elements:
                print(element)
        except:
            print("Invalid Locator/Type or Elements do not exist (At least till now)")

        try:
            element_to_click = help.getElement("//nav[@id='nav_references']//a[text()='Python Reference']",
                                               "xpath")
            help.clickElement("//nav[@id='nav_references']//a[text()='Python Reference']", "xpath")
        except:
            print("Invalid Locator/Type or Elements do not exist (At least till now)")

        try:
            # Waiting for Div element to load
            wait = help.waitForElementToBeVisible("leftmenuinnerinner", "id")
        except:
            print("Invalid Locator/Type or Elements do not exist (At least till now)")

        # Returning Objects
        try:
            objnum = 1
            objects = []

            headings = help.getListOfElementText("//div[@class='top10']//h5", "xpath")

            for heading in headings:
                a_tags_xpath = f"//div[@class='top10' and .//h5[text()='{heading}']]/a"

                sub_headingText = help.getListOfElementText(a_tags_xpath, "xpath")
            # In case if a tag does not have any text
                sub_headingText = [text for text in sub_headingText if text != ""]

                sub_headingLink = []

                for text in sub_headingText:
                    link = help.getElementAttributeText("//a[text()='{}']".format(text), "href", "xpath")
                    sub_headingLink.append(link)

                for i in range(len(sub_headingText)):

                    if sub_headingText[i] != heading:

                        model = ReferenceModel()
                        model.itemId = objnum
                        model.heading = heading
                        model.sub_heading = sub_headingText[i]
                        model.link = sub_headingLink[i]

                        objnum += 1
                        objects.append(model)
            return objects
        except:
            print("Invalid Locator or Type")
