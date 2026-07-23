import random

import pandas as pd


# Use a fixed seed so the same dataset is generated each time
random.seed(42)


product_categories = {
    "Aluminium Foil": [
        "Foil 250 mm",
        "Foil 275 mm",
        "Foil 300 mm",
        "Foil 325 mm",
        "Foil 350 mm",
        "Foil 375 mm",
        "Foil 400 mm",
        "Foil 425 mm",
        "Foil 450 mm",
        "Foil 475 mm",
        "Foil 500 mm",
        "Foil 525 mm",
        "Foil 550 mm",
        "Foil 575 mm",
        "Foil 600 mm"
    ],
    "Packaging Film": [
        "PET Film 12 Micron",
        "PET Film 15 Micron",
        "BOPP Film 18 Micron",
        "BOPP Film 20 Micron",
        "Barrier Film Standard",
        "Barrier Film Premium",
        "Printed Film Type A",
        "Printed Film Type B",
        "Lamination Film A",
        "Lamination Film B",
        "Shrink Film Light",
        "Shrink Film Heavy",
        "Sealant Film A",
        "Sealant Film B",
        "Protective Film"
    ],
    "Polymer Resin": [
        "LDPE Resin",
        "LLDPE Resin",
        "HDPE Resin",
        "PP Resin",
        "PET Resin",
        "Nylon Resin",
        "EVA Resin",
        "Barrier Resin",
        "Recycled PE Resin",
        "Recycled PP Resin",
        "Food Grade Resin A",
        "Food Grade Resin B",
        "Industrial Resin A",
        "Industrial Resin B",
        "Specialty Resin"
    ],
    "Adhesive": [
        "Solvent Adhesive A",
        "Solvent Adhesive B",
        "Water Adhesive A",
        "Water Adhesive B",
        "Lamination Adhesive A",
        "Lamination Adhesive B",
        "Heat Seal Adhesive",
        "Cold Seal Adhesive",
        "Primer Adhesive",
        "Food Grade Adhesive",
        "High Bond Adhesive",
        "Low Viscosity Adhesive",
        "Fast Cure Adhesive",
        "Standard Cure Adhesive",
        "Specialty Adhesive"
    ],
    "Packaging Material": [
        "Cardboard Box Small",
        "Cardboard Box Medium",
        "Cardboard Box Large",
        "Wooden Pallet Standard",
        "Wooden Pallet Heavy",
        "Plastic Pallet",
        "Stretch Wrap",
        "Packing Tape",
        "Protective Sheet",
        "Bubble Wrap",
        "Corrugated Sheet",
        "Paper Core Small",
        "Paper Core Medium",
        "Paper Core Large",
        "Packaging Label"
    ],
    "Ink and Coating": [
        "Black Printing Ink",
        "Blue Printing Ink",
        "Red Printing Ink",
        "Yellow Printing Ink",
        "White Printing Ink",
        "Green Printing Ink",
        "Protective Coating",
        "Matte Coating",
        "Gloss Coating",
        "Barrier Coating",
        "Heat Resistant Coating",
        "Food Grade Coating",
        "Primer Coating",
        "Specialty Ink A",
        "Specialty Ink B"
    ],
    "Maintenance Supply": [
        "Machine Lubricant",
        "Cleaning Solvent",
        "Industrial Cleaner",
        "Filter Cartridge",
        "Cutting Blade",
        "Rubber Roller",
        "Machine Belt",
        "Bearing Standard",
        "Bearing Heavy Duty",
        "Safety Gloves",
        "Protective Mask",
        "Cleaning Cloth",
        "Maintenance Tool Kit",
        "Spare Sensor",
        "Electrical Fuse"
    ]
}


rows = []
sku_number = 1001

for category, products in product_categories.items():
    for product_name in products:

        annual_demand = random.randint(2000, 30000)

        if category == "Aluminium Foil":
            unit_cost = round(random.uniform(3.50, 7.50), 2)
            lead_time = random.randint(10, 30)

        elif category == "Packaging Film":
            unit_cost = round(random.uniform(2.00, 6.00), 2)
            lead_time = random.randint(7, 25)

        elif category == "Polymer Resin":
            unit_cost = round(random.uniform(1.50, 5.50), 2)
            lead_time = random.randint(14, 40)

        elif category == "Adhesive":
            unit_cost = round(random.uniform(4.00, 12.00), 2)
            lead_time = random.randint(10, 35)

        elif category == "Ink and Coating":
            unit_cost = round(random.uniform(5.00, 18.00), 2)
            lead_time = random.randint(7, 28)

        elif category == "Maintenance Supply":
            unit_cost = round(random.uniform(3.00, 40.00), 2)
            lead_time = random.randint(5, 30)

        else:
            unit_cost = round(random.uniform(0.50, 8.00), 2)
            lead_time = random.randint(3, 20)

        ordering_cost = random.randint(50, 250)

        holding_rate = random.uniform(0.15, 0.30)
        holding_cost = round(unit_cost * holding_rate, 2)

        daily_demand_stddev = round(
            random.uniform(
                max(1, annual_demand / 365 * 0.05),
                max(2, annual_demand / 365 * 0.25)
            ),
            2
        )

        service_level_z = random.choice(
            [1.28, 1.65, 1.96, 2.33]
        )

        rows.append(
            {
                "SKU": f"SKU-{sku_number}",
                "Category": category,
                "Product": product_name,
                "Annual_Demand": annual_demand,
                "Unit_Cost": unit_cost,
                "Lead_Time": lead_time,
                "Ordering_Cost": ordering_cost,
                "Holding_Cost": holding_cost,
                "Daily_Demand_StdDev": daily_demand_stddev,
                "Service_Level_Z": service_level_z
            }
        )

        sku_number += 1


inventory_data = pd.DataFrame(rows)

inventory_data.to_csv(
    "inventory_data.csv",
    index=False
)

print("=" * 60)
print("REALISTIC INVENTORY DATASET CREATED")
print("=" * 60)
print(f"Number of SKUs: {len(inventory_data)}")
print("File created: inventory_data.csv")
print("=" * 60)