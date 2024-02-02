def search_in_list(searched_name: str, list_of_students: list[str]) -> bool:
    for name in list_of_students:
        if searched_name == name:
            return True
    return False


student_list: list[str] = ["Enes Sancak", "Joe Doe", "Jane"]

if search_in_list("Enes Sancak", student_list):
    print("Name exists in list.")
else:
    print("Name does not exists in list.")
