import EmpireDB


def main():
    db = EmpireDB.EmpireDB()
    #print("Test getAllFromEmpire:", db.getAllFromEmpire()[0]["name"])
    #print("Test getOneFromEmpire:", db.getOneFromEmpire(1))
    db.updateLog(1, "Gamer")
    #db.createLog("Testing")
    #print("Test getAllFromEmpire:", db.getAllFromEmpire()[0]["name"])
    #print("Test getOneFromEmpire:", db.getOneFromEmpire(2))
    print(db.getAllFromEmpire())

if __name__ == "__main__":
    main()
