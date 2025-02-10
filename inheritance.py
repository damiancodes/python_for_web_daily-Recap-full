class Dad:
    def football(self):
        print("dad like watching football")



class Mum(Dad):
    def cooking(self):
        print("mum like cooking")



class Boy(Dad):
    def  Boyage(self):
        print("The boy is 15 years")


class Girl(Mum):
    def Girl(self):
        print("The girl is 15 years")



my_boy=Boy()
my_boy.football()
my_boy.Boyage()


my_girl=Girl()
my_girl.cooking()
my_girl.Girl()
