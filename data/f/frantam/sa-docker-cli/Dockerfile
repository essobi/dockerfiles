FROM jenkinsci/slave  
  
USER root  
RUN apt-get update && apt-get install -y --no-install-recommends \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
# https://github.com/KostyaSha/yet-another-docker-plugin/issues/217  
RUN echo "export LANG=C.UTF-8" >> /etc/environment  
  
USER jenkins  

