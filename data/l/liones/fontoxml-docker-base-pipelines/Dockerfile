FROM liones/fontoxml-docker-base:latest  
MAINTAINER Erik van der Valk <erik.van.der.valk@fontoxml.com>  
MAINTAINER Martin Middel <martin.middel@fontoxml.com>  
MAINTAINER Stef Busking <stef.busking@fontoxml.com>  
  
# Install chromium, firefox and virtual frame buffer  
RUN apt-get update && apt-get install -y \  
chromium-browser \  
firefox \  
xvfb  
  
# Install nodejs 6.x LTS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  

