class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age <= 12:
            return 50
        if age <= 20:
            return 100
        if age <= 60:
            return 150
        else:
            return 100
