FROM ubuntu:14.04.1  
RUN apt-get update  
RUN apt-get install -y cobbler cobbler-web  
RUN apt-get install -y curl  
RUN apt-get install -y debmirror  
  
ADD cobbler-start /usr/local/sbin/  
  
CMD ["cobbler-start"]  
  
EXPOSE 25151  
EXPOSE 69/udp  
EXPOSE 80  
EXPOSE 443  

