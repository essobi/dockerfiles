FROM texastribune/base  
MAINTAINER tech@texastribune.org  
  
RUN apt-get install -yq supervisor  
  
RUN mkdir -p /app/logs  
  
ONBUILD ENTRYPOINT ["/usr/bin/supervisord", "-n"]  
ONBUILD CMD []  

