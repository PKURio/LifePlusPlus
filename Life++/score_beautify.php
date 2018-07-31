<?php
	header("Access-Control-Allow-Origin: *");

	$score = system("python ./score.py ./2.jpeg", $res);
	echo $score
?>