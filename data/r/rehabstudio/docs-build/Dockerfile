FROM debian:wheezy  
MAINTAINER Ryan Grieve <me@ryangrieve.com>  
  
# install apt dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
graphviz \  
inotify-tools \  
openjdk-7-jre \  
python \  
python-pip \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install sphinx  
RUN pip install \  
sphinx \  
sphinx-rtd-theme \  
sphinxcontrib-images \  
sphinxcontrib-httpdomain  
  
# install plantuml  
RUN wget http://garr.dl.sourceforge.net/project/plantuml/plantuml.jar \  
-O /opt/plantuml.jar  
  
ENV PLANTUML_JAR /opt/plantuml.jar  
  
CMD bash  

