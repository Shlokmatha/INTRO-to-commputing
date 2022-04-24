income = int(input('GROSS INCOME: '))
dependents = int(input('NUMBER OF DEPENDENTS: '))
# Taxable income= Gross Income - Standard deduction - (Dependent deduction * No. of dependents)
Taxable_Income = income - 10000 - (3000*dependents)
# Tax = Taxable Income * Tax Rate
Tax = Taxable_Income * 0.2
print(Tax)
