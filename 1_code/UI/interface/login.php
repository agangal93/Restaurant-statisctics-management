<?php
    session_start();
    echo isset($_SESSION['login']);
    if(isset($_SESSION['login'])) {
      header('LOCATION:login.php'); die();
    }
?>
<!DOCTYPE html>
<html>
   <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
    
    <meta http-equiv='content-type' content='text/html;charset=utf-8' />
     <title> Manager Login</title>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

   </head>
<body background="bb.jpg">

  <h1 class="logo">
    <IMG SRC="logo.jpg" ALT="FOOD BYTE" style="width:20%" WIDTH=150 HEIGHT=200></IMG>
  </h1>
  
  
  <div class="container">
    <center>
    <h3 class="text-center"> Manager  Login</h3>
    <?php
    //if the submit button is clicked with user input
    //it is verified if the username and password are valid 
      if(isset($_POST['submit'])){
        $username = $_POST['username']; $password = $_POST['password'];
        if($username === 'manager' && $password === 'password'){
          $_SESSION['login'] = true; header('LOCATION:menu.html'); //if valid data is  provided as input in links to admin page
          die();
        } {
          echo "<div class='alert alert-danger'>Username and Password do not match.</div>";//if invalid input is provided it provides an alert message
        }

      }
      
    ?>

    <form action="" method="post">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" class="form-control" id="username" name="username" required>
      </div>
      <p>
        
      </p>
      <div class="form-group">
        <label for="pwd">Password:</label>
        <input type="password" class="form-control" id="pwd" name="password" required>
      </div>
      <p>
        
      </p>
      <button type="submit" name="submit" class="btn btn-default">Login</button>
    </form>
  </div>
</center>
</body>
</html>