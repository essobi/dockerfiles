FROM greytip/storm:1.0.0.a  
  
MAINTAINER Sayeed Anjum  
  
#ADD start-supervisor.sh /usr/bin/start-supervisor.sh  
#ADD storm.yaml.tmpl $STORM_HOME/conf/storm.yaml.tmpl  
  
RUN /usr/bin/config-supervisord.sh nimbus  
RUN /usr/bin/config-supervisord.sh drpc  
RUN /usr/bin/config-supervisord.sh logviewer  
  
EXPOSE 6627  
EXPOSE 3772  
EXPOSE 3773  
  
CMD /usr/bin/start-supervisor.sh  

