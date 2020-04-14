<?php 
    if (isset($_POST['submit'])) {
        $file = $_FILES['file'];

        $fileName = $file['name'];
        $fileTmp = $file['tmp_name'];
        $fileError = $file['error'];

        $fileExt = explode('.', $fileName);
        $fileActExt = strtolower(end($fileExt));

        if ($fileError === 0) {
            $fileDestination = "uploaded/".$fileName.".txt";
            move_uploaded_file($fileTmp, $fileDestination);
            echo $fileName.".".$fileActExt."<br>";
            // header("Location: index.php?uploadsuccess");
        } else {
            echo "Error uploading file";
        }

        $algoritma = $_POST['algoritma'];

        if ($algoritma === "boyermoore") {
            echo "BOYER-MOORE";
        } else if ($algoritma === "kmp") {
            echo "KMP";
        } else {
            echo "REGEX";
        }

        $command = escapeshellcmd("main.py ".$algoritma);
        $output = shell_exec($command);
        echo $output;
    }
?>