FROM debian:stretch-slim  
MAINTAINER sysadmin@kronostechnologies.com  
  
# Install  
RUN apt-get update && apt-get install -y --no-install-recommends \  
spamassassin \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
# Install entrypoint  
ADD https://github.com/kronostechnologies/docker-init-
entrypoint/releases/download/1.2.0/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Install start/stop scripts  
COPY ./docker/k /k  
COPY ./docker/etc /etc  
  
# Expose service port  
EXPOSE 783  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

