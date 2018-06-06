FROM debian:stretch-slim  
LABEL maintainer "sysadmin@kronostechnologies.com"  
  
ADD http://database.clamav.net/main.cvd /var/lib/clamav/main.cvd  
ADD http://database.clamav.net/daily.cvd /var/lib/clamav/daily.cvd  
ADD http://database.clamav.net/bytecode.cvd /var/lib/clamav/bytecode.cvd  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
clamav-daemon \  
clamav-freshclam && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
# Permission & clamd.conf setup  
RUN mkdir /run/clamav && chown clamav:clamav /run/clamav && chown -R
clamav:clamav /var/lib/clamav/  
COPY ./conf.d/clamd.conf /etc/clamav/clamd.conf  
COPY ./conf.d/freshclam.conf /etc/clamav/freshclam.conf  
  
# Install start/stop scripts  
COPY ./entrypoint /k  
  
# Install entrypoint  
ADD https://github.com/kronostechnologies/docker-init-
entrypoint/releases/download/1.2.0/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
EXPOSE 3310  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

