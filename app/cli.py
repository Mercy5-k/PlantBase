"""CLI application for managing planters in PlantBase."""
from tabulate import tabulate
import textwrap
from models.base import session, Base, engine
from models.planter import Planter

def wrap_text(text, width=15):
    """Wrapping text to a specified width for better display in tables."""
    return textwrap.fill(str(text), width=width)

def main_menu():
    """Main loop for the CLI application."""

    # Ensure all tables are created in the database
    Base.metadata.create_all(engine)

    while True:
        # Display menu options to the user
        print("\n🌳 PlantBase Main Menu")
        print("1. Add Planter")
        print("2. View All Planters")
        print("3. Update a Planter")
        print("4. Delete a Planter")
        print("0. Exit")

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
            if not planters:
                print("📭 No planters found yet")
            else:
                table_data = []
                for p in planters:
                    row = [
                        p.id,
                        wrap_text(p.name),
                        wrap_text(p.location),
                        wrap_text(p.contact_info),
                        wrap_text(p.plant_type),
                        wrap_text(p.experience_level),
                        f"{p.experience_months} months",
                        wrap_text(p.farm_size),
                        wrap_text(p.preferred_tools, width=25),
                        p.created_at.strftime("%Y-%m-%d %H:%M")
                    ]
                    table_data.append(row)

                print("\n🌿 List of Planters:")
                print(tabulate(
                    table_data,
                    headers=[
                        "ID", "Name", "Location", "Contact", "Plant Type",
                        "Exp Level", "Exp Time", "Farm Size", "Tools", "Created At"
                    ],
                    tablefmt="fancy_grid"
                ))

        elif choice == "3":
            planter_id_input = input("Enter the ID of the planter to update: ").strip()
            if not planter_id_input.isdigit():
                print("❌ Invalid input. Please enter a valid numeric ID.")
                continue

            planter_id = int(planter_id_input)
            planter = Planter.get_by_id(planter_id)

            if planter:
                print(f"Editing {planter.name}. Leave field empty to keep current value.")
                name = input(f"Name [{planter.name}]: ") or planter.name
                location = input(f"Location [{planter.location}]: ") or planter.location
                contact_info = input(f"Contact [{planter.contact_info}]: ") or planter.contact_info
                plant_type = input(f"Plant Type [{planter.plant_type}]: ") or planter.plant_type
                experience_level = input(f"Experience Level [{planter.experience_level}]: ") or planter.experience_level
                experience_months_input = input(f"Experience Months [{planter.experience_months}]: ") or str(planter.experience_months)
                farm_size = input(f"Farm Size [{planter.farm_size}]: ") or planter.farm_size
                preferred_tools = input(f"Preferred Tools [{planter.preferred_tools}]: ") or planter.preferred_tools

                try:
                    experience_months_value = int(experience_months_input)
                except ValueError:
                    experience_months_value = planter.experience_months

                planter.update(
                    name=name,
                    location=location,
                    contact_info=contact_info,
                    plant_type=plant_type,
                    experience_level=experience_level,
                    experience_months=experience_months_value,
                    farm_size=farm_size,
                    preferred_tools=preferred_tools
                )
                print(f"✅ Planter {planter.name} was updated successfully!")
            else:
                print("❌ Planter not found.")

        elif choice == "4":
            planter_id_input =input("Enter the ID of the planter to delete: ").strip()
            if not planter_id_input.isdigit():
                print("❌ Invalid input. Please enter a valid numeric ID.")
                continue

            planter_id = int(planter_id_input)
            planter = Planter.get_by_id(planter_id)

            if planter:
                planter.delete()
                print(f"🗑️ Planter {planter.name} was deleted successfully!")
            else:
                print("❌ Planter not found.")

        elif choice == "0":
            print("👋 Exiting PlantBase. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
