import os
print("os.name:")
print (os.name)
import platform

print("release.system:")
rs = platform.system() #returns the base system, in your case Linux
print(rs)
print("release.release:")
pr = platform.release() #returns release version
print (pr)

print("platform.linux_distribution()")
ld = platform.linux_distribution()
print(ld)