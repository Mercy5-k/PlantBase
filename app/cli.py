"""Unified CLI Application for PlantBase 🌳"""

from tabulate import tabulate
from models.base import session
from models.planter import Planter
from models.plant import Plant
from models.site import Site
from models.harvest import Harvest
from models.activity import Activity
from utils.helper import wrap_text

# Helper functions
def safe_input(prompt, type_=int):
    """Get validated input of given type."""
    while True:
        try:
            return type_(input(prompt))
        except ValueError:
            print(f"❌ Invalid input. Must be a {type_.__name__}.")

def confirm_action(message):
    """Confirm before performing a destructive action."""
    return input(f"{message} (y/n): ").strip().lower() == "y"

# Greeting
def greet():
    print("\n🌱 Welcome to PlantBase CLI 🌱")
    print("Manage your plants, planters, sites, harvests, and activities easily!\n")

# Main Menu
def main_menu():
    greet()
    while True:
        print("\n🌳 Main Menu")
        print("1. Planters")
        print("2. Plants")
        print("3. Sites")
        print("4. Harvests")
        print("5. Activities")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            planter_menu()
        elif choice == "2":
            plant_menu()
        elif choice == "3":
            site_menu()
        elif choice == "4":
            harvest_menu()
        elif choice == "5":
            activity_menu()
        elif choice == "0":
            print("👋 Goodbye from PlantBase!")
            break
        else:
            print("❌ Invalid choice, try again.")

# Planter Menu
def planter_menu():
    while True:
        print("\n👨‍🌾 Planter Menu")
        print("1. Add Planter")
        print("2. View All Planters")
        print("3. Update Planter")
        print("4. Delete Planter")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter planter name: ")
            location = input("Enter planter location: ")
            contact = input("Enter contact info: ")
            plant_type = input("Enter plant type (crops/flowers/trees): ")
            experience_months = safe_input("Enter experience in months: ", int)
            farm_size = input("Enter farm size (e.g. '4 acres'): ")

            new_planter = Planter(
                name=name,
                location=location,
                contact_info=contact,
                plant_type=plant_type,
                experience_months=experience_months,
                farm_size=farm_size,
            )
            session.add(new_planter)
            session.commit()
            print(f"✅ Planter {name} added successfully!")

        elif choice == "2":
            planters = session.query(Planter).all()
            if not planters:
                print("📭 No planters found.")
            else:
                table = [[
                    p.id, wrap_text(p.name), wrap_text(p.location),
                    wrap_text(p.contact_info), p.plant_type, f"{p.experience_months} months", 
                    wrap_text(p.farm_size), p.created_at.strftime("%Y-%m-%d")
                ] for p in planters]
                print(tabulate(table, headers=["ID", "Name", "Location", "Contact",
                                               "Type", "Exp", "Farm Size", "Created"],              
                               tablefmt="fancy_grid"))

        elif choice == "3":
            planter_id = safe_input("Enter ID to update: ", int)
            planter = Planter.get_by_id(planter_id)
            if planter:
                name = input(f"Name [{planter.name}]: ") or planter.name
                location = input(f"Location [{planter.location}]: ") or planter.location
                contact_info = input(f"Contact Info [{planter.contact_info}]: ") or planter.contact_info
                plant_type = input(f"Plant Type [{planter.plant_type}]: ") or planter.plant_type
                experience_months = safe_input(f"Experience Months [{planter.experience_months}]: ", int) or planter.experience_months
                farm_size = input(f"Farm Size [{planter.farm_size}]: ") or planter.farm_size

                planter.update(
                    name=name,
                    location=location,
                    contact_info=contact_info,
                    plant_type=plant_type,
                    experience_months=experience_months,
                    farm_size=farm_size
                )
                print("✅ Updated successfully!")
            else:
                print("❌ Not found.")

        elif choice == "4":
            planter_id = safe_input("Enter ID to delete: ", int)
            planter = Planter.get_by_id(planter_id)
            if planter:
                if confirm_action(f"🗑️ Confirm delete Planter {planter.name}?"):
                    planter.delete()
                    print("✅ Deleted successfully!")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Not found.")

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice.")

