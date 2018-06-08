FROM ubuntu:14.04  
MAINTAINER Gary Leong <gwleong@gmail.com>  
  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10 &&
\  
# echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list && \  
# apt-get update && \  
# apt-get install -y pwgen mongodb-org mongodb-org-server mongodb-org-shell
mongodb-org-mongos mongodb-org-tools && \  
# echo "mongodb-org hold" | dpkg --set-selections && \  
# echo "mongodb-org-server hold" | dpkg --set-selections && \  
# echo "mongodb-org-shell hold" | dpkg --set-selections && \  
# echo "mongodb-org-mongos hold" | dpkg --set-selections && \  
# echo "mongodb-org-tools hold" | dpkg --set-selections  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10 &&
\  
apt-get update && \  
apt-get install -y pwgen wget curl git-core build-essential scons devscripts
lintian dh-make \  
libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-filesystem-
dev \  
libboost-program-options-dev libboost-system-dev libboost-thread-dev \  
libpcap-dev libreadline-dev libssl-dev rng-tools && \  
wget https://s3.amazonaws.com/jiffy-mongodb/mongodb-ssl_2.6.7_amd64.deb && \  
dpkg -i mongodb-ssl_2.6.7_amd64.deb  
  
RUN openssl req -newkey rsa:2048 -new -x509 -subj
"/C=US/ST=California/L=SanFrancisco/O=Dis/CN=www.selfsigned.com" -days 1024
-nodes -out mongodb.crt -keyout mongodb.key && \  
bash -c 'cat mongodb.crt mongodb.key > /etc/ssl/mongodb.pem'  
  
VOLUME /data/db  
  
ENV AUTH yes  
ENV JOURNALING yes  
  
ADD run.sh /run.sh  
ADD set_mongodb_password.sh /set_mongodb_password.sh  
ADD mongod.conf /etc/mongod.conf  
  
EXPOSE 27017 28017  
  
CMD ["/run.sh","-b0.0.0.0"]  

