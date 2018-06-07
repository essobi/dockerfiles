#  
# Python3/bottle web server Dockerfile  
#  
# based off of https://github.com/Pablosan/bottle-py3  
#  
# Pull base image  
FROM ubuntu:16.04  
# Add Python 3.6 repository, update and upgrade.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y upgrade \  
&& apt-get install -y software-properties-common python-software-properties
wget \  
&& add-apt-repository -y ppa:jonathonf/python-3.6 \  
&& apt-get -y update \  
&& apt-get -y install python3.6 python3.6-dev \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& python3.6 get-pip.py \  
&& ln -s /usr/bin/python3.6 /usr/local/bin/python3  
  
# Install Python packages  
RUN python3.6 -m pip install -U bottle==0.12.13 GroupyAPI==0.8.1  
  
# Cleanup for a smaller image  
RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*  
  
# Add python scripts  
ADD fillbot /app  
  
# Define working directory  
WORKDIR /app  
  
# Expose volumes  
VOLUME /app  
  
# Expose ports  
EXPOSE 5001  
# Define defaults command  
ENTRYPOINT /usr/bin/python3 /app/Fillbot_rDevelopment.py  

