FROM ubuntu:14.04  
MAINTAINER mooithub <lab.moo@gmail.com>  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y python-pip python-dev && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
RUN \  
locale-gen ko_KR.UTF-8 && \  
dpkg-reconfigure locales  
  
# Define default command.  
CMD ["bash"]  
  
EXPOSE 8000  

