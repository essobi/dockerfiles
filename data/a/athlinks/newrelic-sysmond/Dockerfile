FROM athlinks/alpine:3.4  
ENV NEW_RELIC_LICENSE_KEY="12345678" \  
NEW_RELIC_HOSTNAME="localhost" \  
NEW_RELIC_LOG_LEVEL="info" \  
NEW_RELIC_LABELS="environment:local;application:eventops;dc:local;region:local;"
\  
NEW_RELIC_VERSION="2.3.0.132"  
ADD https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-${NEW_RELIC_VERSION}-linux.tar.gz /newrelic-sysmond.tar.gz  
RUN tar xvfz /newrelic-sysmond.tar.gz && \  
rm /newrelic-sysmond.tar.gz  
  
WORKDIR /newrelic-sysmond-${NEW_RELIC_VERSION}-linux  
RUN mv ./nrsysmond.cfg /etc/ && \  
mv ./scripts/nrsysmond-config /bin && \  
mv ./daemon/nrsysmond.x64 /bin/nrsysmond  
  
ADD bin/entrypoint.sh /bin/entrypoint.sh  
  
ADD conf/nrsysmond.cfg /tmp/nrsysmond.cfg  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  
CMD ["nrsysmond", "-c", "/etc/nrsysmond.cfg", "-f"]  

