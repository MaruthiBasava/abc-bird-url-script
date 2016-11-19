import openpyxl
import os


class Linker:
    '''
    This class was made to grab links from an excell sheet,
    and to add notes to it like the new link or the status
    '''

    def __init__(self):  # wb is the excel workbook name
        self.wb = openpyxl.load_workbook('data.xlsx')
        self.sheet = self.wb.get_sheet_by_name('Sheet1')

        self.rowNum = 1;

    def sheetTitle(self):
        print(self.sheet.title)

    def getNextLink(self):
        self.rowNum += 1
        return self.sheet['A' + str(self.rowNum)].value

    def addNote(self, note):
        self.sheet['D' + str(self.rowNum)].value = note;
        return note;

