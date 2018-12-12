<html>
<link rel="stylesheet" type="text/css" href="bb.css"></html>

<?php
    
$Fooditem = $_POST['Fooditem'];
$Price=$_POST['Price'];

$con = mysqli_connect("localhost", "root", ""); // Establishing Connection with Server

if(!$con)
{
die("not connected to server");
}
mysqli_select_db( $con,"restaurant");

if(!mysqli_select_db($con,'restaurant'))
{
echo'database not selected';
}


$UpdateQuery="UPDATE fooditem SET Fooditem='$_POST[Fooditem]',Price='$_POST[Price]' WHERE Fooditem='$_POST[Fooditem]'";

mysqli_query($con,$UpdateQuery);
if(!mysqli_query($con,$UpdateQuery))
{
echo "not Updated";
}
else
{
echo" The menu has been Updated";
}
mysqli_close($con);

?>
<br>
<br>
<?php

$conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
mysqli_select_db($conn,'restaurant');

$sqlCommand="SELECT * FROM fooditem"; //You don't need a ; like you do in SQL
$query=mysqli_query($conn,$sqlCommand);

echo "<table border=5>"; // start a table tag in the HTML
echo"<tr><td>Fooditem</td><td>Price</td><tr>";
while($row = mysqli_fetch_array($query))

{   //Creates a loop to loop through results
echo "<tr><td>" . $row['Fooditem'] . "</td><td>" . $row['Price'] . "</td></tr>";  //$row['index'] the index here is a field name
}

echo "</table>"; //Close the table in HTML

mysqli_close($conn);
?>
<br>
