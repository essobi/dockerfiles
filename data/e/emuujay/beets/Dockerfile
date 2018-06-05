FROM ubuntu:xenial  
  
# Install some build dependencies  
RUN apt-get update \  
&& apt-get install -y python-dev \  
python-pip  
  
RUN pip install beets requests pylast  
  
# Copy in config file  
COPY config/ /config  
  
# Copy in the scripts to run  
COPY scripts/ /scripts  
  
# Mount in volumes  
VOLUME /import  
VOLUME /library  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]  

