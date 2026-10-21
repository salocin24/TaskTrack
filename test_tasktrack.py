import pytest

from tasktrack import load_tasks, remove_task_by_number, save_tasks

@pytest.fixture
def sample_tasks():
    return ["Study", "Exercise", "Shop"]

def test_remove_first_task(sample_tasks):
    """Removing task 1 should remove the first task."""
    # Arrange
    task_number = 1
    expected_task = "Study"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_task
    assert sample_tasks == ["Exercise", "Shop"]

def test_remove_middle_task(sample_tasks):
    """Removing task 2 should remove the second task."""
    # Arrange
    task_number = 2
    expected_task = "Exercise"
    
    # Act
    result = remove_task_by_number(sample_tasks, task_number)
    
    # Assert
    assert result == expected_task
    assert sample_tasks == ["Study", "Shop"]

def test_remove_last_task(sample_tasks):
    """Removing task 2 should remove the second task."""
    # Arrange
    task_number = 3
    expected_task = "Shop"
    
    # Act
    result = remove_task_by_number(sample_tasks, task_number)
    
    # Assert
    assert result == expected_task
    assert sample_tasks == ["Study", "Exercise"]

def test_save_tasks_writes_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    tasks = ["Study", "Exercise", "Shop"]
    expected_text = "Study\nExercise\nShop\n"

    # Act
    save_tasks(tasks, test_file)

    # Assert
    assert test_file.read_text() == expected_text

def test_load_tasks_reads_all_tasks(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\nExercise\nShop\n")
    expected_tasks = ["Study", "Exercise", "Shop"]

    # Act
    result = load_tasks(test_file)

    # Assert
    assert result == expected_tasks

def test_load_tasks_ignores_blank_lines(tmp_path):
    # Arrange
    test_file = tmp_path / "tasks.txt"

 
    test_file.write_text("Study\n\nExercise\n")
    
  
    expected_tasks = ["Study", "Exercise"]

    # Act
    result = load_tasks(test_file)

    # Assert

    assert result == expected_tasks

def test_missing_file(tmp_path):
    #Arrange
    test_file = tmp_path / "doesntexist.txt"
    expected_tasks = []

    #Act
    result = load_tasks(test_file)

    #Assert
    assert result == expected_tasks

def test_save_empty_list(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"
    expected_tasks = []
    #Act
    result = save_tasks([], test_file)

    #Assert
    assert load_tasks(test_file) == expected_tasks
####################################################################

@pytest.mark.parametrize(
        "task_number",
        [
            0,
            -1,
            10,
        ],
        ids=[
            "zero",
            "negative_number",
            "number_too_large",
        ],
)

def test_invalid_task_numbers_return_none(task_number):
    #Arrange
    tasks = ["Study", "Exercise", "Shop"]

    #Act
    result = remove_task_by_number(tasks, task_number)

    #Assert
    assert result is None
    assert tasks == ["Study", "Exercise", "Shop"]

