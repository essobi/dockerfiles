FROM java:8  
MAINTAINER linshare <linshare@linagora.com>  
  
EXPOSE 8080  
EXPOSE 8081  
ARG VERSION="2.0.2"  
ARG CHANNEL="releases"  
ARG EXT="com"  
WORKDIR /usr/local/sbin/  
RUN mkdir -p /etc/linshare-thumbnail-server  
COPY config.yml /etc/linshare-thumbnail-server/  
  
RUN apt-get update && apt-get install -y libreoffice  
  
RUN
URL="https://nexus.linagora.${EXT}/service/local/artifact/maven/content?r=linshare-${CHANNEL}&g=org.linagora.linshare&a=thumbnail-
server&v=${VERSION}"; \  
wget --no-check-certificate --progress=bar:force:noscroll \  
-O linshare-thumbnail-server.jar "${URL}&p=jar" && \  
wget --no-check-certificate --progress=bar:force:noscroll \  
-O linshare-thumbnail-server.jar.sha1 "${URL}&p=jar.sha1" && \  
sed -i 's#^\\(.*\\)#\1\tlinshare-thumbnail-server.jar#' linshare-thumbnail-
server.jar.sha1 && \  
sha1sum -c linshare-thumbnail-server.jar.sha1 --quiet && rm -f linshare-
thumbnail-server.jar.sha1  
  
ENTRYPOINT ["java", "-jar", "/usr/local/sbin/linshare-thumbnail-server.jar",
"server", "/etc/linshare-thumbnail-server/config.yml"]  

