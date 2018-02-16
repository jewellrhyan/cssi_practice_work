class Spaceships:
  def __init__ (self, spaceship_doors, spaceship_aliens):
    self.doors = spaceship_doors
    self.aliens = spaceship_aliens
  def drinkWater(self):
    print "The spaceship has a %s with a %s inside. It needs some water." % (self.doors, self.aliens)

shiny = Spaceships("shiny door", "shiny cat")
neonblue = Spaceships("neon blue door", "neon blue cat")

shiny.drinkWater()
neonblue.drinkWater()
