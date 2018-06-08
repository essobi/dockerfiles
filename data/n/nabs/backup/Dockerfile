FROM ubuntu:trusty  
MAINTAINER Titeya <contact@titeya.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \  
apt-get update && \  
apt-get install -y mongodb-org-shell mongodb-org-tools ncftp && \  
apt-get install -y --no-install-recommends mysql-client && \  
echo "mongodb-org-shell hold" | dpkg --set-selections && \  
echo "mongodb-org-tools hold" | dpkg --set-selections && \  
mkdir /backup  
  
RUN echo Europe/Paris | tee /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata && mkdir /scripts  
  
ENV CRON_TIME="0 0 * * *"  
ADD scripts/run.sh /scripts/run.sh  
VOLUME ["/backup"]  
CMD ["/scripts/run.sh"]  

