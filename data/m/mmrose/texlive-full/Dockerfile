FROM philcryer/min-jessie:latest  
MAINTAINER Martin Mrose <github@penthranet.de>  
  
# see recommendation https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices/#apt-get  
RUN apt-get update && apt-get install -y texlive-full \  
&& rm -rf /tmp/* /var/tmp/* \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
VOLUME ["/data"]  

