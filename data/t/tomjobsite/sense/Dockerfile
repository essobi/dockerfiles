FROM kibana:4.6.3  
MAINTAINER Tom Constantine <tom.constantine@jobsite.co.uk>  
  
COPY kibana.yml /opt/kibana/config/kibana.yml  
  
RUN /opt/kibana/bin/kibana plugin --install elastic/sense  

