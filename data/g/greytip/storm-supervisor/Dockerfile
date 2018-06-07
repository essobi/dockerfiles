FROM greytip/storm:1.0.0.a  
  
MAINTAINER Sayeed Anjum  
  
EXPOSE 6700  
EXPOSE 6701  
EXPOSE 6702  
EXPOSE 6703  
EXPOSE 48000  
ADD storm.yaml.tmpl $STORM_HOME/conf/storm.yaml.tmpl  
ADD worker.xml.tmpl $STORM_HOME/log4j2/worker.xml.tmpl  
ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
  
RUN chmod +x /usr/bin/start-supervisor.sh  
  
RUN /usr/bin/config-supervisord.sh supervisor  
RUN /usr/bin/config-supervisord.sh logviewer  
  
CMD /usr/bin/start-supervisor.sh  
  

