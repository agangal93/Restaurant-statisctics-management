import random

## Helper - Class of helper functions for the individual categories of dataset generation
#
class Helper:

    ## The constructor. Initializes Cusine_type, Cusine_map, zone_map, Cusine and Cusine_price hashmap
    # @param self The object pointer
    def __init__(self):
        self.Cusine_div = {"Mexican":0.81, "Italian":0.87, "American":0.58, "Chinese":0.76, "Mediteranean":0.42, "Japanese":0.37, "Thai":0.25, "Indian":0.18}
        self.Cusine_map = {0:"Mexican", 1:"Italian", 2:"American", 3:"Chinese", 4:"Mediteranean", 5:"Japanese", 6:"Thai", 7:"Indian"}
        
        self.Cusine_type = {"Mexican":["Chilaquiles", "Tacos", "Enchiladas", "Quesadillas"],
                        "Italian":["Pepperoni pizza", "Spaghetti and meatballs", "Fettuccine Alfredo", "Chicken parmesan"],
                        "American":["Turkey and Cheese Sandwich","BBQ Bacon Cheeseburger","Chicken Fried Steak"],
                        "Chinese":["Chicken Chow Mein","Beef Lo Mein","Fried Dumpling"],
                        "Mediteranean":["Falafel","Fattet Hummus","Spanakopita"],
                        "Japanese":["Sushi","Sashimi","Tempura","Tonkatsu"],
                        "Thai":["Tom Yum Goong","Khao Soi","Pad See ew"],
                        "Indian":["Butter Chicken","Tandoori Chicken","Alu Gobi"]}

        self.zone_map = {0:"EZ", 1:"NZ", 2:"WZ", 3:"SZ", 4:"CZ"}

        self.total_entries = 10000
        self.num_subset_entries = 2000
        self.num_subsets = 5

        self.Cusine = {"Chilaquiles":0,"Tacos":1,"Enchiladas":2,"Quesadillas":3,"Pepperoni pizza":4,"Spaghetti and meatballs":5,"Fettuccine Alfredo":6,
                        "Chicken parmesan":7,"Turkey and Cheese Sandwich":8,"BBQ Bacon Cheeseburger":9,"Chicken Fried Steak":10,"Chicken Chow Mein":11,"Beef Lo Mein":12,
                        "Fried Dumpling":13,"Falafel":14,"Fattet Hummus":15,"Spanakopita":16,"Sushi":17,"Sashimi":18,"Tempura":19,"Tonkatsu":20,"Tom Yum Goong":21,
                        "Khao Soi":22,"Pad See ew":23,"Butter Chicken":24,"Tandoori Chicken":25,"Alu Gobi":26}

        self.Cusine_price = {"Chilaquiles":5.00,"Tacos":6.50,"Enchiladas":5.99,"Quesadillas":6.19,"Pepperoni pizza":15.50,"Spaghetti and meatballs":7.69,"Fettuccine Alfredo":12.99,
                           "Chicken parmesan":16.99,"Turkey and Cheese Sandwich":6.49,"BBQ Bacon Cheeseburger":6.29,"Chicken Fried Steak":11.99,"Chicken Chow Mein":7.35,"Beef Lo Mein":7.75,
                           "Fried Dumpling":4.95,"Falafel":2.99,"Fattet Hummus":6.99,"Spanakopita":9.95,"Sushi":10.50,"Sashimi":15.99,"Tempura":11.00,"Tonkatsu":15.99,"Tom Yum Goong":8.50,
                           "Khao Soi":6.50,"Pad See ew":6.99,"Butter Chicken":9.59,"Tandoori Chicken":8.39,"Alu Gobi":5.99}
        
        self.DistributionType = ["Gaussian","Increase","Decrease"]

        self.DistIncrease = {"Tacos":"EZ","Falafel":"WZ","Butter Chicken":"NZ"}
        self.DistDecrease = {"Chicken parmesan":"NZ","Enchiladas":"SZ","Pepperoni pizza":"EZ"}
        self.DistGaussian = {"Chilaquiles":"WZ","Falafel":"EZ","Fattet Hummus":"SZ"}

        self.IngredienTest = ["Corn Tortillas","Eggs","Olive Oil","Cheese"]

    ## Calculate Percentage of each array entry using base value
    def CalPercentage(self,arr,base):
        for row in range(0,len(arr)):
            arr[row] = round((arr[row]/base)*100,2)

    ## Get Total number of entries
    def GetTotalNumEntries(self):
        return self.total_entries

    ## Get number of subset entries to be generated
    def GetNumSubsetEntries(self):
        return self.num_subset_entries

    def GetCusineDivision(self):
        return self.Cusine_div

    ## Get Cusine type dict
    def GetCusineType(self):
        return self.Cusine_type

    ## Get Cusine map dict
    def GetCusineMap(self):
        return self.Cusine_map

    ## Get Zone map dict
    def GetZoneMap(self):
        return self.zone_map

    ## Get Cusine Entry dict
    def GetCusine(self):
        return self.Cusine

    ## Get Price of Cusine
    def GetCusinePrice(self):
        return self.Cusine_price

    ## Get distribution type
    def GetDistributionType(self):
        return self.DistributionType

    ## Get Key of the dictionary using input value
    # @param dictionary, Value, IsSingle
    def GetKeyByValue(self,dictOfWords, Value, IsSingle):
        for (key, value) in dictOfWords.items():
            if IsSingle:
                if Value == value:
                    break
            else:
                if Value in value:
                    break
        return key

    ## Get Food Category from Food Entry
    # @param self, Food Entry
    def GetCusineType_FromCusine(self,Entry):
        for row in range(0,len(self.Cusine_type)):
            type_item = self.Cusine_map.get(row)
            assert (type_item is not None),"Invalid food type"
            if Entry in self.Cusine_type.get(type_item):
                Type_of_Cusine = self.GetKeyByValue(self.Cusine_type,self.Cusine_type.get(type_item),True)
                break
        return Type_of_Cusine

    ## Calculate total of input array values
    def GetTotalForRows(self,arr,total,num_rows):
        for value in range(0,num_rows):
            total[value] = sum(arr[value,:])

    ## Get num of subsets
    def GetNumSubsets(self):
        return self.num_subsets

    ## RoundingCorrection - Correct the error generated during rounding of floating point values to floor integers
    # @param self The object pointer, array, percentage conversion
    #
    def RoundingCorrection(self,arr,expected_entries,length):
        total = sum(arr)
        error = expected_entries - total
        assert (error >= 0),"Error should not be negative"
        while error > 0:
            arr[random.randint(0,length-1)] += 1
            error -= 1

    ## Get Increase distribution
    def GetDistIncrease(self):
        return self.DistIncrease

    ## Get decrease distribution
    def GetDistDecrease(self):
        return self.DistDecrease

    ## Get gaussian distribution
    def GetDistGaussian(self):
        return self.DistGaussian

    ## Get Ingredient test list
    def GetIngredientTestList(self):
        return self.IngredienTest