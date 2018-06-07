FROM ubuntu:16.04  
LABEL maintainer "Darren Green <darren@gruen.site>"  
  
CMD ["/usr/local/bin/haxor-news"]  
  
RUN apt-get update && \  
apt-get install -y \  
python-pip \  
less && \  
pip install haxor-news \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  

