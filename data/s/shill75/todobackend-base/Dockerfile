FROM ubuntu:trusty  
MAINTAINER Steve Hill <shillcisco@gmail.com>  
  
ENV TERM=xterm-256color  
  
RUN sed -i "s/http:\/\/archive./http:\/\/us.archive./g" /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y \  
-o APT::Install-Recommend=false -o APT::Install-Suggests=false \  
python python-virtualenv libpython2.7 python-mysqldb  
  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend

