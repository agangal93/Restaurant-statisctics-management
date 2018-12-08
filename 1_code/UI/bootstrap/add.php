<html>
<body>


<form  method="post" action="index.php"> 
<h1>Fooditem</h1><br>
  <input type="text" name="Fooditem" value=""><br>
  <h2>Price</h2><br>
  <input type="text" name="Price" value=""><br><br>
  <input type="submit" value="submit">
</form>
<br>
<br>
<button onclick="goBack()">Go Back</button>

<script>
function goBack() {
    window.history.back();
}
</script>
</button>

</body>
</html>
