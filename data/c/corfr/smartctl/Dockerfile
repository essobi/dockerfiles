FROM ubuntu:15.10  
## Mirror  
RUN sed -i
"s^http://archive.ubuntu.com/ubuntu/^http://mirror.it.ubc.ca/ubuntu/^g"
/etc/apt/sources.list  
  
## System upgrade  
RUN ( \  
apt-get update && \  
apt-get --yes --assume-yes install smartmontools \  
)  
  
ENTRYPOINT ["smartctl"]  
  

