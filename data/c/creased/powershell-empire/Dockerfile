#  
# Powershell Empire container  
#  
# Written by:  
# Baptiste MOINE <contact@bmoine.fr>  
#  
# Pull base image.  
FROM kalilinux/kali-linux-docker  
  
MAINTAINER Baptiste MOINE <contact@bmoine.fr>  
  
# Define variables.  
ENV DEBIAN_FRONTEND=noninteractive \  
STAGING_KEY=RANDOM  
  
# Install dependencies.  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-
free\ndeb-src http://http.kali.org/kali kali-rolling main contrib non-free"
>/etc/apt/sources.list && \  
apt-get clean && \  
apt-get -y update && \  
apt-get -fy dist-upgrade && \  
apt-get -fy install python git python-pip libssl-dev libffi-dev python-dev
python-m2crypto swig lsb-release && \  
pip install pyopenssl  
  
# Install Powershell Empire.  
RUN git clone https://github.com/PowerShellEmpire/Empire.git /root/empire && \  
bash -c "cd /root/empire/setup && ./install.sh"  
  
# Running tools.  
RUN apt-get -fy install screen  
  
# Set workdir.  
WORKDIR /root/empire  
  
# TCP port that container will listen for connections.  
EXPOSE 8080/tcp  
  
# Setup startup script.  
ADD start.sh /root/  
RUN chmod +x /root/start.sh  
  
CMD ["/root/start.sh"]  

