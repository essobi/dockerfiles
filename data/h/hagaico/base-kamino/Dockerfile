FROM docker:dind  
  
# volumes for docker to run properly  
VOLUME ["/tmp/"]  
VOLUME ["/var/lib/docker/"]  
  
# Decleraing env vars  
#ENV KAMINO_INPUT_DIR  
ENV PUSER nobody  
ENV PUID 65534  
ENV PGID 65535  
# install python + Docker compose  
RUN set -e \  
&& apk add --no-cache \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install docker-compose  
  
# Setting my temp & workdir  
RUN mkdir -p /tmp/ && mkdir -p /kamino  
WORKDIR /kamino/  
  
# Copy needed files  
COPY * ./  
RUN chmod +x ./bootstrap.sh && chmod +x ./functions.sh && sync  
  
ENTRYPOINT ["/kamino/bootstrap.sh"]  
CMD []  

