from typing import List


class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = self.validate_comfort_class(comfort_class)
        self.clean_mark = self.validate_clean_mark(clean_mark)
        self.brand = brand

    @staticmethod
    def validate_comfort_class(comfort_class: int) -> int:
        if 1 <= comfort_class <= 7:
            return comfort_class
        return 3

    @staticmethod
    def validate_clean_mark(clean_mark: int) -> int:
        if 1 <= clean_mark <= 10:
            return clean_mark
        return 5


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = self.validate_distance(
            distance_from_city_center
        )
        self.clean_power = self.validate_clean_power(clean_power)
        self.average_rating = self.validate_average_rating(average_rating)
        self.count_of_ratings = self.validate_count_of_ratings(
            count_of_ratings
        )

    @staticmethod
    def validate_distance(distance: float) -> float:
        if distance > 0:
            return distance
        return 1.0

    @staticmethod
    def validate_clean_power(clean_power: int) -> int:
        if 1 <= clean_power <= 10:
            return clean_power
        return 5

    @staticmethod
    def validate_average_rating(average_rating: int) -> int:
        if 1 <= average_rating <= 5:
            return average_rating
        return 3

    @staticmethod
    def validate_count_of_ratings(count_of_ratings: int) -> int:
        if count_of_ratings >= 0:
            return count_of_ratings
        return 0

    def serve_cars(self, cars: List[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(((car.comfort_class
                       * (self.clean_power - car.clean_mark)
                       * self.average_rating)
                      / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings)
             + new_rating) / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
