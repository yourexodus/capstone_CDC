from prepare import PrepareData
#Testing - Read local data
prepared_data = PrepareData(download_new=False)


#program will gather user input
while True:
    #Income
    print("\nPlease Choose your income range.\n\n1 - Less than $10,000\n2 - Less than $15,000 ($10,000 to less than $15,000)\n3 - Less than $20,000 ($15,000 to less than $20,000)\n4 - Less than $25,000 ($20,000 to less than $25,000)\n5 - Less than $35,000 ($25,000 to less than $35,000)\n6 - Less than $50,000 ($35,000 to less than $50,000)\n7 - Less than $75,000 ($50,000 to less than $75,000)\n8 - $75,000 or more")
    input_income = input("\nYour income selection: ")

    #GenHlth'
    print("\nPlease enter your general health code.\n\n1 Excellent\n2 Very good\n3 Good\n4 Fair\n5 Poor\n7 Don’t know/Not Sure\n9 Refused")
    input_genhealth = input("\nYour general health selection: ")

    # 'MentHlth'
    print("\nPlease enter your mental health code.\n\n1 - 30 Number of days\n77 Don’t know/Not sure")
    input_menthealth = input("\nYour mental health selection: ")

    # 'PhysHlth'
    print("\nPlease enter your physical health code. \n\n1 - 30 Number of days\n77 Don’t know\n88 None")
    input_phyhealth = input("\nYour physical health selection: ")


    # 'DiffWalk
    print("\nPlease enter number of days you have difficulty walking or climbing stairs. \n\n1 - 30 Number of days\n77 Don’t know\n88 None")
    input_diffwalk = input("\nPlease enter the number of days you have experienced difficulty walking: ")
    all_input_data = [input_income, input_genhealth, input_menthealth, input_phyhealth, input_diffwalk]

    result = prepared_data.make_prediction(all_input_data)
    print(result)

    back = input('\nWould you like to enter new data?(y/n)')

    if back == "y":
      continue
    else:
      break




