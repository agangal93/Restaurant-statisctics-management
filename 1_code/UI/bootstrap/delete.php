<html>
<body>

<form action="remove.php" method="post">
<h1>Fooditem</h1><br>
  
  
<input type="text" name="Fooditem" value=""><br><br>
<h2>Price</h2>
  <input type="text" name="Price" value=""><br><br>
  <input type="submit" value="submit">
</form>
<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
    window.history.back();
}
</body>
</html>