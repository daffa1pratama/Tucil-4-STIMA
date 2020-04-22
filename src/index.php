<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Extractor</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-3">
    <!-- PAGE TITLE -->
        <div class="text-center">
            .
            <h1>Informator</h1>
            <p>Get your infomation here!</p>
        </div>
        <form action="submit.php" method="post" enctype="multipart/form-data">
        <!-- SELECT FOLDER -->
        <div class="was-validated">
            <label for="file">Folder</label>
            <div class="input-group custom-file mb-3">
                <input type="file" class="custom-file-input" name="file" accept=".txt" id="file" required>
                <label for="file" class="custom-file-label" id="file">Select file</label>
                <div class="invalid-feedback">Invalid file</div>
            </div>
        </div>
        <!-- SELECT FOLDER -->
        <!-- INPUT KEYWORD -->
        <label for="keyword">Keyword</label>
        <div class="input-group mb-3">
            <input type="text" class="form-control" name="keyword" id="keyword" autofocus autocomplete="off" required>
        </div>
        <!-- INPUT KEYWORD -->
        <!-- SELECT ALGORITMA -->
        <label for="algoritma">Algoritma</label>
        <div class="input-group mb-3">
            <select name="algoritma" id="algoritma" class="custom-select" required>
                <option value="">Select algorithm</option>
                <option value="bm">Boyer-Moore</option>
                <option value="kmp">Knuth-Morris-Pratt</option>
                    <option value="regex">Regex</option>
                </select>
                <div class="invalid-feedback">Invalid input</div>
            </div>
            <div class="input-group mb-3">
                <input type="submit" class="btn btn-primary" name="submit" value="Submit"></button>
            </div>
        </form>
        <!-- SELECT ALGORITMA -->
        <div class="mb-5">
            
            <?php 
                if (!$_GET) {
                    
                }
                else if (($_GET['s'])==='success') {
                    echo "<p>Result</p>";
                    $fileName = $_GET['filename'];
                    $keyword = $_GET['keyword'];
                    $algoritma = $_GET['algoritma'];
                    $command = escapeshellcmd("python main.py ".$fileName." ".$keyword." ".$algoritma);
                    $output = shell_exec($command);
                    echo $output;
                }
                ?>
        </div>
    </div>
<!-- Footer -->
<footer class="page-footer font-small fixed-bottom">
    <div class="footer-copyright text-center py-3 bg-light footer-light">© IF2211 Strategi Algoritma : 13518033 / Daffa Pratama Putra</div>
</footer>
<!-- Footer -->
</body>
</html>
