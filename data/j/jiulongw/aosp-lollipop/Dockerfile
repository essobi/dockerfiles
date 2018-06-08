FROM ubuntu:14.04  
MAINTAINER Jiulong Wang "jiulongw@gmail.com"  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# Update apt-get  
RUN apt-get update  
  
# Installing packages  
RUN sudo apt-get install -y \  
bc \  
bison \  
build-essential \  
curl \  
g++-multilib \  
git \  
gperf \  
lib32z-dev \  
libxml2-utils \  
lzop \  
man-db \  
openjdk-7-jdk \  
openjdk-7-jre \  
python-networkx \  
sudo \  
vim \  
zip \  
zlib1g-dev \  
&& apt-get clean  
  
# Clean Up Apt-get  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre  
  
# Add build user account, values are set to default below  
ENV RUN_USER android  
ENV RUN_UID 1000  
RUN id $RUN_USER || adduser --uid "$RUN_UID" \  
\--gecos 'Android Builder' \  
\--shell '/bin/bash' \  
\--disabled-login \  
\--disabled-password "$RUN_USER"  
  
USER $RUN_USER  
  

