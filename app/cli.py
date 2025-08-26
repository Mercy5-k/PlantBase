"""CLI application for managing planters in PlantBase."""

from models.base import session, Base, engine   # import Base + engine
from models.planter import Planter


def main_menu():
    """Main loop for the CLI application."""

    # Ensure all tables are created before we do anything
    Base.metadata.create_all(engine)

    while True:
        # Display menu options to the user
        print("\n🌳 PlantBase Main Menu")
        print("➕ 1. Add Planter")
        print("📋 2. View Planters")
        print("🚪 3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            # Collect planter details from the user
            name = input("Enter planter name: ")
            location = input("Enter planter location: ")
            contact = input("Enter contact info: ")

            # Create new planter object and add it to the database
            new_planter = Planter(name=name, location=location, contact_info=contact)
            session.add(new_planter)
            session.commit()

            print(f"✅ Planter {name} was added successfully!")

        elif choice == "2":
            # Retrieve all planters from the database
            planters = session.query(Planter).all()

            # Loop that prints each planter one by one
            if not planters:
                print("📭 No planters found yet")
            for p in planters:
                print(f"🌿 {p}")

        elif choice == "3":
            print("👋 Exiting PlantBase. Goodbye!")
            break

        else:
            # Handle invalid input
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
