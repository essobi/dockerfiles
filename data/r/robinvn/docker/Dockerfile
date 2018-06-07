FROM isuper/java-oracle:jdk_8  
MAINTAINER robin <robin.github@gmail.com>  
  
ENV PLAY_HOME /local/play/play-1.3.2  
ENV JRE_HOME /usr/lib/jvm/java-8-oracle  
# INSTALL TOMCAT  
  
RUN apt-get update && apt-get install -y telnet zip python dos2unix wget && \  
mkdir -p /local/java/play && \  
wget
https://github.com/playframework/play1/releases/download/1.3.2/play-1.3.2.zip
&& \  
unzip play-1.3.2 -d play-1.3.2 && \  
rm play-1.3.2.zip && \  
mv play-1.3.2 /local/play/ && \  
cd $PLAY_HOME && \  
dos2unix *  
  
ENV PATH $PATH:$PLAY_HOME/:$JRE_HOME  
  
  
# Remove unneeded apps  
  
  
  
# tomcat conf  
#ADD conf ${CATALINA_HOME}/conf  
#ADD tomcat_wrapper.sh /opt/tomcat/bin/  
#RUN ${CATALINA_HOME}/bin/catalina.sh run  
ENTRYPOINT cd /apps && play run  
EXPOSE 9000 8000  
  
  
  
  

