FROM jsurf/rpi-raspbian:latest  
  
RUN [ "cross-build-start" ]  
  
ENV LANG C.UTF-8  
ENV TZ Europe/Paris  
  
RUN apt-get update \  
&& apt-get install -y wget oracle-java8-jdk \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s jdk-8-oracle-arm32-vfp-hflt /usr/lib/jvm/java-8-oracle  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN java -version  
  
# add specified user and group and create and chown the install and downloads
dir  
RUN mkdir -p /opt/JDownloader/ /opt/downloads  
# download the jdownloader jar file and run it to create the neccesary files
and folders  
RUN \  
wget -O /opt/JDownloader/JDownloader.jar --progress=bar:force
http://installer.jdownloader.org/JDownloader.jar  
  
# copy the start script to the Container  
COPY startJD2.sh /opt/JDownloader/  
# make it executable  
RUN chmod +x /opt/JDownloader/startJD2.sh  
  
# Run this when the container is started  
CMD /opt/JDownloader/startJD2.sh  
  
RUN [ "cross-build-end" ]

