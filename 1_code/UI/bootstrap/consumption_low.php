
<?php

 $conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
 mysqli_select_db($conn,'restaurant');

 $sqlCommand="SELECT ItemName FROM inventory WHERE Priority ='L'";
 $query=mysqli_query($conn,$sqlCommand);


 if (!$query) {
     printf("Error: %s\n", mysqli_error($conn));
     exit();
 }

echo "<table border=5>";
 echo"<tr><td>ItemName</td><tr>";
 while($row = mysqli_fetch_array($query))
 {   
 echo "<tr><td>" . $row['ItemName'] . "</td></tr>";  
 }

 echo "</table>"; 
 mysqli_close($conn);
?>

<html>
<head>
<style>
div.img_holder img
{
	float: left;
}
</style>
</head>
<body>
    <img src="LeastConsumed.png"  style="width:100%"/>
</div>
</body>
</html>