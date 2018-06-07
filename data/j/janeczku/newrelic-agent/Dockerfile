FROM busybox:ubuntu-14.04  
MAINTAINER Jan Broer <janeczku@yahoo.com>  
LABEL Description="New Relic Server Agent" vendor="New Relic Inc."  
  
ENV NEW_RELIC_VERSION 2.2.0.125  
ADD https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-${NEW_RELIC_VERSION}-linux.tar.gz /tmp/newrelic-sysmond.tar.gz  
  
RUN tar xvfz /tmp/newrelic-sysmond.tar.gz -C /tmp && \  
rm /tmp/newrelic-sysmond.tar.gz && \  
mv /tmp/newrelic-sysmond-*-linux/daemon/nrsysmond.x64 /bin/nrsysmond && \  
rm -rf /tmp/*  
  
CMD ["/bin/nrsysmond","-E","-F","-l","/dev/stdout"]  

