def emergency_check(disease):

    dangerous = ["Dengue"]

    if disease in dangerous:

        print("\n⚠ EMERGENCY ALERT!")
        print("Visit nearest hospital immediately.")

    else:

        print("\nNo emergency detected.")