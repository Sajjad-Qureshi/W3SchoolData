import gspread
from w3School_github.Data_Scrapping import Data
from w3School_github.GeneralThings.Models import GCell


class GoogleSheets:

    def insert(self):

        try:
            data = Data()
            objects = data.headings_sub_headings()

            listOfLists = [[object.itemId, object.heading, object.sub_heading, object.link] for object in objects]

            # For Google Sheets
            connection = gspread.service_account(filename="creds.json")
            file = connection.open("Task")
            worksheet = file.worksheet("W3School")

            cell_list = []
            for i in range(len(listOfLists)):
                for j in range(len(listOfLists[i])):

                    # Cell Object
                    cell = GCell(i+2, j+1, listOfLists[i][j])
                    cell_list.append(cell)

            # Updating Cells
            worksheet.update_cells(cell_list)
        except:
            print("Something to look up to.")


checking = GoogleSheets()
checking.insert()
