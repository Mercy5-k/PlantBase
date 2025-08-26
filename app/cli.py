"""CLI application for managing planters in PlantBase."""
from tabulate import tabulate
from models.base import session, Base, engine
from models.planter import Planter

def main_menu():
    """Main loop for the CLI application."""

    # Ensure all tables are created in the database
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
            plant_type = input("Enter plant type (crops/flowers/trees): ")
            experience_level = input("Enter experience level (beginner/intermediate/expert): ")
            experience_months = int(input("Enter experience in months: "))
            farm_size = input("Enter farm size (e.g. '4 acres', garden, 'forest'): ")
            preferred_tools = input("Enter preferred tools (comma-separated): ")

            # Create new planter object and add it to the database
            new_planter = Planter(
                name=name,
                location=location,
                contact_info=contact,
                plant_type=plant_type,
                experience_level=experience_level,
                experience_months=experience_months,
                farm_size=farm_size,
                preferred_tools=preferred_tools,
                )
            
            session.add(new_planter)
            session.commit()

            print(f"✅ Planter {name} was added successfully!")

        elif choice == "2":
            # Retrieve all planters from the database
            planters = session.query(Planter).all()

            # Loop that prints each planter one by one
            if not planters:
                print("📭 No planters found yet")
            else:
                 table = [
                    [
                        p.id, p.name, p.location, p.contact_info,
                        p.plant_type, p.experience_level,
                        f"{p.experience_months} months",
                        p.farm_size, p.preferred_tools,
                        p.created_at.strftime("%Y-%m-%d %H:%M")
                    ]
            for p in planters
                 ]
                 print("\n🌿  List of Planters:")
                 print(tabulate(
                    table,
                    headers=[
                        "ID", "Name", "Location", "Contact", "Plant Type",
                        "Exp Level", "Exp Time", "Farm Size", "Tools", "Created At"
                    ],
                    tablefmt="fancy_grid"
                ))

        elif choice == "3":
            print("👋 Exiting PlantBase. Goodbye!")
            break

        else:
            # Handle invalid input
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
