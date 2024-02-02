class Student:

    def __init__(self):
        self.__name: str = str()
        self.__no: int = int()
        self.__notes: list[float] = list()
        self.__average: float = float()
        self.__is_average_calculated: bool = False

    def set_name(self, name: str):
        self.__name = name

    def set_no(self, name: int):
        self.__name = name

    def set_notes(self, notes: list[float]):
        self.__is_average_calculated = False
        self.__notes = notes

    def get_name(self) -> str:
        return self.__name

    def get_no(self) -> int:
        return self.__no

    def get_notes(self) -> list[float]:
        return self.__notes

    def get_average(self) -> float:
        if self.__is_average_calculated:
            return self.__average
        else:
            self.__calculate_average()
            return self.__average

    def __calculate_average(self):
        note_sum = 0.0
        for note in self.__notes:
            note_sum += note
        self.__average = note_sum / len(self.__notes)
        self.__is_average_calculated = True
