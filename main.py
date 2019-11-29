# from bengalaHelp import Helps
from Ultrassom.UltraSonic import UltraSonic
# help = Helps()
# help.run()

ultrassom = UltraSonic()
while True:
  print(ultrassom.getDist())
