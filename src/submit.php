<?php
    if (isset($_POST['submit'])) {
        $file = $_FILES['file'];

        $fileName = $file['name'];
        $fileTmp = $file['tmp_name'];
        $fileError = $file['error'];
        // echo $fileName;
        if ($fileError === 0) {
            $fileDestination = "uploaded/".$fileName;
            move_uploaded_file($fileTmp, $fileDestination);
        } else {
            header("Location: index.php?upload=failed");
        }

        $query = array(
            's' => 'success',
            'filename' => $fileName,
            'keyword' => $_POST['keyword'],
            'algoritma' => $_POST['algoritma']
        );
        $query = http_build_query($query);
        header("Location: index.php?$query");
    }
?>