# Plant Menu
def plant_menu():
    while True:
        print("\n🌿 Plant Menu")
        print("1. Add Plant")
        print("2. View All Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter plant name: ")
            species = input("Enter plant species: ")
            age = safe_input("Enter plant age in months: ", int)
            health = input("Enter health status: ")

            site_id = safe_input("Enter Site ID: ", int)
            planter_id = safe_input("Enter Planter ID: ", int)

            new_plant = Plant(
                name=name, species=species, age_months=age,
                health_status=health, site_id=site_id, planter_id=planter_id
            )
            session.add(new_plant)
            session.commit()
            print(f"✅ Plant {name} added!")

        elif choice == "2":
            plants = session.query(Plant).all()
            if not plants:
                print("📭 No plants found.")
            else:
                table = [[p.id, p.name, p.species, p.age_months, p.health_status,
                          p.site_id, p.planter_id] for p in plants]
                print(tabulate(table, headers=["ID", "Name", "Species", "Age",
                                               "Health", "Site ID", "Planter ID"],
                               tablefmt="fancy_grid"))

        elif choice == "3":
            pid = safe_input("Enter Plant ID to update: ", int)
            plant = Plant.get_by_id(pid)
            if plant:
                name = input(f"Name [{plant.name}]: ") or plant.name
                species = input(f"Species [{plant.species}]: ") or plant.species
                age_months = safe_input(f"Age in months [{plant.age_months}]: ", int) or plant.age_months
                health_status = input(f"Health Status [{plant.health_status}]: ") or plant.health_status

                plant.update(
                    name=name,
                    species=species,
                    age_months=age_months,
                    health_status=health_status
                )
                print("✅ Plant updated!")
            else:
                print("❌ Plant not found.")

        elif choice == "4":
            pid = safe_input("Enter Plant ID to delete: ", int)
            plant = Plant.get_by_id(pid)
            if plant:
                if confirm_action(f"🗑️ Confirm delete Plant {plant.name}?"):
                    plant.delete()
                    print("✅ Plant deleted.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Plant not found.")

        elif choice == "0":
            break
        else:
            print("❌ Invalid choice.")

# Site Menu
def site_menu():
    while True:
        print("\n📍 Site Menu")
        print("1. Add Site")
        print("2. View All Sites")
        print("3. Update Site")
        print("4. Delete Site")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter site name: ")
            location = input("Enter site location: ")
            size = input("Enter site size: ")
            soil_type = input("Enter soil type: ")

            new_site = Site(name=name, location=location, size=size, soil_type=soil_type)
            session.add(new_site)
            session.commit()
            print(f"✅ Site {name} added!")

        elif choice == "2":
            sites = session.query(Site).all()
            if not sites:
                print("📭 No sites found.")
            else:
                table = [[s.id, s.name, s.location, s.size, s.soil_type] for s in sites]
                print(tabulate(
                    table,
                    headers=["ID", "Name", "Location", "Size", "Soil Type"],
                    tablefmt="fancy_grid"
                ))

        elif choice == "3":
            sid = safe_input("Enter Site ID to update: ", int)
            site = Site.get_by_id(sid)
            if site:
                name = input(f"Name [{site.name}]: ") or site.name
                location = input(f"Location [{site.location}]: ") or site.location
                size = input(f"Size [{site.size}]: ") or site.size
                soil_type = input(f"Soil Type [{site.soil_type}]: ") or site.soil_type

                site.update(
                    name=name,
                    location=location,
                    size=size,
                    soil_type=soil_type
                )
                print("✅ Site updated!")
            else:
                print("❌ Site not found.")

        elif choice == "4":
            sid = safe_input("Enter Site ID to delete: ", int)
            site = Site.get_by_id(sid)
            if site:
                if confirm_action(f"🗑️ Confirm delete Site {site.name}?"):
                    site.delete()
                    print("✅ Site deleted.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Site not found.")

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice.")

# Harvest Menu
def harvest_menu():
    while True:
        print("\n🌾 Harvest Menu")
        print("1. Add Harvest")
        print("2. View All Harvests")
        print("3. Update Harvest")
        print("4. Delete Harvest")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            plants = session.query(Plant).all()
            if not plants:
                print("📭 No plants available. Add plants first.")
                continue

            print("\nAvailable Plants:")
            for p in plants:
                print(f"ID: {p.id}, Name: {p.name}")

            plant_id = safe_input("Enter Plant ID: ", int)
            if not any(p.id == plant_id for p in plants):
                print("❌ Invalid Plant ID.")
                continue

            while True:
                try:
                    quantity = float(input("Enter quantity harvested: "))
                    break
                except ValueError:
                    print("❌ Invalid input. Must be a number.")
            unit = input("Enter unit (kg, bags, etc): ").strip() or "kg"

            Harvest.create(plant_id=plant_id, quantity=quantity, unit=unit)
            print("✅ Harvest added!")

        elif choice == "2":
            harvests = Harvest.get_all()
            if not harvests:
                print("📭 No harvests found.")
            else:
                table = [[h.id, h.plant_id, h.quantity, h.unit, h.date] for h in harvests]
                print(tabulate(table, headers=["ID", "Plant ID", "Quantity", "Unit", "Date"],
                               tablefmt="fancy_grid"))

        elif choice == "3":
            hid = safe_input("Enter Harvest ID to update: ", int)
            harvest = Harvest.get_by_id(hid)
            if harvest:
                quantity_input = input(f"Quantity [{harvest.quantity}]: ").strip()
                quantity = float(quantity_input) if quantity_input else harvest.quantity

                unit = input(f"Unit [{harvest.unit}]: ") or harvest.unit
                date = input(f"Date [{harvest.date}]: ") or str(harvest.date)

                harvest.update(
                    quantity=quantity,
                    unit=unit,
                    date=date
                )
                print("✅ Harvest updated!")
            else:
                print("❌ Harvest not found.")

        elif choice == "4":
            hid = safe_input("Enter Harvest ID to delete: ", int)
            harvest = Harvest.get_by_id(hid)
            if harvest:
                if confirm_action(f"🗑️ Confirm delete Harvest ID {harvest.id}?"):
                    harvest.delete()
                    print("✅ Harvest deleted.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Harvest not found.")

        elif choice == "0":
            break
        else:
            print("❌ Invalid choice.")

# Activity Menu
def activity_menu():
    while True:
        print("\n📝 Activity Menu")
        print("1. Add Activity")
        print("2. View All Activities")
        print("3. Update Activity")
        print("4. Delete Activity")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            desc = input("Enter description: ")

            plants = session.query(Plant).all()
            if not plants:
                print("📭 No plants available. Add plants first.")
                continue

            print("\nAvailable Plants:")
            for p in plants:
                print(f"ID: {p.id}, Name: {p.name}")

            plant_id = safe_input("Enter Plant ID: ", int)
            if not any(p.id == plant_id for p in plants):
                print("❌ Invalid Plant ID.")
                continue

            Activity.create(session, description=desc, plant_id=plant_id)
            print("✅ Activity created!")

        elif choice == "2":
            activities = Activity.get_all(session)
            if not activities:
                print("📭 No activities found.")
            else:
                table = [[a.id, a.description, a.plant_id, a.timestamp] for a in activities]
                print(tabulate(table, headers=["ID", "Description", "Plant ID", "Timestamp"],
                               tablefmt="fancy_grid"))

        elif choice == "3":
            aid = safe_input("Enter Activity ID to update: ", int)
            act = Activity.get_by_id(session, aid)
            if act:
                description = input(f"Description [{act.description}]: ") or act.description
                timestamp = input(f"Timestamp [{act.timestamp}]: ") or str(act.timestamp)

                act.update(
                    session,
                    description=description,
                    timestamp=timestamp
                )
                print("✅ Activity updated!")
            else:
                print("❌ Activity not found.")

        elif choice == "4":
            aid = safe_input("Enter Activity ID to delete: ", int)
            act = Activity.get_by_id(session, aid)
            if act:
                if confirm_action(f"🗑️ Confirm delete Activity ID {act.id}?"):
                    act.delete(session)
                    print("✅ Activity deleted.")
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Activity not found.")

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice. Try again.")

# Run CLI
if __name__ == "__main__":
    main_menu()
