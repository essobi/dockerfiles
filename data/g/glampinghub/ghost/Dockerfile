FROM ghost:1.21  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -qy build-essential python && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

