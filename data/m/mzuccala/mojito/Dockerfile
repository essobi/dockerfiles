FROM java:8-jre  
LABEL maintainer="michele@zuccala.com"  
  
ENV MOJITO_VERSION 0.83  
RUN apt-get update && \  
apt-get install -y curl gettext-base  
  
RUN mkdir -p /opt/mojito && \  
curl -L
https://github.com/box/mojito/releases/download/v${MOJITO_VERSION}/mojito-
cli-${MOJITO_VERSION}.jar > /opt/mojito/cli.jar && \  
curl -L
https://github.com/box/mojito/releases/download/v${MOJITO_VERSION}/mojito-
webapp-${MOJITO_VERSION}.jar > /opt/mojito/webapp.jar  
  
COPY application.properties.dist /opt/mojito/  
COPY mojito-webapp-launcher.sh /opt/  
  
EXPOSE 8080  
CMD ["/opt/mojito-webapp-launcher.sh"]  

