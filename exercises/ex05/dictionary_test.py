"""EX06 - Who is battleship? - A giant leap for mankind away from Battleship."""

__author__: str = "730646830"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use1() -> None:
    """Testing invert with one key and one value."""
    plant_dict: dict[str, str] = {"vegetable": "lettuce"}
    output: dict[str, str] = invert(plant_dict)
    assert output == {"lettuce": "vegetable"}


def test_invert_use2() -> None:
    """Testing invert with multiple keys and multiple values."""
    plant_dict: dict[str, str] = {"vegetable": "lettuce", "fruit": "apple"}
    output: dict[str, str] = invert(plant_dict)
    assert output == {"lettuce": "vegetable", "apple": "fruit"}


def test_invert_edge() -> None:
    """Testing invert with an empty string value."""
    plant_dict: dict[str, str] = {"vegetable": ""}
    output: dict[str, str] = invert(plant_dict)
    assert output == {"": "vegetable"}


def test_favorite_color_use1() -> None:
    """Testing favorite_color with three keys and three values."""
    color_dict: dict[str, str] = {"Hayden": "Blue", "Isaac": "Blue", "Georgia": "Red"}
    output: str = favorite_color(color_dict)
    assert output == "Blue"


def test_favorite_color_use2() -> None:
    """Testing favorite_color with lots of keys and lots of values."""
    color_dict: dict[str, str] = {"Hayden": "Blue", "Isaac": "Blue", "Georgia": "Red", "Manir": "Yellow", "Ruhi": "Red", "Bryce": "Red"}
    output: str = favorite_color(color_dict)
    assert output == "Red"


def test_favorite_color_edge() -> None:
    """Testing favorite_color with the most popular string being an empty one."""
    color_dict: dict[str, str] = {"Hayden": "", "Isaac": "", "Georgia": "", "Manir": "Yellow", "Ruhi": "Red", "Bryce": "Red"}
    output: str = favorite_color(color_dict)
    assert output == ""


def test_count_use1() -> None:
    """Testing count with one key."""
    count_list: list[str] = ["Hi", "Hi", "Hi"]
    output: dict[str, int] = count(count_list)
    assert output == {"Hi": 3}


def test_count_use2() -> None:
    """Testing count with multiple keys."""
    count_list: list[str] = ["Hi", "Hello", "Hi", "Hola"]
    output: dict[str, int] = count(count_list)
    assert output == {"Hi": 2, "Hello": 1, "Hola": 1}


def test_count_edge() -> None:
    """Testing count with no keys."""
    count_list: list[str] = [""]
    output: dict[str, int] = count(count_list)
    assert output == {"": 1}


def test_alphabetizer_use1() -> None:
    """Testing alphabetizer with one word."""
    alphabetizer_list: list[str] = ["apple"]
    output: dict[str, list[str]] = alphabetizer(alphabetizer_list)
    assert output == {"a": ["apple"]}


def test_alphabetizer_use2() -> None:
    """Testing alphabetizer with multiple words."""
    alphabetizer_list: list[str] = ["apple", "boat", "array", "cat"]
    output: dict[str, list[str]] = alphabetizer(alphabetizer_list)
    assert output == {"a": ["apple", "array"], "b": ["boat"], "c": ["cat"]}


def test_alphabetizer_edge() -> None:
    """Testing alphabetizer with a not real word."""
    alphabetizer_list: list[str] = ["dfkdsjf"]
    output: dict[str, list[str]] = alphabetizer(alphabetizer_list)
    assert output == {"d": ["dfkdsjf"]}


def test_update_attendance_use1() -> None: 
    """Testing update_attendance with a new day added."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Jane", "Annie"], "Tuesday": ["Raya"]}
    dow: str = "Tuesday"
    student: str = "Raya"
    update_attendance(attendance_dict, dow, student)
    assert attendance_dict == {"Monday": ["Jane", "Annie"], "Tuesday": ["Raya"], "Wednesday": ["Raya"]}


def test_update_attendance_use2() -> None: 
    """Testing update_attendance with new name added."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Jane", "Annie"], "Tuesday": ["Raya"]}
    dow: str = "Tuesday"
    student: str = "Jake"
    update_attendance(attendance_dict, dow, student)
    assert attendance_dict == {"Monday": ["Jane", "Annie"], "Tuesday": ["Raya", "Jake"]}


def test_update_attendance_edge() -> None: 
    """Testing update_attendance with student being an empty string."""
    attendance_dict: dict[str, list[str]] = {"Monday": ["Jane", "Annie"], "Tuesday": ["Raya"]}
    dow: str = "Monday"
    student: str = ""
    update_attendance(attendance_dict, dow, student)
    assert attendance_dict == {"Monday": ["Jane", "Annie", ""], "Tuesday": ["Raya"]}
