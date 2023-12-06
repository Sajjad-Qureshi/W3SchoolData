from w3School_github.Data_Scrapping import Data
from w3School_github.GeneralThings.Models import *


class Validation:

    def validating(self):

        try:
            # W3School RealTime Objects
            w3 = Data()
            w3_objects = w3.headings_sub_headings()

            # Google Sheets Objects
            worksheet = ControllerReference(authorize("creds.json", "Task"), "W3School")
            sheet_objects = worksheet.loadData()

            # Color Formats
            green = worksheet.green_format()
            red = worksheet.red_format()

            validation_props = Reference_validation_props()
            green_red_tuples = []

            for g_obj in sheet_objects:

                w3_instance_record = [w3_obj for w3_obj in w3_objects if w3_obj.heading == g_obj.heading]

                if len(w3_instance_record) > 0:
                    # Green Heading Cells
                    green_red_tuples.append((f"{validation_props.heading}{int(g_obj.itemId)+1}", green))

                    sub_heading = [sub_head for sub_head in w3_instance_record if sub_head.sub_heading == g_obj.sub_heading]

                    if len(sub_heading) > 0:
                        green_red_tuples.append((f"{validation_props.sub_heading}{int(g_obj.itemId)+1}", green))

                        link = [link for link in sub_heading if link.link == g_obj.link]

                        if len(link) > 0:
                            green_red_tuples.append((f"{validation_props.link}{int(g_obj.itemId)+1}", green))
                        else:
                            green_red_tuples.append((f"{validation_props.link}{int(g_obj.itemId)+1}", red))

                    else:
                        green_red_tuples.append((f"{validation_props.sub_heading}{int(g_obj.itemId)+1}", red))

                else:
                    green_red_tuples.append((f"{validation_props.heading}{int(g_obj.itemId)+1}", red))

            worksheet.format_cells(green_red_tuples)
        except:
            print("Invalid Cred/Workbook/Sheet Name")


checking = Validation()
checking.validating()
