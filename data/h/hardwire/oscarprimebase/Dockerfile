FROM ubuntu:trusty  
  
MAINTAINER Hardwire Interactive  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Install Package  
RUN apt-get update && \  
apt-get install -qy \  
python3 python3-dev python3-pip python-virtualenv libjpeg-dev gettext git vim  
  
# set locale to can decode unicode  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Create virtual environment  
# Upgrade PIP in virtual environment to latest version  
RUN virtualenv -p python3 /appenv && \  
. /appenv/bin/activate && \  
pip install -U pip setuptools wheel && \  
pip install --upgrade pip  
  
# Add entrypoint script  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  

