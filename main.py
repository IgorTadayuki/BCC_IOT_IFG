# from bengalaHelp import Helps
from Ultrassom import UltraSonic
# help = Helps()
# help.run()

ultrassom = UltraSonic()
while True:
  print(ultrassom.getDist())
