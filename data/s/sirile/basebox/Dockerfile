FROM progrium/busybox  
MAINTAINER Ilkka Anttonen version: 0.1  
RUN ln -s /opt/files/runsv /sbin/runsv  
RUN ln -s /opt/files/runsvdir /sbin/runsvdir  
RUN ln -s /opt/files/consul /usr/bin/consul  
COPY consul /etc/service/consul/run  
COPY config-consul.json /etc/consul.d/config-consul.json  
CMD "/sbin/runsvdir" "/etc/service"  

