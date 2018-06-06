FROM ubuntu:precise  
  
RUN apt-get update;\  
echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list;\  
apt-get -y install python-software-properties;\  
add-apt-repository -y ppa:chris-lea/node.js;\  
apt-get update;\  
apt-get install -y nodejs;\  
apt-get clean  

