FROM ubuntu:14.04  
MAINTAINER team@lastbackend.com  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
| sudo tee /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y pwgen mongodb-org mongodb-org-server mongodb-org-shell
mongodb-org-mongos mongodb-org-tools && \  
echo "mongodb-org hold" | dpkg --set-selections && \  
echo "mongodb-org-server hold" | dpkg --set-selections && \  
echo "mongodb-org-shell hold" | dpkg --set-selections && \  
echo "mongodb-org-mongos hold" | dpkg --set-selections && \  
echo "mongodb-org-tools hold" | dpkg --set-selections  
  
VOLUME /data/db  
  
ENV AUTH yes  
ENV JOURNALING yes  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
EXPOSE 27017 28017  
CMD ["/init.sh"]

