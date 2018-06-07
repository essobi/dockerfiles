FROM tianon/latex:latest  
LABEL version="1.0"  
LABEL maintainer="Mcdostone"  
  
WORKDIR /root  
  
RUN apt-get update && \  
apt-get install -y inkscape python-pygments  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get --purge remove -y .\\*-doc$

