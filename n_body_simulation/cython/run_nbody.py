import sys
import pyximport

pyximport.install()
import nbody

nbody.main(int(sys.argv[1]))

