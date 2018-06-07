FROM luismesalas/storm:1.0.1  
MAINTAINER luismesalas  
  
RUN /usr/bin/config-supervisord.sh supervisor  
RUN /usr/bin/config-supervisord.sh logviewer  
  
EXPOSE 6700  
EXPOSE 6701  
EXPOSE 6702  
EXPOSE 6703  
EXPOSE 8000  
CMD /usr/bin/start-supervisor.sh  

