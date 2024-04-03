"""Some functions for my garden plan!"""

# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Add by Kind."""
    if plant_kind in plants_by_kind:  # if key "plant_kind" is in "plants_by_kind"
        plants_by_kind[plant_kind].append(plant)
    else:  # if key "plant_kind" is NOT in "plants_by_kind"
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add by date."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)

# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Look Up by kind and date."""
    assert plant_kind in plants_by_kind
    assert month in plants_by_date
    # Look up the list of plants of kind "plant_kind"
    list_of_plants_by_kind: list[str] = plants_by_kind[plant_kind]
    # Look up the list of plants by month planted
    list_of_plants_by_date: list[str] = plants_by_date[month]
    # list_of_plants_by_kind = ["marigolds", "roses"]
    # list_of_plants_by_date = ["carrots", "roses"]
    combined: list[str] = []
    for plant in list_of_plants_by_kind: 
        for other_plant in list_of_plants_by_date:
            if other_plant == plant:  # Element shows up in both lists
                combined.append(other_plant)
    if len(combined) > 0:
        return f"{plant_kind}s to plant in {month}: {combined}"
    else: 
        return f"No {plant_kind} to plant in {month}"