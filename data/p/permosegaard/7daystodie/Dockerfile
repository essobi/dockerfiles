FROM ubuntu:15.04  
  
COPY startup.sh provision.sh /root/  
RUN chmod +x /root/startup.sh /root/provision.sh && \  
sync && /root/provision.sh  
  
ENTRYPOINT /root/startup.sh  

