from flat import Bill, Flatmate
from report import PdfReport

ip_amount= float(input("Enter the bill amount: "))
ip_period = str(input("Enter the Month and Year: "))

flatmate1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {flatmate1} stayed in house during the bill period? "))


flatmate2 = input("What is other flatmate name? ")
days_in_house2 = int(input(f"How many days did {flatmate2} stayed in house during the bill period? "))

the_bill = Bill(amount=ip_amount, period=ip_period)
name1 = Flatmate(name=flatmate1, days_in_house=days_in_house1)
name2 = Flatmate(name=flatmate2, days_in_house=days_in_house2)

print(f"{flatmate1} pays: ",name1.pays(bill = the_bill, guest = name2))
print(f"{flatmate2} pays: ",name2.pays(bill = the_bill, guest = name1))

pdf_report = PdfReport(filename="Flatmates_bill.pdf")
pdf_report.generate(flatmate1 = name1, flatmate2 = name2, bill = the_bill)