FROM tomcat:slim  
LABEL MAINTAINER karrth <karrth@gmail.com>  
  
LABEL version="1.2"  
LABEL description="Subsonic Media server"  
  
# packages we need  
RUN apt-get update  
RUN apt-get -y install libav-tools lame curl  
  
# transcode  
RUN mkdir -p /opt/data/transcode  
RUN ln -s /usr/bin/lame /opt/data/transcode/lame  
RUN ln -s /usr/bin/avconv /opt/data/transcode/ffmpeg  
  
# setup tomcat  
RUN rm -rf ${CATALINA_HOME}/webapps/ROOT  
RUN curl -skL $(curl -skL https://sourceforge.net/projects/subsonic/rss |
egrep -oah -m 1
"https:\/\/sourceforge\\.net\/projects\/subsonic\/files\/subsonic\/[0-9]+\\.[0-9]+\\.[0-9]+\/subsonic-[0-9]+\\.[0-9]+\\.[0-9]+-war\\.zip\/download")
-o /tmp/subsonic.war.zip  
RUN unzip /tmp/subsonic.war.zip  
RUN mv subsonic.war ${CATALINA_HOME}/webapps/ROOT.war  
RUN rm /tmp/subsonic.war.zip  
  
# configure subsonic  
ENV JAVA_OPTS="-Dsubsonic.contextPath=/ -Dsubsonic.home=/opt/data"  
# store our settings on a volume  
VOLUME /opt/data  
  
# show our interface  
EXPOSE 8080  

