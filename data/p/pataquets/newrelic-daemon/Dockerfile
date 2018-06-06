FROM pataquets/ubuntu:trusty  
  
RUN \  
DEBIAN_FRONTEND=noninteractive \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
548C16BF && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >>
/etc/apt/sources.list.d/newrelic.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y newrelic-daemon && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "newrelic-daemon", "-f", "--logfile", "/dev/stdout" ]  

