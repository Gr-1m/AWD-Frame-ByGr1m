<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
function broadcast(){

}
while (1){ broadcast(); usleep(5000); }
?>