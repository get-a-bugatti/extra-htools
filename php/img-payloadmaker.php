<?php
function convertToFakeJPG($inputFile, $outputFile) {
    // Define JPEG magic number (Start of Image - SOI marker)
    $jpegMagicNumber = "\xFF\xD8\xFF";
    
    // Read the contents of the original PHP file
    $phpContent = file_get_contents($inputFile);
    if ($phpContent === false) {
        die("Error: Unable to read the input file.\n");
    }

    // Combine the JPEG magic number with the original PHP content
    $fakeJpgContent = $jpegMagicNumber . $phpContent;

    // Write the combined content to the new file
    if (file_put_contents($outputFile, $fakeJpgContent) === false) {
        die("Error: Unable to write to the output file.\n");
    }

    echo "Fake JPEG created: $outputFile\n";
    echo "MIME type detected: " . mime_content_type($outputFile) . "\n";
}

// Example usage
$inputPhpFile = 'example.php'; // Path to your PHP file
$outputFakeJpg = 'fake_image.jpg'; // Path for the fake JPEG file

convertToFakeJPG($inputPhpFile, $outputFakeJpg);
?>

