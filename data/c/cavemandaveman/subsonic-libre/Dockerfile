FROM alpine:3.3  
  
MAINTAINER cavemandaveman <cavemandaveman@openmailbox.org>  
  
ENV TOMCAT_VERSION="8.0.32" \  
TOMCAT_URL="http://apache.arvixe.com/tomcat/tomcat-8/v8.0.32/bin/apache-
tomcat-8.0.32.tar.gz" \  
SUBSONIC_URL="https://github.com/EugeneKay/subsonic/releases/download/v5.3-kang/subsonic-v5.3-kang.war"  
# Update repo and install java, transcoders  
RUN apk --update add \  
openjdk8-jre-base \  
ffmpeg \  
lame \  
flac  
  
# Create necessary folders  
RUN mkdir -p "/var/subsonic/transcode" \  
"/var/music" \  
"/opt"  
# Add symlinks for subsonic to use transcoders  
RUN for transcoder in ffmpeg flac lame; \  
do ln -s "$(which $transcoder)" "/var/subsonic/transcode/$transcoder"; \  
done  
  
# Download and untar tomcat, rename folder, and remove default tomcat page  
RUN wget -qO - $TOMCAT_URL \  
| tar -xzC "/opt/" \  
&& mv "/opt/apache-tomcat-$TOMCAT_VERSION" "/opt/apache-tomcat" \  
&& rm -rf "/opt/apache-tomcat/webapps/ROOT/"  
# Download and move subsonic into tomcat folder as main app  
RUN wget -qO "/opt/apache-tomcat/webapps/ROOT.war" $SUBSONIC_URL  
# Create tomcat system user/group and change ownership of necessary files and
folders  
# in order to avoid subsonic root user warning  
RUN addgroup -g 666 -S tomcat \  
&& adduser -u 666 -SHG tomcat tomcat \  
&& chown -R tomcat:tomcat \  
"/opt/apache-tomcat" \  
"/var/subsonic" \  
"/var/music"  
# Use the new tomcat user  
USER tomcat  
  
# Start the tomcat server  
CMD ["/opt/apache-tomcat/bin/catalina.sh", "run"]  

