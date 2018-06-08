FROM debian:wheezy  
  
ENV NEW_RELIC_SYSMOND_VERSION 2.0.3.113  
# apt-get update  
RUN apt-get update -q && \  
apt-get install -y ca-certificates curl && \  
echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list && \  
curl -L https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
apt-get update -q && \  
apt-get install -y newrelic-sysmond=$NEW_RELIC_SYSMOND_VERSION && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD newrelic/nrsysmond.cfg /etc/newrelic/nrsysmond.cfg  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
VOLUME ["/etc/newrelic/"]  
  
CMD ["nrsysmond", "-c", "/etc/newrelic/nrsysmond.cfg", "-f"]

