FROM kibana:4.6.1  
MAINTAINER Thomas Zoratto <thomas.zoratto@gmail.com>  
  
# install shield plugin  
RUN /opt/kibana/bin/kibana plugin --install kibana/shield  
# owner of /opt/kibana/** is incorrect after plugin installation  
RUN chown -R kibana:kibana /opt/kibana  

