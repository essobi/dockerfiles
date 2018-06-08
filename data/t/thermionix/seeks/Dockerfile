from ubuntu:precise  
  
env DEBIAN_FRONTEND noninteractive  
  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list.d/precise.list && apt-get update  
run apt-get install -y --no-install-recommends python-software-properties  
  
run add-apt-repository -y ppa:seeks-packaging/ppa && apt-get update  
  
run apt-get install -y seeks  
  
run sed -i 's/127.0.0.1:8250/0.0.0.0:8250/' /etc/seeks/config  
  
expose 8250  
cmd /usr/bin/seeks  

