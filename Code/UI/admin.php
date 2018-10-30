<?php
    session_start();
    if(!isset($_SESSION['login'])) {
        header('LOCATION:login.php'); die();
    }
?>
<html>
    <head>
        <style>
        img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}</style>

        <title>Admin Page</title>
    </head>
    <body background="bb1.jpg">
        <h5>Welcome manager</h5>
        <h1 class="logo">
    <IMG SRC="logo.jpg" ALT="FOOD BYTE" style="width:10%" WIDTH=100 HEIGHT=100></IMG>
  </h1>
  <h3 class="text-center"> Administration</h3>
        <form method="post" action="manager.php">
        <tr>
            <td><input type="radio" value="add" name="Analytics">1.ADD/DELETE MENU<br><p></p>
                <input type="radio" value="view" name="Analytics">2.VIEW INVENTORY<br><p></p>
                <input type="radio" value="modify" name="Analytics">3.MODIFY PRICE<br><p></p>
                <input type="radio" value="4.schedule" name="Analytics">4.EMPLOYEE SCHEDULE<br><p></p>
                <input type="radio" value="5.wage" name="Analytics">5.EMPLOYEE WAGE<br><p></p>
                <input type="radio" value="6.pl" name="Analytics">6.VIEW PROFIT/LOSS<br><p></p>

                <h3 class="text-center"> Analytics</h3>
                <input type="radio" value="inventory" name="Analytics">1.INVENTORY MANAGEMENT<br><p></p>
                <input type="radio" value="location" name="Analytics">2.GEOGRAPHICAL TREND ANALYSIS<br><p></p>
                <input type="radio" value="customerdensity" name="Analytics">3.CUSTOMER DENSITY ANALYSIS<br><p></p>
                <input type="radio" value="item" name="Analytics">4.ITEM BASED REVENUE ANALYSIS<br><p></p>
            </td>
        </tr>
        <tr>
        <button type="submit" name="submit" class="btn btn-default">Submit</button>    
        </tr>
        </form>
        
    </body> 
</html>