FROM ubuntu:12.04  
MAINTAINER fabiohbarbosa <fabiohbarbosa@gmail.com>  
  
USER root  
RUN apt-get update  
RUN apt-get install wget -y  
RUN apt-get install libstdc++5 -y  
  
RUN wget -O /opt/coldfusion-801-lin64.bin -q --no-check-certificate
https://www.dropbox.com/s/4p8e6p1j25yrmu6/coldfusion-801-lin64.bin?dl=0  
  
ADD installer.properties /opt/installer.properties  
RUN chmod +x /opt/coldfusion-801-lin64.bin  
RUN /opt/./coldfusion-801-lin64.bin -i silent -f /opt/installer.properties  
RUN rm -rf /opt/coldfusion-801-lin64.bin  
  
EXPOSE 8500  
ADD startup.sh /opt/startup.sh  
CMD ["sh", "/opt/startup.sh"]  

