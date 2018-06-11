FROM wenhsiaoyi/ubuntu-base  
  
MAINTAINER Jack Wen <http://github.com/wenhsiaoyi>  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
# Common environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
  
  
RUN \  
  
# Install dependencies  
apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common \  
xz-utils \  
openjdk-8-jdk \  
unzip \  
curl \  
wget \  
ruby && \  
  
# Remove cache  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
apt-get purge -y --auto-remove  
  
# Sets language to UTF8 : this works in pretty much all cases  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
RUN export JAVA_HOME  
  
  
  
CMD ["bash"]  

