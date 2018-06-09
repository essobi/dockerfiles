FROM ubuntu:14.04  
MAINTAINER Unvired <support@unvired.io>  
  
RUN apt-get update -y && apt-get install -y \--no-install-recommends \  
ca-certificates \  
curl \  
wget \  
zip \  
unzip \  
supervisor \  
redis-server \  
openjdk-7-jre-headless \  
&& rm -rf /opt/lib/apt/lists/*  
  
LABEL vendor="Unvired Inc." \  
com.unvired.ump.module="TRIAL-PLATFORM" \  
com.unvired.ump.release="R-3.002.0040" \  
com.unvired.ump.release-date="21-Dec-2015"  
# Directories for work and passing input at runtime  
RUN mkdir -p /opt/unvired/temp \  
&& mkdir -p /var/UMPinput  
  
RUN wget -q -O/opt/unvired/temp/UMP3_Docker.zip
https://owncloud.unvired.com/index.php/s/p7qECutefEvRu9S/download  
  
RUN unzip -qq /opt/unvired/temp/UMP3_Docker.zip -d /opt/unvired/UMP3 \  
&& rm -f /opt/unvired/temp/UMP3_Docker.zip \  
&& chmod +x /opt/unvired/UMP3/bin/standalone.sh  
  
# Get the runtime deployment / dependencies for UMP  
RUN wget -q -O/opt/unvired/UMP3/standalone/deployments/UMP.ear
https://owncloud.unvired.com/index.php/s/MozjB5OOVIeAwer/download  
RUN wget -q -O/opt/unvired/UMP3/modules/unvired/middleware/main/UMP_Core.jar
https://owncloud.unvired.com/index.php/s/dUfxnaqXKt4Piz2/download  
RUN wget -q -O/opt/unvired/UMP3/modules/unvired/middleware/main/UMP_Logger.jar
https://owncloud.unvired.com/index.php/s/MyqJVSMKiOFfOVo/download  
RUN wget -q
-O/opt/unvired/UMP3/modules/unvired/middleware/main/UMP_odata_sdk.jar
https://owncloud.unvired.com/index.php/s/9kdLWxvOZZ5uorr/download  
RUN wget -q
-O/opt/unvired/UMP3/modules/unvired/middleware/main/UMP_sapjco_sdk.jar
https://owncloud.unvired.com/index.php/s/KKUTuLDZxkE4OIT/download  
RUN wget -q
-O/opt/unvired/UMP3/modules/unvired/middleware/main/UMP_jdbc_sdk.jar
https://owncloud.unvired.com/index.php/s/0EztBmYLs6PRBrt/download  
  
# Config for trial  
COPY config/hazelcast.xml
/opt/unvired/UMP3/standalone/configuration/hazelcast.xml  
COPY config/standalone-full.xml
/opt/unvired/UMP3/standalone/configuration/standalone-full.xml  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config/sentinel.conf /etc/sentinel.conf  
  
ENV JBOSS_HOME=/opt/unvired/UMP3  
ENV DOCKER_UMP_VERSION=R-3.002.0040  
  
# Main port and Management console  
EXPOSE 8080 9990  
  
# Any files like SAP connection binaries can be passed in via this volume, the
startup script will copy from here to start  
VOLUME /var/UMPinput  
  
ENTRYPOINT ["supervisord"]

