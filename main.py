import meccanoid.py
mec = Meccanoid()

mec.connect('04:A3:16:40:2C:27')

mec.servo(1, 0xAA)

mec.disconnect()


# In terminal we can use this to test but I wan't able to make it work
# (bash) gatttool -b 04:A3:16:40:2C:27 -I
# [LE]>  connect
# [LE]>  char-write-req 0x001f 191d1d1d1d1d1d1d1d1d1d1d1d1d1d1d10206



