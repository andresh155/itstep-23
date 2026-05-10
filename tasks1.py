contacts = {}
 
translations = {
    "cat": "кіт",
    "dog": "собака",
    "house": "дім",
    "car": "машина",
    "book": "книга",
    "water": "вода",
    "sun": "сонце",
    "moon": "місяць",
    "tree": "дерево",
    "apple": "яблуко",
    "friend": "друг",
    "love": "любов",
    "city": "місто",
    "sky": "небо",
    "phone": "телефон",
}
 
rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
 
 
def select_task():
    task = input("виберіть завдання: 1-4 ")
    match task:
        case "1":
            contact_book()
        case "2":
            text = input("введіть текст: ")
            task2(text)
        case "3":
            currency = input(f"введіть валюту {list(rates.keys())}: ").upper()
            amount = float(input("введіть суму у гривнях: "))
            task3(currency, amount)
        case "4":
            word = input("введіть слово англійською: ").lower()
            task4(word)
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
            select_task()

 
def contact_book():
    action = input("дія: додати(1) / видалити(2) / змінити(3) / всі контакти(4): ")
    match action:
        case "1":
            name = input("введіть ім'я: ")
            phone = input("введіть номер телефону: ")
            contacts[name] = phone
            print(f"контакт '{name}' додано")
        case "2":
            name = input("введіть ім'я для видалення: ")
            if name in contacts:
                del contacts[name]
                print(f"контакт '{name}' видалено")
            else:
                print("контакт не знайдено")
        case "3":
            name = input("введіть ім'я для зміни: ")
            if name in contacts:
                phone = input("введіть новий номер: ")
                contacts[name] = phone
                print(f"контакт '{name}' оновлено")
            else:
                print("контакт не знайдено")
        case "4":
            if not contacts:
                print("контактна книжка порожня")
            else:
                print("── всі контакти ──")
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
        case _:
            print("невірна дія")
 

 
def task2(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        word = word.strip(".,!?;:\"'")
        if word:
            counts[word] = counts.get(word, 0) + 1
    print("── кількість слів ──")
    for word, count in counts.items():
        print(f"{word}: {count}")
 
 
def task3(currency, amount):
    if currency in rates:
        result = amount / rates[currency]
        print(f"{amount} грн = {result:.2f} {currency}")
    else:
        print(f"валюта '{currency}' не знайдена")
 
 
 
def task4(word):
    if word in translations:
        print(f"{word} → {translations[word]}")
    else:
        print(f"слово '{word}' не знайдено у словнику")
 
 
while True:
    select_task()
 
