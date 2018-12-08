<html>
<body>

<h1>Fooditem:</h1><br>
<form action="modprice.php" method="post">
  <input type="text" name="Fooditem" value=""><br>
  <h2>Price:</h2><br>
  <input type="text" name="Price" value=""><br><br>
  <input type="submit" value="Submit">
</form>
<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
    window.history.back();
}
</script>
</body>
</html>