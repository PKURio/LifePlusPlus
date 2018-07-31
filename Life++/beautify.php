<?php
	header("Access-Control-Allow-Origin: *");
	system("python ./beautify.py", $res);
	echo "OK"
?>