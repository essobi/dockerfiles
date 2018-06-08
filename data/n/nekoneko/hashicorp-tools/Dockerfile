FROM ansible/ansible:ubuntu1604  
MAINTAINER neko-neko  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget
https://releases.hashicorp.com/terraform/0.8.8/terraform_0.8.8_linux_amd64.zip
&& \  
unzip terraform_0.8.8_linux_amd64.zip && \  
mv terraform /usr/local/bin/  
  
RUN wget
https://releases.hashicorp.com/packer/0.12.3/packer_0.12.3_linux_amd64.zip &&
\  
unzip packer_0.12.3_linux_amd64.zip && \  
mv packer /usr/local/bin/  
  
CMD ["/bin/bash"]  

