  
from sjfloat/dev  
  
user root  
run echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-bockports.list  
run apt-get update && apt-get -t jessie-backports install -y \  
openjdk-8-dbg \  
openjdk-8-doc  
  
user $USER  
cmd $SHELL -l  

