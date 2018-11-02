<html>
    <head>
        <style>
        img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}</style>
</head>
<body background="bb1.jpg">
        
        <h1 class="logo">
    <IMG SRC="logo.jpg" ALT="FOOD BYTE" style="width:10%" WIDTH=100 HEIGHT=100></IMG>
  </h1>
</body>
</html>
<?php

if(isset($_POST['submit'])){
$selected_val = $_POST['Analytics'];  // Storing Selected Value In Variable
echo "Results for :" .$selected_val;  // Displaying Selected Value
}

?>