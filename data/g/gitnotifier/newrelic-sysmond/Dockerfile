FROM debian:jessie  
MAINTAINER Andrea Usuelli (andreausu@gmail.com)  
  
ENV NEW_RELIC_LICENSE_KEY=YOUR_LICENSE_KEY \  
CUSTOM_HOSTNAME=CUSTOM_HOSTNAME \  
LOG_LEVEL=info \  
NEW_RELIC_VERSION=2.2.0.125  
ADD https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-${NEW_RELIC_VERSION}-linux.tar.gz /opt/newrelic-sysmond.tar.gz  
RUN cd /opt && tar xvfz newrelic-sysmond.tar.gz && \  
rm newrelic-sysmond.tar.gz && \  
cd newrelic-sysmond-${NEW_RELIC_VERSION}-linux && \  
mv nrsysmond.cfg /etc/ && \  
mv scripts/nrsysmond-config /bin && \  
mv daemon/nrsysmond.x64 /bin/nrsysmond  
  
CMD /bin/nrsysmond-config --set license_key=$NEW_RELIC_LICENSE_KEY && \  
/bin/nrsysmond -c /etc/nrsysmond.cfg -n $CUSTOM_HOSTNAME -d $LOG_LEVEL -l
/dev/stdout -F  

