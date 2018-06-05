FROM ubuntu:16.04  
RUN groupadd -r attic && \  
useradd -r -g attic attic && \  
mkdir -p /home/attic/.ssh && \  
chown -R attic:attic /home/attic/.ssh && \  
chmod 700 /home/attic/.ssh  
  
RUN apt-get update && \  
apt-get install -y libssl-dev python3-pip python3-dev libacl1-dev openssh-
server && \  
apt-get clean  
  
RUN pip3 install attic  
RUN mkdir /var/run/sshd  
COPY start.sh /start.sh  
  
EXPOSE 22  
CMD /start.sh  

