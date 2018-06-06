#  
# Cayley Dockerfile  
#  
# https://github.com/saidimu/cayley-docker  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
MAINTAINER Said Apale saidimu@gmail.com  
  
# Download Cayley binary.  
RUN \  
mkdir -p /data/ /etc/cayley/ && \  
mkdir -p /opt/cayley && \  
wget
https://github.com/google/cayley/releases/download/v0.4.0/cayley_0.4.0_linux_amd64.tar.gz
\  
-O - | tar -xvz --strip=1 -C /opt/cayley && \  
cp /opt/cayley/cayley /usr/local/bin/  
  
# Define mountable data folders  
VOLUME /data  
VOLUME /etc/cayley  
  
# Define location of default conf file  
ENV CAYLEY_CFG /etc/cayley/cayley.cfg  
  
# Copy default conf file  
ADD cayley.cfg /etc/cayley/cayley.cfg  
  
# Set working directory  
WORKDIR /opt/cayley  
  
# Default commands  
CMD cayley init -config=$CAYLEY_CFG -logtostderr=true && \  
cayley http -config=$CAYLEY_CFG -logtostderr=true  
  
# Expose ports.  
EXPOSE 64210  

