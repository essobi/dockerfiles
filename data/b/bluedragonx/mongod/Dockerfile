FROM bluedragonx/baseimage:0.1  
MAINTAINER Ryan Bourgeois <bluedragonx@gmail.com>  
  
# set up the container environment  
EXPOSE 27017  
VOLUME /data  
ENTRYPOINT ["/sbin/my_init"]  
  
# install packages  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' > /etc/apt/sources.list.d/mongodb.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7F0CEB10 && \  
apt-get update -qy && \  
apt-get install -y mongodb-org-server=2.6.1 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# create dirs and add config files  
RUN mkdir -p /etc/service/mongod  
ADD files/run /etc/service/mongod/  

