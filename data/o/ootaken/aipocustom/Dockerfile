FROM ootaken/aipobase:latest  
MAINTAINER Kenichiro Ota <oota_ken@hotmail.com>  
  
ENV AIPO_REPO https://github.com/aipocom/aipo.git  
ENV AIPO_OPENSOCIAL_REPO https://github.com/aipocom/aipo-opensocial.git  
ENV BRANCH installer:stable  
  
USER root  
  
ADD build.sh .  
ENTRYPOINT ./build.sh && /bin/bash  

