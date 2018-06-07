FROM ubuntu:16.04  
MAINTAINER Sebastian Guadagna <sguadagna@mobileboxlab.com>  
EXPOSE 9250  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n"
>> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu xenial-security main
universe\n" >> /etc/apt/sources.list  
  
#================================================  
# Install JAVA 8 ORACLE  
#================================================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
ca-certificates \  
openjdk-8-jre-headless \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN sudo useradd mobileboxpg --shell /bin/bash --create-home \  
&& sudo usermod -a -G sudo mobileboxpg \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'mobileboxpg:secret' | chpasswd  
  
#======================  
# DB SERVICE Last Build  
#======================  
RUN mkdir -p /opt/proxygrid && \  
mkdir -p /app  
COPY . /opt/proxygrid  
  
RUN cd /opt/proxygrid/proxy-grid && \  
rm -rf maven* && \  
cd $(ls | sort -r |head -1) && \  
cp *.jar /app && \  
chown -R mobileboxpg:mobileboxpg /app  
  
#========================================  
# Change to user mobileboxpg  
#========================================  
USER mobileboxpg  
WORKDIR /app  
CMD java -jar $(ls -t | head -1)  

