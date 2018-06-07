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
  
# DevHub Installation  
RUN \  
git clone https://github.com/volpe28v/DevHub.git && \  
cd DevHub && \  
npm install  
  
#-----  
# Install mongodb admin tools  
#-----  
#RUN \  
# apt-get install -y php-pear php5-dev php5-mongo php5-fpm nginx  
# Add supervisor config file  
ADD template/etc/supervisor/conf.d/devhub.conf
/etc/supervisor/conf.d/devhub.conf  
  
# Clean up  
RUN \  
apt-get clean  
  
VOLUME ["/DevHub", "/var/lib/mongodb"]  
EXPOSE 3000  
ENTRYPOINT ["/usr/bin/supervisord", "-n"]  
  

