FROM debian  
MAINTAINER Ryan Grieve <me@ryangrieve.com>  
  
# no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# update apt cache, upgrade the system and install the system utils we need  
RUN apt-get update --fix-missing && apt-get upgrade -y  
RUN apt-get install -y make wget python python-pip build-essential
openjdk-7-jre  
  
# install sphinx  
RUN pip install Sphinx sphinx-rtd-theme sphinxcontrib-httpdomain  
RUN wget http://garr.dl.sourceforge.net/project/plantuml/plantuml.jar -O
/opt/plantuml.jar  
  
ENV PLANTUML_JAR /opt/plantuml.jar  
  
CMD bash  

