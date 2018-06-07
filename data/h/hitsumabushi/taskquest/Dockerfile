FROM hitsumabushi/ubuntu  
  
MAINTAINER hitsumabushi  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install basic tools  
RUN \  
apt-get update && \  
apt-get install -y curl git supervisor  
  
# Install npm  
RUN \  
curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get update && \  
apt-get install -y nodejs  
  
# Install mongodb from MongoDB official repository  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org  
  
# TaskQuest Installation  
RUN \  
git clone https://github.com/hashrock/taskquest.git && \  
cd taskquest && \  
npm install && \  
cp .env.example .env  
  
# Add supervisor config file  
ADD etc/supervisor/conf.d/taskquest.conf /etc/supervisor/conf.d/taskquest.conf  
  
# Clean up  
RUN \  
apt-get clean  
  
VOLUME ["/taskquest", "/var/lib/mongodb"]  
EXPOSE 4000  
ENTRYPOINT ["/usr/bin/supervisord", "-n"]  
  

