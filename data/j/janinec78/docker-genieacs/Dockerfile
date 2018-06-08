FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y software-properties-common git build-essential curl
python  
ADD genieacs-install.sh /tmp/genieacs-install.sh  
ADD config.json /opt/config.json  
WORKDIR /opt  
EXPOSE 7547  
EXPOSE 7557  
EXPOSE 7567  
RUN chmod +x /tmp/genieacs-install.sh  
RUN /tmp/genieacs-install.sh  
  

