<?php
	header("Access-Control-Allow-Origin: *");

	$base64_image_content = $_POST['imgBase64'];
	$flag = 0;
	//匹配出图片的格式
	if (preg_match('/^(data:\s*image\/(\w+);base64,)/', $base64_image_content, $result)) {
		$type = $result[2];
		$new_file = "./1.{$type}";
		$res = file_put_contents($new_file, base64_decode(str_replace($result[1], '', $base64_image_content)));
 		if ($res != 0)
			$flag = 1;
	}

	$score = system("python ./score.py ./1.jpeg", $res);
	echo $score
?>