import Common
import Location
import CustomerDensity
import Dataethnic

H = Common.Helper()
L = Location.Location()
C = CustomerDensity.DensityTime()
E = Dataethnic.EthnicState()

L.CreateLocationDataset()
C.CreateDensityTime()
E.CreateEthnicset()