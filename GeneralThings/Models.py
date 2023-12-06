class ReferenceModel:

    itemId = None
    heading = ""
    sub_heading = ""
    link = ""


class GCell:

    def __init__(self, r, c, v):

        self.row = r
        self.col = c
        self.value = v


class ControllerReference:

    def __init__(self, workbook, sheetName):
        self.worksheet = workbook.worksheet(sheetName)

    def loadData(self):

        contents = self.worksheet.get_all_records()
        objected_list = []

        for dic in contents:
            json_model = ReferenceModel()
            json_model.itemId = dic["ItemId"]
            json_model.heading = dic["Heading"]
            json_model.sub_heading = dic["Sub-Heading"]
            json_model.link = dic["Link"]

            objected_list.append(json_model)

        return objected_list

    def format_cells(self, tupleslist):
        format_cell_ranges(self.worksheet, tupleslist)

    def green_format(self):

        green = cellFormat(
            backgroundColor=color(0.0, 0.7, 0.0),
            textFormat=textFormat(bold=True, foregroundColor=color(0, 0, 0)),
            horizontalAlignment='CENTER')

        return green

    def red_format(self):

        red = cellFormat(
            backgroundColor=color(0.7, 0.0, 0.0),
        textFormat = textFormat(bold=True, foregroundColor=color(0, 0, 0)),
            horizontalAlignment='CENTER')

        return red


def authorize(credfileName, workbookName):
    connection = gspread.service_account(credfileName)

    workbook = connection.open(workbookName)

    return workbook


class Reference_validation_props:
    itemId = "A"
    heading = "B"
    sub_heading = "C"
    link = "D"
