FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Copy scripts  
COPY provision_homestead.sh provision_system.sh serve.sh run.sh /  
  
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
  
RUN chmod +x /*.sh \  
&& ./provision_system.sh \  
&& ./provision_homestead.sh \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
EXPOSE 80 443 22 35729 9876  
CMD ["/run.sh"]  

