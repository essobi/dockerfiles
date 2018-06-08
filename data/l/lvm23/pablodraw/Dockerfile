FROM debian:jessie  
MAINTAINER Mauro <mauro@sdf.org>  
  
RUN apt-get update \  
&& apt-get install -yq mono-complete wget unzip --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /asc \  
&& wget http://download.picoe.ca/pablodraw/3.2/PabloDraw-3.2.1.zip -O
/asc/PabloDraw.zip \  
&& cd /asc \  
&& unzip PabloDraw.zip  
  
ENTRYPOINT [ "mono", "/asc/PabloDraw.exe" ]  

