from i2clibraries import i2c_hmc5883l

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1) #choosing which i2c port to use, RPi2 model B uses port 1

hmc5883l.setContinuousMode()

hmc5883l.setDeclination(0,6) #type in the magnetic declination of your location in the bracket (degrees, minute)

print(hmc5883l)