FROM openjdk:8-jre-alpine  
  
MAINTAINER DBpedia Spotlight Team <dbp-spotlight-
developers@lists.sourceforge.net>  
  
  
ENV RELEASE_SERVER downloads.dbpedia-spotlight.org  
ENV RELEASE_FILENAME dbpedia-spotlight-services-1.0.0.jar  
  
RUN apk add --no-cache curl && \  
mkdir -p /opt/spotlight/templates && \  
cd /opt/spotlight && \  
curl -O "https://$RELEASE_SERVER/spotlight/$RELEASE_FILENAME" && \  
curl -O "https://$RELEASE_SERVER/spotlight/services/application.yml" && \  
curl -O "https://$RELEASE_SERVER/spotlight/services/templates/nif-21.vm" && \  
cd /bin && \  
curl -O "https://$RELEASE_SERVER/spotlight/services/spotlight.sh" && \  
apk del curl  
  
RUN chmod +x /bin/spotlight.sh  
  
EXPOSE 8080  

