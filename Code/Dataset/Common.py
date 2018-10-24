
class Helper:

    def __init__(self):
        self.Foodtype = {"Pizza":["Cheese Pizza","Bacon Pizza","Veggie Pizza"],
                        "Bakeries":["Bagels","Waffles","Pancakes","Muffins"],
                        "Sandwich shop":["Turkey and Cheese","Egg Salad","Grilled Cheese"],
                        "Steak and BBQ":["BBQ Bacon Cheeseburger","Pork Poterhouse","Smoked Cheddar Burger"],
                        "Mexican":["Burrito","Taco","Enchilada"],
                        "Ice cream":["Strawberry","Mango","Oreo"],
                        "Chinese":["Chicken Chow Mein","Beef Lo Mein","Fried Dumpling"]}
        self.food_data = {0:"Pizza", 1:"Bakeries", 2:"Sandwich shop", 3:"Steak and BBQ", 4:"Mexican", 5:"Ice cream", 6:"Chinese"}

    def CalPercentage(self,arr,base):
        for row in range(0,len(arr)):
            arr[row] = round((arr[row]/base)*100,2)

    def GetFoodType(self):
        return self.Foodtype;

    def GetFoodData(self):
        return self.food_data;

    def GetTotalForRows(self,arr,total,num_rows):
        for value in range(0,num_rows):
            total[value] = sum(arr[value,:])

