<?php
$a = array();
exec('python ./subscribe.py',$a);
echo $a[0];
?>




