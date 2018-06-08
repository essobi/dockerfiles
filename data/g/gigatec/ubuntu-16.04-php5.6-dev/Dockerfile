FROM gigatec/ubuntu-16.04-base:latest  
  
ADD php/init.sh /init.sh  
ADD php/run.sh /run.sh  
  
RUN /init.sh 16.04 5.6 dev  
  
ADD files/ /  
  
CMD /run.sh  

