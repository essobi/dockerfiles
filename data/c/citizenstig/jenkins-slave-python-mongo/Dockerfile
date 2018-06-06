FROM citizenstig/jenkins-slave-python  
  
# Install and prepare mongo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10 &&
\  
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
mkdir /data && mkdir /data/db && \  
apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/  

