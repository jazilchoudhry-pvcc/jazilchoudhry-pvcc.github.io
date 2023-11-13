# Name: Jazil Choudhry
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats

# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia

# PET CARE MEDS Pricing
#------------------
# Canine Vaccines:
# 1.Bordatella $30.00
# 2.DAPP $35.00
# 3.Int luenza $48.00
# 4.Leptospirosis $21.00
# 5.Lyme Disease $41.00
# 6.Rabies $25.00
# 7.Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
# Small dogs, Up to 25 bs:_s9;99
# Medium-sized dogs, 26 to 50 Ibs: $11.99
# Large dogs: 51 to 100 lbs: $13.99

import datetime

############## define global variables ############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48

PR_ALL = 0
PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

#define global variables

############## define program functions ################
def main():
    more = True
    while more:
        get_user_data ()
        
        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations ()
            display_cat_results ()
            
        askAgain = input("\nwould you like process another pet (Y/N)?: ")
        if askAgain.upper () == "N" :
            more= False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")
def get_user_data():
        global pet_name, pet_type, pet_weight
        pet_name = input("Pet name: ")
        pet_type = input("Is this pet a dog (D) or cat (C)?" )
        pet_weight = int(input("Weight of your pet (in pounds): "))




############ DOG functions ###############

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1. Bordatella \n\t2.DAPP \n\t3.Influenza\n\t4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies\n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu = dog1+dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs. ")
    heart_yesno = input (f"\tWould you like to order monthly heartworm medication for " + pet_name + " (Y/N)?")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("\How many heart worms chews would you like to order? "))
        
        def perform_dog_calculations():
            global vax_cost, vax_name, chews_cost, total

            ######### vaccines
            if pet_vax_type ==1 :
                vax_cost= PR_BORD
                vax_name = "Bordatella"
            elif pet_vax_type ==2:
                vax_cost= PR_DAPP
                vax_name = "DAPP"
            elif pet_vax_type ==3:
                vax_cost = PR_FLU
                vax_name = "Influenza"
            else:
                PR_ALL = PR_BORD + PR_DAPP + PR_FLU
                vax_cost = .85 * PR_ALL
                vax_name = "FULL Vax Package"
            #### heart worm chews
            if num_chews != 0:
                if pet_weight < 25:
                    chews_cost = num_chews * PR_CHEWS_SMALL
                elif 25 <= pet_weight < 51:
                    chews_cost = num_chews * PR_CHEWS_MED
            else:
                chews_cost = num_chews * PR_CHEWS_LARGE
        ######find total
        total= vax_cost+ chews_cost
                

        def display_dog_results():
            # Display company name
            print("\nPET CARE MEDS")

            #Display vaccine details
            print("\nVaccine Details: ")
            print(f"Pet Name: {pet_name}")
            print(f"Vaccine Type: {vax_name}")
    print(f"Vaccine Cost: ${vax_cost:.2f}")

    # Display heartworm chews details
    if num_chews != 0:
        print(f"\nHeartworm Chews:")
        print(f"Number of Chews: {num_chews}")
        print(f"Chews Cost: ${chews_cost:.2f}")

    # Display total amount
    print("\nTotal Amount:")
    print(f"Total Cost: ${total:.2f}")

    # Display date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nDate: " + current_date)
            

############ Cat functions #############
def get_cat_data():
    global pet_vax_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1. Feline Leukemia \n\t2. Feline Viral Rhinotracheitis \n\t3. Rabies"
    cat2 = "\n\t4. Full Vaccine Package \n\t5. NONE"
    catmenu = cat1 + cat2
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heartworm prevention medication is recommended for all cats. ")
    heart_yesno = input("\tWould you like to order monthly heartworm medication for " + pet_name + " (Y/N)?")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))


def perform_cat_calculations():
    global vax_cost, vax_name, chews_cost, total

    ######### vaccines
    if pet_vax_type == 1:
        vax_cost = 35  # Feline Leukemia
        vax_name = "Feline Leukemia"
    elif pet_vax_type == 2:
        vax_cost = 30  # Feline Viral Rhinotracheitis
        vax_name = "Feline Viral Rhinotracheitis"
    elif pet_vax_type == 3:
        vax_cost = 25  # Rabies
        vax_name = "Rabies"
    else:
        vax_cost = (35 + 30 + 25) * 0.9  # Full Vaccine Package with 10% discount
        vax_name = "FULL Vax Package"
        #### heartworm chews
    if num_chews == 0:
        chews_cost = num_chews * 8.00

    ###### find total
    total = vax_cost + chews_cost


def display_cat_results():
    # Display company name
    print("\nPET CARE MEDS")

    # Display vaccine details
    print("\nVaccine Details:")
    print(f"Pet Name: {pet_name}")
    print(f"Vaccine Type: {vax_name}")
    print(f"Vaccine Cost: ${vax_cost:.2f}")

    # Display heartworm chews details
    if num_chews != 0:
        print("\nHeartworm Chews:")
        print(f"Number of Chews: {num_chews}")
        print(f"Chews Cost: ${chews_cost:.2f}")

    # Display total amount
    print("\nTotal Amount:")
    print(f"Total Cost: ${total:.2f}")

    # Display date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nDate: " + current_date)


############## call on main program to execute ###############
main()
    
























        
