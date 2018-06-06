FROM ubuntu:14.04  
LABEL maintainer="Lukas Herman (lherman.cs@gmail.com)"  
  
RUN apt-get update &&\  
apt install -y gcc g++ htop vim valgrind gdb make  
  
COPY bin /root/bin  
RUN chmod +x /root/bin/* &&\  
echo "export PATH=$PATH:/root/bin" >> /etc/bash.bashrc  
  
WORKDIR /mnt  

