<?php

$conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
mysqli_select_db($conn,'employee_shifts');

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
<body>
<form action="mailto:yashasvi261196@gmail.com" method="post" enctype="text/plain">

<br><br><br>
<tr><td>Employee_Id  </td><tr>
<select name="employee_id">

<?php 
$conn = mysqli_connect('localhost', 'root', ''); //The Blank string is the password
mysqli_select_db($conn,'employee_shifts');
$sql = mysqli_query($conn, "SELECT ID FROM details");
while ($row = $sql->fetch_assoc()){
echo "<option value=\"id\">" . $row['ID'] . "</option>";
}
?>
</select>

<br><br>
<tr><td>Shift</td>

<input type="text" name="shift" value""><br><br>
<input type="submit"  value"submit">
</form>
<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
    window.history.back();
}
</body>
</html>







