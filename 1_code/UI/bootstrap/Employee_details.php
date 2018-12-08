<?php
$Shift = $_POST['Shift'];

#$Date = date("Y-m-d",strtotime($_POST['Date']));
$Date = $_POST['Date'];



 $conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
 mysqli_select_db($conn,'restaurant');

 $sqlCommand="SELECT * FROM allocation WHERE Shift='$_POST[Shift]'AND Date='$_POST[Date]'";
 $query=mysqli_query($conn,$sqlCommand);


 if (!$query) {
     printf("Error: %s\n", mysqli_error($conn));
     exit();
 }

echo "<table border=5>";
 echo"<tr><td>EMP_ID</td><td>Name</td><td>Shift</td><tr>";
 while($row = mysqli_fetch_array($query))
 {   
 echo "<tr><td>" . $row['Emp_ID'] . "</td><td>" . $row['Name'] ."</td><td>". $row['Shift'] . "</td></tr>";  
 }

 echo "</table>"; 
 mysqli_close($conn);
?>