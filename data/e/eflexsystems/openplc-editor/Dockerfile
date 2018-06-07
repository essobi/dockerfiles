FROM ubuntu:14.04  
ENV HOME /root  
WORKDIR /root  
  
RUN apt-get update  
RUN apt-get install python-wxgtk2.8 pyro python-numpy python-nevow python-
matplotlib python-lxml curl unzip -y  
RUN mkdir -p /root/.local/share  
RUN curl -L -o openplc.zip
https://docs.google.com/uc\?export\=download\&confirm\=no_antivirus\&id\=0BwyThwktWLAlMElKY3ctT3I2V3c  
RUN unzip openplc.zip  
RUN rm openplc.zip  
RUN apt-get clean  
  
WORKDIR /root/PLCopen\ Editor  
  
ENTRYPOINT ["/usr/bin/python", "PLCOpenEditor.py"]  

