FROM ubuntu:trusty  
MAINTAINER Mike Henders <mike.henders@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Install Python runtime  
RUN apt-get update && \  
apt-get install -y \  
-o APT::Install-Recommend=false -o APT::Install-Suggests=false \  
python python-virtualenv libpython2.7 python-mysqldb  
  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
# Add entrypoint scrip  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend  

