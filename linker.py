#for ABCBIRDS
import openpyxl
import os
class Linker:
    '''
    This class was made to grab links from an excell sheet,
    and to add notes to it like the new link or the status
    '''
    def __init__(self): #wb is the excel workbook name
        self.wb= openpyxl.load_workbook('links.xlsx')
        #print(self.fileName)
        self.sheet = self.wb.get_sheet_by_name('Sheet1')
        #print('------"%s" has been selected------' % (self.sheet.title))
        #print(self.sheet['A1045'].value)
        self.rowNum = 1;

    def sheetTitle(self):
        print(self.sheet.title)

    def getNextLink(self):
        self.rowNum += 1
        return self.sheet['A' + str(self.rowNum)].value

    def addNote(self, note):
        self.sheet['D' + str(self.rowNum)].value = note;
        return note;

    def save(self):
        self.wb.save('links-updated.xlsx')

    def length(self):
        self.startRow = self.rowNum;
        self.current = self.getNextLink()
        while not self.current is None:
            self.current = self.getNextLink()
        self.temp2 = self.rowNum
        self.rowNum = self.startRow
        return self.temp2 - 1
