FROM kpmeen/docker-scala-sbt  
  
# Install MongoDB  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \  
echo "deb http://ftp.debian.org/debian jessie-backports main" | tee
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install -y mongodb-org-shell pandoc curl apt-transport-https ca-
certificates software-properties-common  
  
# Install docker  
RUN \  
curl -fsSL https://yum.dockerproject.org/gpg | apt-key add \- && \  
add-apt-repository "deb https://apt.dockerproject.org/repo/
debian-$(lsb_release -cs) main" && \  
apt-get update && \  
apt-get -y install docker-engine  
  
WORKDIR /root  
  

