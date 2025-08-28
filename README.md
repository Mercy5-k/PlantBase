# 🌱 PlantBase
---

**PlantBase** is a **Command Line Interface (CLI) application** that helps farmers and agricultural projects manage their farm records in a simple, structured, and interactive way.  It is designed for **smallholder farmers and learners** who want to keep track of farming data digitally instead of relying on paper notes.

PlantBase provides a **menu-driven interface** where users can manage planters, plants, sites, harvests, and activities all from the terminal.  With **validated inputs** and **clear tabular outputs**, PlantBase helps reduce errors and provides a smooth workflow for managing farm-related data.  

## Table of Contents
---
- [Project Overview](#-project-overview)
-  [Features](#-features)
-   [Installation](#-installation)
-  [How to Use](#-how-to-use)
-   [Models & Relationships](#-models--relationships)
-   [Seeding Data](#-seeding-data)
-   [Dependencies](#-dependencies)  
-  [Author](#-author)  
-  [License](#-license)

## Project Overview
---

PlantBase CLI is a lightweight farming record management system built with Python and SQLAlchemy.  It helps track **planters, plants, sites, harvests, and activities** in one place.  
The system is designed to reflect **real farming workflows in Kenya**, making it simple to:  
- Register planters and their farms.  
- Manage plants with age, health, and species details.  
- Record farm sites with soil type and size.  
- Track harvests and farming activities like watering, weeding, and spraying.
- 
This project demonstrates a clean and interactive **CRUD workflow** for agriculture management while ensuring data consistency and user-friendly navigation in the command line.  

## How to Use
---
**Start the CLI**  
   ```bash
   pipenv shell
   python -m app.cli
```

🌱 PlantBase Main Menu

When the app starts, you’ll see:

**Main Menu**
1. Planters
2. Plants
3. Sites
4. Harvests
5. Activities
0. Exit

**Submenus**

Each section, lets you:

- Enter Data when prompted.

- View Data displayed in pretty tables

- Exit the App using the 0

``` bash
👋 Goodbye from PlantBase!
```
##  Features
---

- 👨‍🌾 **Planters Management**  
  - Add, view, update, and delete planter records.  
  - Store details such as name, location, contact info, experience, and farm size.  

- 🌿 **Plants Management**  
  - Manage plant details: name, species, age (months), and health status.  
  - Link each plant to a **planter** and a **site**.  

- 📍 **Sites Management**  
  - Register and manage farm sites with size, location, and soil type.  
  - Assign multiple plants to a single site.  

- 🌾 **Harvest Records**  
  - Record harvests linked to plants.  
  - Track yield amounts and harvest dates.  

- 📝 **Activities Log**  
  - Keep track of farm activities such as watering, weeding, spraying, or fertilizing.  
  - Attach each activity to a specific plant for easy monitoring.  

- ✅ **Safe Updates**  
  - Update non-critical fields freely.  
  - Critical IDs (`plant_id`, `site_id`, `planter_id`) are **protected** from accidental changes.  

- 📊 **Pretty Tables**  
  - All data displayed in **clear, tabular format** using `tabulate`.  
  - Easy-to-read overview of plants, planters, sites, harvests, and activities.  

- 🧑‍💻 **User-Friendly CLI**  
  - Interactive text-based menus.  
  - Simple navigation with validation and confirmation prompts.  

##  Installation
---

 **Clone the repository**
   ```bash
   git clone https://github.com/Mercy5-k/PlantBase.git
   cd PlantBase
   ```
**Install dependencies using Pipenv**
   ```bash
   pipenv install
   pipenv shell
   ```
##  Models & Relationships
---

### 👨‍🌾 Planter
Represents a **farmer or caretaker** responsible for plants.  
- **Fields:** `id`, `name`, `location`, `contact_info`, `plant_type`, `experience_months`, `farm_size`, `created_at`  
- **Relationships:**  
  - One **planter** can manage many **plants**.

---

### 🌿 Plant
Represents a **specific crop, flower, or tree** being grown.  
- **Fields:** `id`, `name`, `species`, `age_months`, `health_status`, `site_id`, `planter_id`  
- **Relationships:**  
  - Each **plant** belongs to **one planter** and **one site**.  
  - A plant can have many **harvests** and **activities**.

---

### 📍 Site
Represents the **farm location** where plants are grown.  
- **Fields:** `id`, `name`, `location`, `size`, `soil_type`  
- **Relationships:**  
  - One **site** can host many **plants**.

---

### 🌾 Harvest
Represents the **produce collected** from a plant.  
- **Fields:** `id`, `plant_id`, `quantity`, `date`, `notes`  
- **Relationships:**  
  - Each **harvest** is linked to a **single plant**.

---

### 📝 Activity
Represents **farm activities** done on plants (watering, weeding, spraying, etc.).  
- **Fields:** `id`, `plant_id`, `description`, `date`  
- **Relationships:**  
  - Each **activity** is linked to a **single plant**.

---

### 🔗 Relationship Overview
- **Planter → Plant** (One planter can manage many plants)  
- **Site → Plant** (One site can host many plants)  
- **Plant → Harvest** (One plant can produce many harvests)  
- **Plant → Activity** (One plant can have many activities)

## Seeding Data
---
The project includes a **seed script** that generates realistic Kenyan farming data.

- **Planters:** 15–30 (with Kenyan names, locations, and contact details)  
- **Sites:** 4–14 (with realistic farm sizes and soil types)  
- **Plants:** 6–12 (linked to planters and sites, with varied species & ages)  
- **Harvests:** 7–15 (with quantities, dates, and notes)  
- **Activities:** 5- 10 (watering, weeding, spraying, etc. on plants)  

This helps simulate **real-world usage** for demonstration and testing.

---

##  Dependencies
- **Python 3.8+**  
- **Pipenv** (for dependency management)  
- **SQLAlchemy** (ORM for database management)  
- **Faker** (data seed)  
- **Tabulate** (for clean tabular CLI output)  

---

##  Future Improvements
- Add **user authentication & roles** (Admin vs Planter).  
- Enable **report exports** to CSV or PDF.  
- Introduce **notifications/reminders** for farm activities (e.g., watering schedules).  
- Provide **analytics dashboards** (yields per site, planter performance).  
- Extend to a **web or mobile app** for broader use.  

---

##  Author
Created by **Mercy Kinya**  

---

## 📄 License
MIT License  
Copyright (c) 2025 **Mercy Kinya**



