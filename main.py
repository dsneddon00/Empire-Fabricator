import EmpireDB


def main():
    db = EmpireDB.EmpireDB()
    print(db.getAllFromEmpire()[0]["name"])


if __name__ == "__main__":
    main()
