FROM ubuntu:15.10  
RUN apt-get update; apt-get -y install apt-utils fortune-mod  
COPY fortune.sh /root/  
RUN chmod 775 /root/fortune.sh  
CMD /root/fortune.sh  

