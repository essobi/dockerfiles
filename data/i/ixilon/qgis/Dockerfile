FROM ubuntu:16.04  
MAINTAINER Gerald Fiedler <gerald@ixilon.de>  
  
RUN echo "deb http://qgis.org/debian xenial main" >> /etc/apt/sources.list  
RUN gpg --keyserver keyserver.ubuntu.com --recv 073D307A618E5811  
RUN gpg --export \--armor 073D307A618E5811 | apt-key add -  
  
RUN apt-get update && \  
apt-get install -y qgis python-qgis qgis-plugin-grass && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD qgis  

