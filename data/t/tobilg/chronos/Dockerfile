FROM java:openjdk-8-jre  
MAINTAINER tobilg <tobilg@gmail.com>  
  
# packages  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
echo "deb http://repos.mesosphere.io/debian jessie main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y --force-yes
mesos=0.28.0-2.0.16.debian81 chronos  
  
# Add bootstrapping script  
ADD bootstrap.sh /bootstrap.sh  
RUN chmod +x /bootstrap.sh  
  
# Expose standard port  
EXPOSE 8080  
ENTRYPOINT ["/bootstrap.sh"]  

