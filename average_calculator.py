
class AverageCalculator:
    def calculate_average(self, num_list):
        if not num_list:
            return 0
        return sum(num_list) / len(num_list)

    def compare_averages(self, list1, list2):
        avg1 = self.calculate_average(list1)
        avg2 = self.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg1 < avg2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"