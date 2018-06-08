FROM debian:buster-slim  
MAINTAINER sysadmin@kronostechnologies.com  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gearman-tools \  
gearman-job-server \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
RUN mkdir -p /opt/gearman && \  
chown gearman /opt/gearman  
  
WORKDIR /opt/gearman  
COPY ./bin /opt/gearman/bin  
RUN chmod +x /opt/gearman/bin/*  
  
EXPOSE 4730  
ENTRYPOINT ["/opt/gearman/bin/entrypoint.sh"]  

