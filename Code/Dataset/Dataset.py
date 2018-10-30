import Common
import Location
import CustomerDensity
import Dataethnic

H = Common.Helper()
L = Location.Location()
E = Dataethnic.EthnicState()
C = CustomerDensity.DensityTime()

FoodCount = L.CreateLocationDataset()
EthnicCount = E.CreateEthnicset()
C.CreateDensityTime(FoodCount,EthnicCount)
