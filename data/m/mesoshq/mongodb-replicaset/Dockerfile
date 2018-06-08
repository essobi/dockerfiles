FROM ubuntu:14.04  
MAINTAINER tobilg <tobilg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Install MongoDB  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends --force-yes \  
curl mongodb-org mongodb-org-server mongodb-org-shell mongodb-org-mongos
mongodb-org-tools && \  
echo "mongodb-org hold" | dpkg --set-selections && echo "mongodb-org-server
hold" | dpkg --set-selections && \  
echo "mongodb-org-shell hold" | dpkg --set-selections && \  
echo "mongodb-org-mongos hold" | dpkg --set-selections && \  
echo "mongodb-org-tools hold" | dpkg --set-selections && \  
curl -L --insecure https://github.com/stedolan/jq/releases/download/jq-1.5/jq-
linux64 -o /usr/bin/jq && \  
chmod +x /usr/bin/jq  
  
# Standard setting (can be overwritten by -e while running)  
ENV STORAGE_ENGINE wiredTiger  
ENV JOURNALING yes  
  
# Add run script for MongoDB  
ADD run.sh /usr/local/bin/run.sh  
  
# Add init script for MongoDB  
ADD init.sh /usr/local/bin/init.sh  
  
EXPOSE 27017  
CMD ["/usr/local/bin/run.sh"]

