FROM searchspring/sumologic:latest  
  
ENV \  
DOCKERIZE_VER=v0.5.0 \  
SUMO_SOURCE_NAME=sumo-docker-collector \  
SUMO_CATEGORY=docker \  
SUMO_ALL_CONTAINERS=false \  
SUMO_COLLECT_EVENTS=false \  
SUMO_MULTILINE_PROCESSING_ENABLED=false \  
SUMO_SOURCE_TYPE=DockerLog  
# Install Dockerize  
RUN \  
apt-get update \--quiet && \  
apt-get install \--quiet \--force-yes -y wget tar gzip && \  
apt-get clean \--quiet && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
cd /tmp && \  
wget -q
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VER}/dockerize-
linux-amd64-${DOCKERIZE_VER}.tar.gz && \  
tar -C /usr/local/bin -xzf /tmp/dockerize-linux-amd64-${DOCKERIZE_VER}.tar.gz
&& \  
rm /tmp/dockerize-linux-amd64-${DOCKERIZE_VER}.tar.gz && \  
mkdir /templates  
ADD sumo-sources.json.tmpl /template/sumo-sources.json.tmpl  
ADD start /start  
ENTRYPOINT [ "./start", "dockerize", "-template=/template/sumo-
sources.json.tmpl:/etc/sumo-sources.json",
"-stdout=/opt/SumoCollector/logs/collector.log", "/bin/bash", "run.sh" ]  

