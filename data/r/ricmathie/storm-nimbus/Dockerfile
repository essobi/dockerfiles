FROM ricmathie/storm:1.0.5  
MAINTAINER ricmathie  
  
EXPOSE 6627  
EXPOSE 3772  
EXPOSE 3773  
EXPOSE 8000  
RUN /usr/bin/config-supervisord.sh nimbus  
RUN /usr/bin/config-supervisord.sh logviewer  
RUN /usr/bin/config-supervisord.sh drpc  
  
#ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
CMD /usr/bin/start-supervisor.sh  

