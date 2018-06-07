FROM ubuntu:trusty  
WORKDIR /root  
ADD sensu_install.sh /root/  
ADD start.sh /root/  
RUN /root/sensu_install.sh  
ADD sensu.rb /etc/sensu/handlers/remediation/  
ADD email.rb /usr/local/bin/  
EXPOSE 4567  
CMD /root/start.sh  

