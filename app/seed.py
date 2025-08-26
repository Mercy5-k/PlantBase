from models.base import session
from models.planter import Planter
from datetime import datetime

def seed():
    # This clears existing data to avoid duplicates during seeding
    session.query(Planter).delete()

    # Samples of planters that could be added
    planters = [
        Planter(
            name="Community Green Initiative",
            location="Nakuru",
            contact_info="Community Green Initiative",
            plant_type="Trees",
            experience_level="Intermediate",
            experience_months=15,
            farm_size="Large forest",
            preferred_tools="Chainsaw, Shovel",
            created_at=datetime.now()
        ),
        Planter(
            name="Jeff Njuguna",
            location="Eldoret",
            contact_info="0723456789",
            plant_type="Tress",
            experience_level="Expert",
            experience_months=3,
            farm_size="4 acres",
            preferred_tools="Pruning saw, Tractor ",
            created_at=datetime.now()
        ),
         Planter(
            name="Mary Kamba",
            location="Kisumu",
            contact_info="0798765432",
            plant_type="Vegetables",
            experience_level="Intermediate",
            experience_months=12,
            farm_size="1/2 Acre",
            preferred_tools="Hoe, Water Pump",
            created_at=datetime.now()
        ),
    ]

    session.add_all(planters)
    session.commit()
    print("✅ Seed data was added successfully!")

if __name__ == "__main__":
    seed()
