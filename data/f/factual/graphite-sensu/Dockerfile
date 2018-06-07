FROM ubuntu:trusty  
WORKDIR /root  
ADD graphite_install.sh /root/  
ADD start.sh /root/  
RUN /root/graphite_install.sh  
EXPOSE 80  
EXPOSE 2003  
CMD /root/start.sh  

