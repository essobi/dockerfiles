## Version 1.0.4  
FROM fortytwoio/debian:latest  
MAINTAINER Thomas Fritz <thomas.fritz@forty-two.io>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqy > /dev/null 2>&1  
# You do not have to do this in your Dockerfiles anymore :). Just convenience  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqy > /dev/null
2>&1  
  
# Common used and rarely changing package dependencies. locales package will
also dpkg-reconfigure locales.  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qqy --no-install-
recommends \  
socat \  
supervisor \  
unzip \  
> /dev/null 2>&1  
  
# We want to add the local ./bin dir to /usr/local/bin in Docker container /
images extending from this image.  
ONBUILD ADD ./bin/ /usr/local/bin/  
ONBUILD ADD ./etc/supervisor-conf.d/ /etc/supervisor/conf.d/  
  
# Ports used by Serf for node discovery and cluster managment  
EXPOSE 7373 7946  
VOLUME ["/var/log"]  
  
CMD ["/usr/bin/env", "init.sh"]  
  
# Downloading, unpacking and moving in $PATH of serf binary  
ADD https://dl.bintray.com/mitchellh/serf/0.6.3_linux_amd64.zip /tmp/serf.zip  
RUN cd /tmp && \  
unzip /tmp/serf.zip && \  
mv /tmp/serf /usr/local/bin  
  
# We add the local ./bin dir to /usr/local/bin.  
ADD ./bin/ /usr/local/bin/  
ADD ./etc/supervisor-conf.d/ /etc/supervisor/conf.d/  
  
RUN rm -rf /tmp/* && \  
rm -rf /var/tmp/*  

