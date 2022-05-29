class Built_train:
    wellcome="Well come built Train: "
    def __init__(self, ticket_price,Your_trivel):
        self.ticket_price=ticket_price
        self.Your_trivel=Your_trivel
        if self.Your_trivel>=1 and self.Your_trivel<=5:
            print(f"Your ticket price is {self.ticket_price} ")
        elif self.Your_trivel>5:
            self.ticket_price=20+(self.Your_trivel-5)*8
            print(f"Your ticket price is {self.ticket_price}")
train=Built_train(20,4)
