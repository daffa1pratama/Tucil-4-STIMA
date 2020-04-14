<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KMP Matcher</title>
</head>
<body>
    <div style="border-style: solid">
    <!-- PAGE TITLE -->
        <h1> My InfoExtraction App </h1>

        <form action="submit.php" method="post" enctype="multipart/form-data">
            <!-- SELECT FOLDER -->
            <label for="file"> Folder : </label>
            <input type="file" name="file" accept=".txt" required><br>

            <!-- INPUT KEYWORD -->
            <label for="keyword"> Keyword : </label>
            <input type="text" name="keyword" id="keyword" required><br>

            <!-- SELECT ALGORITMA -->
            <label for="algoritma"> Algoritma : <br></label>
            <input type="radio" name="algoritma" id="algoritma" value="boyermoore" required> Boyer-Moore <br>
            <input type="radio" name="algoritma" id="algoritma" value="kmp"> KMP <br>
            <input type="radio" name="algoritma" id="algoritma" value="regex"> Regex <br>
            <input type="submit" name="submit" value="Submit"></button>
        </form>
        <label for=""> Result : <br></label>
    </div>
</body>
</html>
