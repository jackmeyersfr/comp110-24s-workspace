"""Test my garden functions."""

__author__: str = '730646830'


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Testing add by kind."""
    plant_dict: dict[str, list[str]] = {"vegetable": ["onion", "spinach", "lettuce"]}
    plant: str = "vegetable"
    vegetable: str = "cabbage"
    add_by_kind(plant_dict, plant, vegetable)
    assert plant_dict == {"vegetable": ["onion", "spinach", "lettuce", "cabbage"]}


def test_add_by_kind_edge() -> None:
    """Testing add_by_kind edge case."""
    plant_dict: dict[str, list[str]] = {"vegetable": ["onion", "spinach", "lettuce"]}
    plant: str = "vegetable"
    vegetable: str = ""
    add_by_kind(plant_dict, plant, vegetable)
    assert plant_dict == {"vegetable": ["onion", "spinach", "lettuce", ""]}


def test_add_by_date_use() -> None:
    """Testing add by date."""
    plant_dict: dict[str, list[str]] = {"April": ["onion", "spinach", "lettuce"]}
    month: str = "May"
    vegetable: str = "cabbage"
    add_by_date(plant_dict, month, vegetable)
    assert plant_dict == {"April": ["onion", "spinach", "lettuce"], "May": ["cabbage"]}


def test_add_by_date_edge() -> None:
    """Testing add_by_date edge case."""
    plant_dict: dict[str, list[str]] = {"May": ["onion", "spinach", "lettuce"]}
    plant: str = "April"
    vegetable: str = ""
    add_by_date(plant_dict, plant, vegetable)
    assert plant_dict == {"May": ["onion", "spinach", "lettuce"], "April": [""]}


def test_lookup_by_kind_and_date_use() -> None:
    """Testing lookup by kind and date."""
    plant_dict: dict[str, list[str]] = {"vegetable": ["onion", "spinach", "lettuce"]}
    month_dict: dict[str, list[str]] = {"May": ["onion", "cabbage", "lettuce"]}
    plant: str = "vegetable"
    month: str = "May"
    output: str = lookup_by_kind_and_date(plant_dict, month_dict, plant, month)
    assert output == "vegetables to plant in May: ['onion', 'lettuce']"


def test_lookup_by_kind_and_date_edge() -> None:
    """Testing lookup by kind and date edge example."""
    plant_dict: dict[str, list[str]] = {"vegetable": ["onion", "spinach", "lettuce"]}
    month_dict: dict[str, list[str]] = {"May": ["cabbage"]}
    plant: str = "vegetable"
    month: str = "May"
    output: str = lookup_by_kind_and_date(plant_dict, month_dict, plant, month)
    assert output == "No vegetable to plant in May"
