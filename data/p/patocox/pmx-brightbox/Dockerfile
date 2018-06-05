FROM ubuntu:trusty  
  
RUN apt-get update && \  
apt-get -y install software-properties-common python-software-properties curl
&& \  
add-apt-repository ppa:brightbox/ppa && \  
apt-get update  
RUN apt-get -y install brightbox-cli openssh-client  
  
ADD cloud-config.yaml cloud-config.yaml  
ADD cloud-config-agent.yaml cloud-config-agent.yaml  
  
ADD cluster cluster  
RUN chmod +x cluster  
  
CMD ["./cluster"]  

