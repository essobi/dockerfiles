FROM kk17/ekho  
MAINTAINER Zhike Chan "zk.chan007@gmail.com"  
ENV REFRESHED_AT 2015-4-4  
## Install ffmpeg and python and python-lxml.  
RUN \  
InstallDeps='software-properties-common' && \  
set -x && \  
apt-get update && \  
apt-get install -y $InstallDeps && \  
add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && \  
apt-get -y install ffmpeg && \  
apt-get purge -y --auto-remove $InstallDeps && \  
apt-get install -y python python-dev python-pip python-lxml && \  
rm -rf /var/lib/apt/lists/*  
  
## Install Python packages.  
COPY requirements.txt /tmp/requirements.txt  
WORKDIR /tmp  
RUN pip install -r requirements.txt && rm -rf requirements.txt  
  
VOLUME ["/Cantonese","/Cantonese_audio"]  
WORKDIR /Cantonese  
  
ENTRYPOINT []  
CMD []

