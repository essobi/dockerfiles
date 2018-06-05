FROM polinux/supervisor:alpine  
  
ENV GITBUCKET_VERSION="4.18.0" \  
HOSTNAME="0.0.0.0" \  
CONTEXTPATH="" \  
DATA_DIR="/data/gitbucket"  
RUN \  
apk add --update openjdk8 curl && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /opt/ && \  
curl -sL
https://github.com/gitbucket/gitbucket/releases/download/${GITBUCKET_VERSION}/gitbucket.war
-o /opt/gitbucket.war  
  
COPY container-files/ /  
  
EXPOSE 8080 29418  

