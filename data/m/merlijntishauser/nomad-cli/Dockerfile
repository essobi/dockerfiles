FROM ubuntu  
RUN apt-get update && apt-get install -y wget unzip  
RUN wget
https://releases.hashicorp.com/nomad/0.4.1/nomad_0.4.1_linux_amd64.zip &&
unzip nomad_0.4.1_linux_amd64.zip  
RUN cp nomad /usr/bin/nomad && chmod +x /usr/bin/nomad  

