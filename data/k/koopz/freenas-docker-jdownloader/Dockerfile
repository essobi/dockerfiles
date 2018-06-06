FROM openjdk:8-jre  
  
MAINTAINER Koopzington <koopzington@gmail.com>  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version="2" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="false" \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/opt/JDownloader/cfg\", \  
\"descr\": \"Configuration files directory\" \  
}, \  
{ \  
\"name\": \"/opt/JDownloader/Downloads\", \  
\"descr\": \"Downloads Folder\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"JDOWNLOADER_GID\", \  
\"descr\": \"PGID assigned upon creation\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"JDOWNLOADER_UID\", \  
\"descr\": \"PUID assigned upon creation\", \  
\"optional\": true \  
} \  
]"  
  
# Install fontconfig and download phantomjs  
RUN apt-get update && \  
apt-get install -y --no-install-recommends fontconfig && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
wget -O /tmp/phantomjs.tar.bz2 --progress=bar:force
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
cd /tmp/ && \  
tar xvfj phantomjs.tar.bz2 && \  
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \  
rm -rf /tmp/phantomjs*  
  
# Create user and group for JDownloader.  
RUN groupadd -r -g 666 jdownloader && \  
useradd -r -u 666 -g 666 jdownloader  
  
# Create directory, download and start JD2 for the initial update and creation
of config files.  
RUN mkdir -p /opt/JDownloader/ && \  
wget -O /opt/JDownloader/JDownloader.jar --user-
agent="https://hub.docker.com/r/koopz/freenas-docker-jdownloader/"
--progress=bar:force http://installer.jdownloader.org/JDownloader.jar && \  
java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar  
  
COPY startJD2.sh /opt/JDownloader/  
RUN chmod +x /opt/JDownloader/startJD2.sh  
  
WORKDIR /opt/JDownloader  
  
# Run this when the container is started  
CMD startJD2.sh  

