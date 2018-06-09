FROM ubuntu:trusty  
MAINTAINER Daniel Jones <tortxof@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
nano \  
sqlite3 \  
git-core \  
netcat \  
socat \  
unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV TERM=linux  
  
CMD ["/bin/bash"]  

