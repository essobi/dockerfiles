FROM learninglayers/java8jce  
  
MAINTAINER Dominik Renzel <renzel@dbis.rwth-aachen.de>  
  
WORKDIR /opt  
  
# Download & unpack las2peer service CI build from Jenkins  
RUN wget http://layers.dbis.rwth-aachen.de/jenkins/job/las2peer-Demo-
Service/lastSuccessfulBuild/artifact/*zip*/archive.zip \  
&& unzip archive.zip \  
&& rm archive.zip \  
&& mv archive las2peer-federation  
  
RUN wget http://www.java2s.com/Code/JarDownload/commons-jxpath/commons-
jxpath-1.1.jar.zip && unzip commons-jxpath-1.1.jar.zip  
RUN wget http://mirror.synyx.de/apache//commons/logging/binaries/commons-
logging-1.2-bin.zip && unzip commons-logging-1.2-bin.zip  
RUN wget http://www.java2s.com/Code/JarDownload/sbbi/sbbi-
upnplib-1.0.4.jar.zip && unzip sbbi-upnplib-1.0.4.jar.zip  
RUN ls -la *.zip  
RUN rm *.zip  
RUN mv *.jar las2peer-federation/lib  
RUN mv commons-logging-1.2/commons-logging-1.2.jar las2peer-federation/lib  
  
WORKDIR /opt/las2peer-federation  
  
COPY pastry.properties ./etc/pastry.properties  
  
# expose las2peer bootstrap port to host  
EXPOSE 9011/tcp  
EXPOSE 9011/udp  
  
# Start las2peer service and connect to bootstrap port  
# make start script executable  
RUN chmod +x ./bin/*.sh \  
# TODO: make two following lines obsolete by earlier removal of startup params
(in GitHub, Jenkins)  
# for some reason, Jenkins delivers las2peer start scripts in DOS format, so
d2u them...  
&& apt-get install dos2unix -yq && dos2unix ./bin/*.sh \  
# for some reason, Jenkins delivers start script with params "interactive",
"uploadStartupDirectory" so remove these...  
&& sed -i "s#interactive##g;s#uploadStartupDirectory##g"
./bin/connect_network.sh \  
&& sed -i "s#interactive##g;s#uploadStartupDirectory##g"
./bin/start_network.sh \  
&& sed -i "s#8080#8082#g"
./etc/i5.las2peer.webConnector.WebConnector.properties  
  
COPY run.sh run.sh  
  
CMD ["bash", "run.sh"]  
  

