#  
# Dockerfile for libresonic  
#  
# https://github.com/tonipes/libresonic-docker  
#  
# https://github.com/Libresonic/libresonic  
#  
  
FROM tomcat:6.0  
  
MAINTAINER Telyn  
  
# Install libs for transcoding  
RUN apt-get update && \  
apt-get install \--yes \--force-yes \--no-install-recommends \--no-install-
suggests flac && \  
apt-get install \--yes \--force-yes \--no-install-recommends \--no-install-
suggests lame && \  
apt-get install \--yes \--force-yes \--no-install-recommends \--no-install-
suggests libav-tools  
  
# Download and setup libresonic  
RUN rm -rf /usr/local/tomcat/webapps && mkdir /usr/local/tomcat/webapps \  
&& wget https://libresonic.org/release/libresonic-v6.0.1.war -O
/usr/local/tomcat/webapps/ROOT.war \  
&& mkdir -p /var/subsonic/transcode \  
&& cd /var/subsonic/transcode \  
&& ln -s "$(which flac)" \  
&& ln -s "$(which lame)" \  
&& ln -s "$(which avconv)" ffmpeg  

