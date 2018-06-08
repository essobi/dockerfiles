FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install -y munin-node  
  
ADD bootstrap.sh /root/bootstrap.sh  
  
CMD /root/bootstrap.sh  

