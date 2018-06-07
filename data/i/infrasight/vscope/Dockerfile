FROM alpine:latest as downloader  
  
ADD https://dist.vscope.net/server/release/latest-linux64.gtk.zip /vscope.zip  
  
RUN unzip /vscope.zip -d /tmp  
  
RUN rm /tmp/vScopeServer/vScopeServer.ini  
  
RUN cp /tmp/vScopeServer/plugins/com.infrasight.bootstrap_*.jar
/tmp/vScopeServer/bootstrap.jar  
  
RUN sed -i 's|osgi.instance.area.*|osgi.instance.area=/data|g'
/tmp/vScopeServer/configuration/config.ini  
RUN sed -i
's|osgi.configuration.area.*|osgi.configuration.area=/data/configuration|g'
/tmp/vScopeServer/configuration/config.ini  
  
FROM openjdk:8-jre-alpine  
MAINTAINER Konrad Eriksson "konrad.eriksson@infrasightlabs.com"  
COPY \--from=downloader /tmp/ /  
  
# vScope Web UI port  
EXPOSE 80  
# vScope OSGi console  
EXPOSE 4444  
## Entrypoint  
ENTRYPOINT ["/usr/bin/java", "-cp", "/vScopeServer/bootstrap.jar",
"com.infrasight.bootstrap.Bootstrapper", "-install", "/vScopeServer"]  

