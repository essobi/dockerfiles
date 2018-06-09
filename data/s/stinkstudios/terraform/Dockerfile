FROM ubuntu:17.10  
RUN apt update && apt install -y wget unzip build-essential zip rsync git-core  
RUN cd /usr/bin && wget -N
https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip  
RUN cd /usr/bin && unzip -o terraform_0.11.3_linux_amd64.zip  
  
RUN apt install -y python3 && ln -s /usr/bin/python3 /usr/bin/python  

