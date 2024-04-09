import flet as ft

class Expense(ft.UserControl):

    def build(self):
        self.expenseName = ft.TextField(value="Unnamed Expense", width= 600, height=60)
        self.minusButton = ft.IconButton(ft.icons.REMOVE, on_click=self.minus, icon_color= ft.colors.INDIGO_900)
        self.plusButton = ft.IconButton(ft.icons.ADD, on_click=self.plus, icon_color= ft.colors.INDIGO_900)
        self.amountSpace = ft.TextField(value="0")
        self.categories =ft.Dropdown(label="Category", height=60, options=[ft.dropdown.Option("Food"), ft.dropdown.Option("Shopping"), ft.dropdown.Option("Transportation"), ft.dropdown.Option("Entertainment"), ft.dropdown.Option("Investments"),],autofocus=True,)
        
        self.mainRow = ft.Row(controls=[self.expenseName, self.minusButton, self.amountSpace, self.plusButton, self.categories], alignment=ft.MainAxisAlignment.CENTER)
        return self.mainRow
    
    def minus(self,e):
        
        actualAmount = int(self.amountSpace.value)
        
        actualAmount-=1
        self.amountSpace.value = str(actualAmount)
        self.amountSpace.update()

    def plus(self,e):
        
        actualAmount = int(self.amountSpace.value)
        
        actualAmount+=1
        self.amountSpace.value = str(actualAmount)
        self.amountSpace.update()

def main(page: ft.Page):
    page.title = "Expense Tracker"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.auto_scroll = True
    page.scroll = ft.ScrollMode.HIDDEN
    page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    expenses = []

    def importExpenses(e):
        with open("Records.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.split("|")
                tempExpense = Expense()
                tempExpense.expenseName = data[0]
                tempExpense.amountSpace = data[1]
                tempExpense.categories = data[2]
                expenses.append(tempExpense)
                page.add(tempExpense)

        page.update()

    def export(e):
        with open("Records.txt", "w") as file:
            for record in expenses:
                file.write(f"{record.expenseName.value} | {record.amountSpace.value} | {record.categories.value} \n")

    def addExpense(e):
        expense = Expense()
        expenses.append(expense)
        expensesColumn.controls.append(expense)
        page.update()

    title = ft.Text(spans=[ft.TextSpan("Expense Tracker", ft.TextStyle(size=50,weight=ft.FontWeight.BOLD,font_family="Kanit", color=ft.colors.INDIGO_900))])
    exportButton = ft.ElevatedButton("Export", on_click=export, bgcolor=ft.colors.ORANGE_600,)
    importButton = ft.ElevatedButton("Import", on_click=importExpenses, bgcolor=ft.colors.ORANGE_600,)
    buttonsRow = ft.Row(controls=[importButton, exportButton], alignment=ft.MainAxisAlignment.CENTER)
    expensesColumn = ft.Column()
    fab = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=addExpense, bgcolor=ft.colors.ORANGE_600,)

    page.add(title, buttonsRow, expensesColumn, fab)

ft.app(target=main)