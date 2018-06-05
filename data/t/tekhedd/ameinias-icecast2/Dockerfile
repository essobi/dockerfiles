  
# Share root with ameinias  
From java:8  
MAINTAINER tekHedd <tekhedd@byteheaven.net>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /adata  
EXPOSE 8000  
USER icecast2  
  
# Expects to find its config file and log dirs in the  
# /adata volume, imported from the ameinias container  
CMD [ "/usr/bin/icecast2", "-c", "/adata/icecast.xml" ]  

