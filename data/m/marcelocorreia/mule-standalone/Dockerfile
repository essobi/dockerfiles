FROM java:7  
MAINTAINER Marcelo Correia <marcelo.correia@starvisitor.com>  
WORKDIR /usr/local/  
RUN wget https://repository-
master.mulesoft.org/nexus/content/groups/public/org/mule/distributions/mule-
standalone/3.7.0/mule-standalone-3.7.0.tar.gz  
RUN tar -xvzf mule-standalone-3.7.0.tar.gz  
RUN useradd -g users -m -s /bin/bash yoda  
RUN chown -R yoda:users /usr/local/mule-standalone-3.7.0  
USER yoda  
WORKDIR /usr/local/  
ENV MULE_HOME=/usr/local/mule-standalone-3.7.0  
CMD $MULE_HOME/bin/mule $MULE_OPTS  

