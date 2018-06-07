FROM debian:latest  
MAINTAINER Daniel Atkinson <hourd.tasa@gmail.com>  
RUN apt-get update \  
&& \  
apt-get install -y doxygen graphviz \  
&& \  
rm -rf /var/lib/apt/lists/* \  
&& \  
mkdir -p /src  
WORKDIR /src  
VOLUME /src  
CMD ["doxygen", "Doxyfile"]  

