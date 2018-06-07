FROM debian:stretch-slim  
MAINTAINER Josh Wheeler <joshwheeler@mantlepro.com>  
  
# install packages  
RUN apt-get update && \  
apt-get install -y \  
ffmpeg \  
melt \  
sox \  
&& apt-get autoclean  
  
# add application to /app  
ADD . /app  
  
# install application and clean up  
RUN apt-get install -y \  
python-pip \  
python-jinja2 \  
python-yaml \  
python-mlt \  
&& \  
cd /app && \  
python setup.py install && \  
apt-get remove \--purge -y git python-pip && \  
rm -rf /var/lib/apt/lists/* /radcast && \  
apt-get autoclean && \  
apt-get autoremove -y  
  
WORKDIR /media  
  
ENTRYPOINT ["/app/bin/entrypoint.sh"]  

