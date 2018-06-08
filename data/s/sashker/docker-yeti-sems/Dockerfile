FROM debian:jessie  
  
MAINTAINER Alexander Mustafin <mustafin.aleksandr@gmail.com>  
  
#Grab keys for repo  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 9CEBFFC569A832B6  
  
#Add repo and install packets  
RUN echo 'deb http://pkg.yeti-switch.org/debian/jessie stable main ext' >>
/etc/apt/sources.list && \  
apt-get update && apt-get -y install sems sems-modules-yeti && rm -rf
/var/lib/apt/lists/*  
  
VOLUME ["/etc/sems/", "/var/log/sems"]  
  
COPY sems.conf /etc/sems/  
COPY yeti.conf /etc/sems/etc/  
RUN mv /etc/sems/etc/jsonrpc.conf.dist /etc/sems/etc/jsonrpc.conf  
  
#Set necessary variables for configs  
ENV INTERNAL_IP=eth0  
ENV SIP_PORT=5061  
ENV PUBLIC_IP=eth0  
ENV NODE_ID=1  
ENV MANAGEMENT_ADDR=127.0.0.1  
#Patch for creating necessary directories  
RUN mkdir -p /var/spool/sems/dump /var/spool/sems/record  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 5061 7080  
CMD ["sems"]  

