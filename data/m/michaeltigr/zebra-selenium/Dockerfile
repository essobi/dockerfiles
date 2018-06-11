FROM selenium/standalone-firefox:latest  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# Install procps.  
RUN apt-get update \  
&& apt-get -y install wget curl procps \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entry_point.sh /opt/bin/entry_point.sh  
RUN chmod +x /opt/bin/entry_point.sh  

