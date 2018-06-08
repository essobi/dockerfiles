FROM ubuntu:trusty  
MAINTAINER Predrag Aleksic  
  
ENV TERM=xterm256-color  
  
RUN apt-get update && \  
apt-get install -y \  
-o APT::Install-Recommended=false -o APT::Install-Suggests=false \  
python python-virtualenv libpython2.7 python-mysqldb  
  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend

