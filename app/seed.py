from models.base import Base, engine, session
from models.site import Site
from models.planter import Planter
from models.plant import Plant
from models.harvest import Harvest
from models.activity import Activity
import datetime 

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed Sites
sites = [
    Site(name="Kitale Agrofarm", location="Trans-Nzoia", size="80 acres", soil_type="Loamy"),
    Site(name="Kericho Greenfields", location="Kericho", size="150 acres", soil_type="Clay"),
    Site(name="Mwea Rice Scheme", location="Kirinyaga", size="300 acres", soil_type="Alluvial"),
    Site(name="Naivasha Valley Farm", location="Naivasha", size="50 acres", soil_type="Volcanic"),
    Site(name="Meru Highlands", location="Meru", size="70 acres", soil_type="Sandy Loam"),
]
session.add_all(sites)
session.commit()

# Seed Planters
planters = [
    Planter(
        name="Kamau Mwangi",
        location="Trans-Nzoia",
        contact_info="0723763523",
        plant_type="Crops",
        experience_months=144,
        farm_size="10 acres",
        site_id=sites[0].id
    ),
    Planter(
        name="Omondi Onyango",
        location="Trans-Nzoia",
        contact_info="0789763433",
        plant_type="Crops",
        experience_months=96,
        farm_size="8 acres",
        site_id=sites[0].id
    ),
    Planter(
        name="Achieng Otieno",
        location="Kericho",
        contact_info="achien4@gmail.com",
        plant_type="Tea",
        experience_months=120,
        farm_size="15 acres",
        site_id=sites[1].id
    ),
    Planter(
        name="Kiprotich Sang",
        location="Kericho",
        contact_info="0745678909",
        plant_type="Tea",
        experience_months=72,
        farm_size="12 acres",
        site_id=sites[1].id
    ),
    Planter(
        name="Mwea Irrigation Cooperative Society",
        location="Kirinyaga",
        contact_info="mwea@coop@gmail.com",
        plant_type="Rice",
        experience_months=240,
        farm_size="300 acres",
        site_id=sites[2].id
    ),
    Planter(
        name="Naivasha Flower Growers Association",
        location="Naivasha",
        contact_info="0790996513",
        plant_type="Flowers",
        experience_months=180,
        farm_size="25 acres",
        site_id=sites[3].id
    ),
    Planter(
        name="Meru Macadamia Farmers Union",
        location="Meru",
        contact_info="0771225677",
        plant_type="Macadamia",
        experience_months=216,
        farm_size="50 acres",
        site_id=sites[4].id
    ),
    Planter(
        name="St. Mary’s Secondary School Agriculture Club",
        location="Kirinyaga",
        contact_info="0763312010",
        plant_type="Vegetables",
        experience_months=48,
        farm_size="2 acres",
        site_id=sites[2].id
    ),
    Planter(
        name="ACK St. Paul’s Church Farm",
        location="Trans-Nzoia",
        contact_info="0722334455",
        plant_type="Crops",
        experience_months=108,
        farm_size="20 acres",
        site_id=sites[0].id
    ),
    Planter(
        name="Green Kenya NGO",
        location="Naivasha",
        contact_info="greenkenya@gmail.com",
        plant_type="Vegetables",
        experience_months=132,
        farm_size="15 acres",
        site_id=sites[3].id
    ),
]
session.add_all(planters)
session.commit()


# Seed Plants 
plants = [
    Plant(name="Hybrid Maize H614", species="Maize", age_months=4, health_status="Healthy", site_id=sites[0].id, planter_id=planters[0].id),
    Plant(name="Grevillea Tree", species="Tree", age_months=36, health_status="Healthy", site_id=sites[0].id, planter_id=planters[0].id),
    Plant(name="Rosecoco Beans", species="Beans", age_months=3, health_status="Pest Infested", site_id=sites[0].id, planter_id=planters[1].id),
    Plant(name="Eucalyptus Trees", species="Tree", age_months=48, health_status="Healthy", site_id=sites[0].id, planter_id=planters[8].id),
    Plant(name="Purple Tea", species="Tea", age_months=18, health_status="Needs Water", site_id=sites[1].id, planter_id=planters[2].id),
    Plant(name="Hass Avocado", species="Fruit", age_months=24, health_status="Healthy", site_id=sites[1].id, planter_id=planters[2].id),
    Plant(name="Arabica Coffee", species="Coffee", age_months=20, health_status="Diseased", site_id=sites[1].id, planter_id=planters[3].id),
    Plant(name="Pishori Rice", species="Rice", age_months=6, health_status="Healthy", site_id=sites[2].id, planter_id=planters[4].id),
    Plant(name="Kilele F1 Tomatoes", species="Vegetable", age_months=2, health_status="Needs Water", site_id=sites[2].id, planter_id=planters[4].id),
    Plant(name="Ngombe Bananas", species="Fruit", age_months=14, health_status="Healthy", site_id=sites[2].id, planter_id=planters[7].id),
    Plant(name="Red Roses", species="Flower", age_months=3, health_status="Healthy", site_id=sites[3].id, planter_id=planters[5].id),
    Plant(name="Cucumbers", species="Vegetable", age_months=1, health_status="Pest Infested", site_id=sites[3].id, planter_id=planters[9].id),
    Plant(name="Macadamia Trees", species="Tree", age_months=60, health_status="Healthy", site_id=sites[4].id, planter_id=planters[6].id),
    Plant(name="Robusta Coffee", species="Coffee", age_months=30, health_status="Needs Water", site_id=sites[4].id, planter_id=planters[6].id),
]

session.add_all(plants)
session.commit()

# Seed Harvests
harvests = [
    Harvest(plant_id=plants[0].id, quantity=1200, unit="kg", date=datetime.date(2025, 7, 15)), # maize
    Harvest(plant_id=plants[2].id, quantity=300, unit="kg", date=datetime.date(2025, 7, 25)), # beans
    Harvest(plant_id=plants[4].id, quantity=400, unit="kg", date=datetime.date(2025, 6, 30)), # tea
    Harvest(plant_id=plants[5].id, quantity=250, unit="kg", date=datetime.date(2025, 7, 10)), # avocado
    Harvest(plant_id=plants[6].id, quantity=150, unit="kg", date=datetime.date(2025, 8, 2)),  # coffee
    Harvest(plant_id=plants[7].id, quantity=2000, unit="kg", date=datetime.date(2025, 8, 5)), # rice
    Harvest(plant_id=plants[9].id, quantity=600, unit="kg", date=datetime.date(2025, 8, 7)),  # bananas
    Harvest(plant_id=plants[10].id, quantity=10000, unit="stems", date=datetime.date(2025, 8, 15)), # roses
    Harvest(plant_id=plants[11].id, quantity=180, unit="kg", date=datetime.date(2025, 8, 18)), # cucumbers
    Harvest(plant_id=plants[12].id, quantity=900, unit="kg", date=datetime.date(2025, 7, 20)),  # macadamia
]

session.add_all(harvests)
session.commit()

# Seed Activities
activities = [
    Activity(description="Weeded maize field", plant_id=plants[0].id, timestamp=datetime.datetime(2025, 7, 20, 9, 0)),
    Activity(description="Pruned Grevillea trees", plant_id=plants[1].id, timestamp=datetime.datetime(2025, 7, 25, 10, 30)),
    Activity(description="Sprayed beans against aphids", plant_id=plants[2].id, timestamp=datetime.datetime(2025, 7, 28, 14, 0)),
    Activity(description="Harvested eucalyptus for timber", plant_id=plants[3].id, timestamp=datetime.datetime(2025, 8, 1, 15, 0)),
    Activity(description="Plucked tea leaves", plant_id=plants[4].id, timestamp=datetime.datetime(2025, 7, 29, 8, 0)),
    Activity(description="Harvested ripe avocados", plant_id=plants[5].id, timestamp=datetime.datetime(2025, 7, 31, 11, 0)),
    Activity(description="Mulched coffee bushes", plant_id=plants[6].id, timestamp=datetime.datetime(2025, 8, 3, 10, 15)),
    Activity(description="Flooded rice paddies", plant_id=plants[7].id, timestamp=datetime.datetime(2025, 7, 26, 7, 30)),
    Activity(description="Staked tomato plants", plant_id=plants[8].id, timestamp=datetime.datetime(2025, 7, 30, 16, 0)),
    Activity(description="Removed banana suckers", plant_id=plants[9].id, timestamp=datetime.datetime(2025, 8, 1, 9, 45)),
    Activity(description="Applied fertilizer to roses", plant_id=plants[10].id, timestamp=datetime.datetime(2025, 8, 4, 10, 0)),
    Activity(description="Watered cucumbers in greenhouse", plant_id=plants[11].id, timestamp=datetime.datetime(2025, 8, 5, 8, 15)),
    Activity(description="Harvested macadamia nuts", plant_id=plants[12].id, timestamp=datetime.datetime(2025, 8, 7, 12, 0)),
    Activity(description="Pruned coffee trees", plant_id=plants[13].id, timestamp=datetime.datetime(2025, 8, 8, 9, 30)),
]
session.add_all(activities)
session.commit()

print("✅ Seed data added successfully!")
