FROM ubuntu:precise  
  
RUN apt-get update;\  
echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list;\  
apt-get -y install python-software-properties;\  
add-apt-repository -y ppa:chris-lea/redis-server;\  
apt-get update;\  
apt-get install -y redis-server;\  
apt-get clean  
  
EXPOSE 6379  
  
ENTRYPOINT ["redis-server"]  

