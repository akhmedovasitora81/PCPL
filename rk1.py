from operator import itemgetter

class Computer:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class HDD:
    def __init__(self, id: int, model: str, capacity: int, computer_id: int):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.computer_id = computer_id

class HDDInstallation:
    def __init__(self, hdd_id: int, computer_id: int):
        self.hdd_id = hdd_id
        self.computer_id = computer_id

computers = [
    Computer(1, "Игровой компьютер ASUS"),
    Computer(2, "Офисный компьютер HP"),
    Computer(3, "Ноутбук Lenovo"),
]

hdds = [
    HDD(1, "Adata SU650", 512, 1),
    HDD(2, "AMD Radeon R5", 256, 1),
    HDD(3, "Samsung 980 Pro", 2048, 2),
    HDD(4, "Kingston A400", 480, 2),
    HDD(5, "WD Blue HDD", 1000, 3),
]

installations = [
    HDDInstallation(1, 1),
    HDDInstallation(1, 2),
    HDDInstallation(2, 1),
    HDDInstallation(3, 2),
    HDDInstallation(3, 3),
    HDDInstallation(5, 3),
]

def main():
    one_to_many = [
        (h.model, h.capacity, c.name)
        for c in computers
        for h in hdds
        if h.computer_id == c.id
    ]

    many_to_many_temp = [
        (c.name, link.computer_id, link.hdd_id)
        for c in computers
        for link in installations
        if c.id == link.computer_id
    ]

    many_to_many = [
        (h.model, h.capacity, comp_name)
        for comp_name, comp_id, hdd_id in many_to_many_temp
        for h in hdds
        if h.id == hdd_id
    ]

    print("Задание E1")
    for c in computers:
        if "компьютер" in c.name.lower():
            print(f"{c.name}: ", end="")
            separator = ""
            for model, capacity, comp_name in one_to_many:
                if comp_name == c.name:
                    print(f"{separator}{model}", end="")
                    separator = ", "
            print()

    print("\nЗадание E2")
    for c in computers:
        c_hdds = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_hdds) > 0:
            c_capacities = [capacity for _, capacity, _ in c_hdds]
            c_capacity_avg = sum(c_capacities) / len(c_capacities)
            print(f"{c.name}: {c_capacity_avg:.2f} ГБ")

    print("\nЗадание E3")
    for h in hdds:
        if h.model.lower().startswith("а") or h.model.lower().startswith("a"):
            print(f"{h.model}: ", end="")
            separator = ""
            printed_comps = set()
            for model, capacity, comp_name in many_to_many:
                if model == h.model and comp_name not in printed_comps:
                    print(f"{separator}{comp_name}", end="")
                    separator = ", "
                    printed_comps.add(comp_name)
            print()

if __name__ == "__main__":
    main()
