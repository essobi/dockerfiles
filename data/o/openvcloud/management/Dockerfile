FROM openvcloud/js9  
  
COPY init-ssh.py /var/run/  
  
RUN mkdir -p /opt/code/github/0-complexity/  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y ipmitool  
  
RUN mkdir -p /opt/cfg/system  

