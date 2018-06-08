FROM alpine:3.4  
ENV NEW_RELIC_LICENSE_KEY YOUR_LICENSE_KEY  
ENV NEW_RELIC_SYSMOND_VERSION 2.3.0.132  
ENV GLIBC_VERSION 2.23-r3  
  
RUN apk add --update ca-certificates wget && \  
wget -q "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \  
apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk && \  
wget https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-${NEW_RELIC_SYSMOND_VERSION}-linux.tar.gz && \  
tar xvzf newrelic-sysmond-${NEW_RELIC_SYSMOND_VERSION}-linux.tar.gz && \  
cp newrelic-sysmond-${NEW_RELIC_SYSMOND_VERSION}-linux/daemon/nrsysmond.x64
/usr/sbin/nrsysmond && \  
chmod 755 /usr/sbin/nrsysmond && \  
cp newrelic-sysmond-${NEW_RELIC_SYSMOND_VERSION}-linux/scripts/nrsysmond-
config /usr/sbin/ && \  
chmod 755 /usr/sbin/nrsysmond-config && \  
mkdir /etc/newrelic && \  
cp newrelic-sysmond-${NEW_RELIC_SYSMOND_VERSION}-linux/nrsysmond.cfg
/etc/newrelic/nrsysmond.cfg && \  
mkdir -p /usr/local/bin  
  
COPY entry.sh /usr/local/bin/entry.sh  
  
ENTRYPOINT ["/usr/local/bin/entry.sh"]  
  
CMD ["nrsysmond", "-c", "/etc/newrelic/nrsysmond.cfg", "-l", "/dev/stdout",
"-f"]  

