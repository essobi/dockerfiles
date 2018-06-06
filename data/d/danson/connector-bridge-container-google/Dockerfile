FROM ubuntu:16.04  
MAINTAINER ARM <doug.anson@arm.com>  
EXPOSE 22/tcp  
EXPOSE 8234/tcp  
EXPOSE 28520/tcp  
RUN apt-get update  
RUN apt-get -y install default-jre vim locales openssh-server supervisor
dnsutils unzip zip ntp  
RUN useradd arm -m -s /bin/bash  
RUN mkdir -p /home/arm  
RUN chown arm.arm /home/arm  
COPY ssh-keys.tar /home/arm/  
COPY properties-editor.zip /home/arm/  
COPY connector-bridge.zip /home/arm/  
COPY restart.sh /home/arm/  
COPY configure_instance.sh /home/arm/  
COPY start_instance.sh /home/arm/  
COPY update_hosts.sh /home/arm/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN chmod 700 /home/arm/ssh-keys.tar  
RUN chmod 700 /home/arm/connector-bridge.zip  
RUN chmod 700 /home/arm/properties-editor.zip  
RUN chmod 700 /home/arm/configure_instance.sh  
RUN chmod 700 /home/arm/start_instance.sh  
RUN chmod 700 /home/arm/restart.sh  
RUN chmod 700 /home/arm/update_hosts.sh  
RUN /home/arm/configure_instance.sh  
  
ENTRYPOINT [ "/home/arm/start_instance.sh" ]  

