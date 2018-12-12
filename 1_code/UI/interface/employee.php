<!DOCTYPE html>
<html>
<head>
	<title></title>
	<h1>EMPLOYEE PREFERRED SCHEDULE</h1>
</head>
<body>

</body>
</html>


<?php

$conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
mysqli_select_db($conn,'restaurant');

$sqlCommand="SELECT * FROM details"; //You don't need a ; like you do in SQL
$query=mysqli_query($conn,$sqlCommand);

echo "<table border=5>"; // start a table tag in the HTML
echo"<tr><td>ID</td><td>Name</td><td>Shift</td><tr>";
while($row = mysqli_fetch_array($query))

{   //Creates a loop to loop through results
echo "<tr><td>" . $row['ID'] . "</td><td>" . $row['Name'] ."</td><td>". $row['Shift'] . "</td></tr>";  //$row['index'] the index here is a field name
}

echo "</table>"; //Close the table in HTML

mysqli_close($conn);
?>

<html>
<br>

<link rel="stylesheet" type="text/css" href="bb.css">


<body>

<form action="mailto:yashasvi261196@gmail.com" method="post" enctype="text/plain">


</form>
<br>
<br>
<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
    window.history.back();
}
</script>
</body>
</html>







