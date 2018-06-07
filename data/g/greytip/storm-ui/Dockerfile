FROM greytip/storm:1.0.0.a  
  
MAINTAINER Sayeed Anjum  
  
RUN /usr/bin/config-supervisord.sh ui  
RUN /usr/bin/config-supervisord.sh logviewer  
  
EXPOSE 8080 48000  
CMD /usr/bin/start-supervisor.sh  
  

