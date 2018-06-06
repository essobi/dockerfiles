# Docker Definition for ElasticSearch Curator  
# Taken from https://github.com/elastic/curator/blob/master/Dockerfile  
FROM python:2.7.8-slim  
MAINTAINER Christian R. Vozar <christian@rogueethic.com>  
  
ENV CURATOR_VERSION 4.0  
ENV CURATOR_UID 555  
ENV CURATOR_GID 555  
RUN pip install --quiet elasticsearch-curator==${CURATOR_VERSION} && \  
groupadd -r -g ${CURATOR_GID} curator && \  
useradd -r -g curator -u ${CURATOR_UID} curator && \  
mkdir -p /etc/curator  
  
ENTRYPOINT [ "/usr/local/bin/curator", "--config", "/etc/curator/curator.yml"
]  

