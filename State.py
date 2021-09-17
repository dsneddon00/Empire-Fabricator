class State:

    def __init__(self):
        self.dataLst = []
        self.owner = 0
        self.xloc = 0
        self.yloc = 0
        self.des = 0
        self.effic = 0
        self.mobil = 0
        self.off = 0
        self.terr0 = 0
        self.terr1 = 0
        self.terr2 = 0
        self.terr3 = 0
        self.xdist = 0
        self.ydist = 0
        self.avail = 0
        self.work = 0
        self.coastal = 0
        self.newdes = 0
        self.min = 0
        self.gold = 0
        self.fert = 0
        self.ocontent = 0
        self.uran = 0
        self.oldown = 0
        self.civil = 0
        self.milit = 0
        self.shell = 0
        self.gun = 0
        self.petrol = 0
        self.iron = 0
        self.dust = 0
        self.bar = 0
        self.food = 0
        self.oil = 0
        self.lcm = 0
        self.hcm = 0
        self.uw = 0
        self.rad = 0
        self.c_dist = 0
        self.m_dist = 0
        self.s_dist = 0
        self.g_dist = 0
        self.p_dist = 0
        self.i_dist = 0
        self.d_dist = 0
        self.b_dist = 0
        self.f_dist = 0
        self.o_dist = 0
        self.l_dist = 0
        self.h_dist = 0
        self.u_dist = 0
        self.r_dist = 0
        self.c_del = 0
        self.m_del = 0
        self.s_del = 0
        self.g_del = 0
        self.p_del = 0
        self.i_del = 0
        self.d_del = 0
        self.b_del = 0
        self.f_del = 0
        self.o_del = 0
        self.l_del = 0
        self.h_del = 0
        self.u_del = 0
        self.r_del = 0
        self.fallout = 0
        self.access = 0
        self.road = 0
        self.rail = 0
        self.dfense = 0



    def appendOutputToDataLst(self):
        fin = open("outputSect.txt", "rt")
        for line in fin:
            for value in line.split():
                self.dataLst.append(value)
                print(value)
