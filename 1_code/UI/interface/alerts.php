<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="bb.css">
</head>
<body>

</body>
</html>
<?php

 $conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
 mysqli_select_db($conn,'restaurant');

 $sqlCommand="SELECT * FROM lowstock";
 $query=mysqli_query($conn,$sqlCommand);


 if (!$query) {
     printf("Error: %s\n", mysqli_error($conn));
     exit();
 }

echo "<table border=5>";
 echo"<tr><td>ItemName</td><td>Percentage</td><tr>";
 while($row = mysqli_fetch_array($query))
 {   
 echo "<tr><td>" . $row['ItemName'] . "</td><td>" . $row['Perc'] . "</td></tr>";  
 }

 echo "</table>"; 
 mysqli_close($conn);
?>
