FROM progrium/busybox  
MAINTAINER Ilkka Anttonen version: 0.1  
COPY consul_ui /opt/consul_ui  
COPY startConsul.sh /usr/bin/startConsul.sh  
RUN ln -s /opt/files/consul /usr/bin/consul  
CMD '/usr/bin/startConsul.sh'  

