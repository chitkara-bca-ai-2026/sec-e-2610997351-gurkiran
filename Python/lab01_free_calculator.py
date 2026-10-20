#Student Fee Calculator
Tutionfee=int(input("Enter Tution Fee: "))
Labfee=int(input("Enter Lab Fee: "))
Libraryfee=int(input("Enter Library Fee: "))
Examfee=int(input("Enter Exam fee: "))
Discount=int(input("Enter Discount Amount: "))
Total=Tutionfee+Labfee+Libraryfee+Examfee
Discount1=Total-Discount
Annualfee=Discount1*2
Monthly=Annualfee/12
print(f"Tution Fee: {Tutionfee:.2f}")
print(f"Lab Fee: {Labfee:.2f}")
print(f"Library Fee: {Libraryfee:.2f}")
print(f"Exam Fee: {Examfee:.2f}")
print(f"Total Fee: {Total:.2f}")
print(f"Discount: {Discount:.2f}")
print(f"Fee after Discount: {Discount1:.2f}")
print(f"Annual Fee: {Annualfee:.2f}")
print(f"Monthly Installment: {Monthly:.2f}")

      


