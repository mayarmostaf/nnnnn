class wizard :
    health =100
    energy=500
    sheild_limit=3
    spells=dict()
    def dec_health(self,pw1,pw2): #that aregular fun which applied on instance and it only dec health when spell is not sheild
        if pw1 != 0 and pw2 != 0:
            self.health -= abs(pw1 - pw2)
    def dec_energy(self,pw):#that a regular func which applied to instance and it doenesnt dec if spell is sheild
        if pw!=0:
          self.energy-=pw


harry=wizard()
harry.spells={
"AvadaKedavra":100,
"Crucio" :40,
"Imperio" :20,
"sheild" : 0,
 "Reducto":60,
 "Fiendfyre": 50,
"Nebulus": 4
}
voldemart=wizard()
voldemart.spells={
"AvadaKedavra":100,
"Crucio" :40,
"Imperio" :20,
"sheild" : 0,
 "Taboo":80,
 "Expulso":60,
"Confringo":55
}

while( harry.health >0 and harry.energy>0) and (voldemart.health >0 and voldemart.energy>0)and(harry.sheild_limit>0 and voldemart.sheild_limit>0) :
   print ("enter the two spells (harry then voldmart ):\n ")
   spell_string = input()
   h_spell, v_spell = spell_string.split() #take each input individually
   if h_spell == "sheild":#dec opportunity of sheild on using it
       harry.sheild_limit -= 1
   elif v_spell == "sheild":#dec opportunity of sheild on using it
       voldemart.sheild_limit -= 1
   pw1 = harry.spells[h_spell]  # calling the value (power of spell ) using key (spell)
   pw2 = voldemart.spells[v_spell]# calling the value (power of spell ) using key (spell)
   if pw1 > pw2:#the loser health dec if it is voldemart
       voldemart.dec_health(pw1, pw2)
   elif pw2 > pw1:#the loser health dec if it is harry
       harry.dec_health(pw1, pw2)
   harry.dec_energy(pw1)# each time wizard energy dec
   voldemart.dec_energy(pw2)# each time wizard energy dec
   print("\t\tharry\t\tvoldemart\n")
   print("health:\t" + str(harry.health) + "\t\t\t" +str( voldemart.health) + "\n")
   print("energy:\t" +str( harry.energy) + "\t\t\t" + str(voldemart.energy) + "\n")
if harry.health > voldemart.health:
    print("harry is the winner")
elif voldemart.health > harry.health:
    print("voldemart is the winner")
#program works as long as you enter the spells right with upper and lower case