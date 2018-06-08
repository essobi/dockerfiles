### Dockerfile for Splunk  
FROM debian:jessie  
RUN apt-get update -q && apt-get install -y \  
wget  
  
MAINTAINER Nick Perry <nwperry@gmail.com>  
  
# Download the Splunk installer, install Splunk, then remove the installer.  
RUN wget -O /splunk-6.2.3-264376-linux-2.6-amd64.deb
"http://www.splunk.com/page/download_track?file=6.2.3/splunk/linux/splunk-6.2.3-264376-linux-2.6-amd64.deb&ac=test_modal_enterprise&wget=true&name=wget&platform=Linux&architecture=x86_64&version=6.2.3&product=splunk&typed=release"
&& \  
dpkg -i /splunk-6.2.3-264376-linux-2.6-amd64.deb && \  
rm /splunk-6.2.3-264376-linux-2.6-amd64.deb  
  
# Configure Splunk to run as splunk user.  
RUN sed -i 's/# SPLUNK_OS_USER/SPLUNK_OS_USER=splunk/' /opt/splunk/etc/splunk-
launch.conf && mkdir -p /opt/splunk/var /data /license && chown -R
splunk:splunk /opt/splunk /data /license  
  
# Create a basic local/web.conf to enable HTTPS for the Splunk web interface.  
RUN echo '[settings]\nenableSplunkWebSSL = true\nprivKeyPath =
etc/auth/splunkweb/privkey.pem\ncaCertPath = etc/auth/splunkweb/cert.pem' >>
/opt/splunk/etc/system/local/web.conf && \  
chown splunk:splunk /opt/splunk/etc/system/local/web.conf  
  
# Add a script for Splunk process lifecycle management in Docker.  
RUN echo '#!/bin/bash\nset -e\n/opt/splunk/bin/splunk start --accept-license
--no-prompt --answer-yes\ntrap "echo SIGTERM && /opt/splunk/bin/splunk stop &&
exit" SIGTERM\ntail -f /dev/null &\nwait $!' > /bin/splunk.sh && chmod 755
/bin/splunk.sh  
  
CMD ["/bin/splunk.sh"]  
  
ENV SPLUNK_HOME /opt/splunk  
  
EXPOSE 8000 8089 9997 5514  
VOLUME ["/data"]  
VOLUME ["/license"]  
VOLUME ["/opt/splunk/var"]  
  
### END  
### For persistence, map /opt/splunk/var to a directory on the host or
separate  
### data container.  
###  

