FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
curl --fail --location --silent --show-error -o /tmp/emailrelay.deb \  
http://sourceforge.net/projects/emailrelay/files/emailrelay/1.9/emailrelay_1.9_amd64.deb/download
&& \  
DEBIAN_FRONTEND=noninteractive \  
dpkg -i /tmp/emailrelay.deb && \  
rm -v /tmp/emailrelay.deb  
  
ENTRYPOINT [ "emailrelay", "--no-daemon", "--no-syslog", "--log-
file=/dev/stdout" ]  
CMD [ "--help", "--verbose" ]  

