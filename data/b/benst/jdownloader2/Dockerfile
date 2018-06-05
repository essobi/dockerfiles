FROM openjdk:8-jre  
  
LABEL maintainer "Benjamin Stein <info@diffus.org>"  
  
# the user jd2 will run with and his group  
ARG user=jd2  
ARG group=jd2  
ARG uid=1000  
ARG gid=1000  
# add specified user and group and create and chown the install and downloads
dir  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${gid} -m -s /bin/bash ${user} \  
&& mkdir -p /opt/JDownloader/ /opt/downloads \  
&& chown -R ${uid}:${group} /opt/JDownloader/ /opt/downloads  
  
# copy the start script to the Container  
COPY startJD2.sh /opt/JDownloader/  
# make it executable  
RUN chmod +x /opt/JDownloader/startJD2.sh  
  
# switch to the specified user  
USER ${user}  
  
# download the jdownloader jar file and run it to create the neccesary files
and folders  
RUN \  
wget -O /opt/JDownloader/JDownloader.jar --user-
agent="https://hub.docker.com/r/benst/headless-jd2-docker/"
\--progress=bar:force http://installer.jdownloader.org/JDownloader.jar && \  
java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar ;  
  
# Run this when the container is started  
CMD /opt/JDownloader/startJD2.sh  

