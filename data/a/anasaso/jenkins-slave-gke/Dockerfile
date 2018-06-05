FROM jenkinsci/jnlp-slave:3.7-1-alpine  
  
MAINTAINER Anas ASO <aso.anas@protonmail.com>  
  
USER root  
  
# Docker group on GKE nodes always has the ID 450.  
RUN addgroup -g 450 docker && \  
adduser jenkins docker  
  
# Add needed SSL packages  
apk add wget ca-certificates  
  
USER jenkins  

