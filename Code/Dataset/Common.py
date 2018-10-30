
class Helper:

    def __init__(self):
        self.Foodtype = {"Pizza":["Cheese Pizza","Bacon Pizza","Veggie Pizza"],
                        "Bakeries":["Bagels","Waffles","Pancakes","Muffins"],
                        "Sandwich shop":["Turkey and Cheese Sandwich","Egg Salad","Grilled Cheese Sandwich"],
                        "Steak and BBQ":["BBQ Bacon Cheeseburger","Pork Porterhouse","Smoked Cheddar Burger"],
                        "Mexican":["Burrito","Taco bowl","Enchilada"],
                        "Ice cream":["Strawberry Shake","Mango Smoothie","Oreo Shake"],
                        "Chinese":["Chicken Chow Mein","Beef Lo Mein","Fried Dumpling"]}
        self.food_data = {0:"Pizza", 1:"Bakeries", 2:"Sandwich shop", 3:"Steak and BBQ", 4:"Mexican", 5:"Ice cream", 6:"Chinese"}
        self.zone_data = {0:"EZ", 1:"NZ", 2:"WZ", 3:"SZ", 4:"CZ"}       
        self.east_zone = ["New York", "Maryland", "Virginia", "New Jersey"]
        self.north_zone = ["Wisconsin", "Minnesota", "North Dakota", "Michigan"]
        self.west_zone = ["California", "Washington", "Arizona", "Oregon"]
        self.south_zone = ["Texas", "New Mexico", "Mississippi", "Georgia"]
        self.central_zone = ["Colorado", "Utah", "Nebraska", "Kansas"]
        self.num_entries = 500
        self.food_entry = {"Cheese Pizza":0,"Bacon Pizza":1,"Veggie Pizza":2,"Bagels":3,"Waffles":4,"Pancakes":5,"Muffins":6,
                           "Turkey and Cheese Sandwich":7,"Egg Salad":8,"Grilled Cheese Sandwich":9,"BBQ Bacon Cheeseburger":10,"Pork Porterhouse":11,"Smoked Cheddar Burger":12,
                           "Burrito":13,"Taco bowl":14,"Enchilada":15,"Strawberry Shake":16,"Mango Smoothie":17,"Oreo Shake":18,
                           "Chicken Chow Mein":19,"Beef Lo Mein":20,"Fried Dumpling":21}
        self.price = {"Cheese Pizza":13.25,"Bacon Pizza":15.50,"Veggie Pizza":14,"Bagels":5.49,"Waffles":2.50,"Pancakes":5.89,"Muffins":5.99,
                      "Turkey and Cheese Sandwich":6.49,"Egg Salad":4.99,"Grilled Cheese Sandwich":4.29,"BBQ Bacon Cheeseburger":6.29,
                      "Pork Porterhouse":29.99,"Smoked Cheddar Burger":14.25,"Burrito":6.50,"Taco bowl":6.50,
                      "Enchilada":5.99,"Strawberry Shake":2.19,"Mango Smoothie":3.79,"Oreo Shake":2.79,
                      "Chicken Chow Mein":7.35,"Beef Lo Mein":7.75,"Fried Dumpling":4.95}

    def CalPercentage(self,arr,base):
        for row in range(0,len(arr)):
            arr[row] = round((arr[row]/base)*100,2)

    def GetFoodType(self):
        return self.Foodtype;

    def GetFoodData(self):
        return self.food_data;

    def GetZoneData(self):
        return self.zone_data;

    def GetTotalForRows(self,arr,total,num_rows):
        for value in range(0,num_rows):
            total[value] = sum(arr[value,:])

    def GetEastZone(self):
        return self.east_zone

    def GetNorthZone(self):
        return self.north_zone

    def GetWestZone(self):
        return self.west_zone

    def GetSouthZone(self):
        return self.south_zone

    def GetCentralZone(self):
        return self.central_zone

    def GetNumEntries(self):
        return self.num_entries

    def GetFoodEntry(self):
        return self.food_entry

    def GetKeyByValue(self,dictOfWords, Value, IsSingle):
        for (key, value) in dictOfWords.items():
            if IsSingle:
                if Value == value:
                    break
            else:
                if Value in value:
                    break
        return key

    def GetFoodCategory(self,Entry):
        for row in range(0,len(self.Foodtype)):
            type_item = self.food_data.get(row)
            assert (type_item is not None),"Invalid food type"
            if Entry in self.Foodtype.get(type_item):
                Type_of_Food = self.GetKeyByValue(self.Foodtype,self.Foodtype.get(type_item),True)
                break
        return Type_of_Food

    def GetPriceItem(self):
        return self.price