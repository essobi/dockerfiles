# Use the same base image as tekhedd/ameinias to reduce footprint,  
# even though we really don't need java.  
FROM java:8  
MAINTAINER tekHedd <tekhedd@byteheaven.net>  
  
COPY am-ices2.sh /  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y ices2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& chmod a+rx /am-ices2.sh  
  
VOLUME [ "/adata" ]  
  
# uses config file /adata/ices2.xml and /adata/audio-fifo  
CMD [ "/am-ices2.sh" ]  
  
# docker run [...] --link icecast2:icecastserver --volumes-from ameinias
tekhedd/ameinias-ices2  

