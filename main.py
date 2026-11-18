from model.credit_card import CreditCard
from storage.card_storage import CardStorage


def main():
    card = CreditCard("John Smith", "Chase", "123456789", 5000)
    card.charge(1000)
    card.make_payment(300)
    print(card)
    CardStorage.save([card], "data/cards.json")


if __name__ == "__main__":
    main()
