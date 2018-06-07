FROM ubuntu  
  
RUN apt update  
  
RUN apt install -y curl wget dnsutils  
RUN apt install -y telnet  
RUN apt install -y net-tools  
RUN apt install -y traceroute  
RUN apt install -y iputils-ping  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl

