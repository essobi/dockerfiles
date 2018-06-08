FROM docker:stable-git  
  
ENV PATH=/usr/local/src/.ci/bin:/usr/local/src/bin:${PATH}  
  
RUN set -exu && \  
apk add --update bash ca-certificates curl git make py-pip tar jq && \  
pip install docker-compose && \  
rm -rf ~/* /var/cache/* && \  
mkdir -p /var/cache/docker/ /usr/local/src/  
  
WORKDIR /usr/local/src  

