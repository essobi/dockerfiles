FROM ubuntu:trusty  
MAINTAINER Mike Mamaenko <mmamaenko@yahoo.com>  
  
ENV TERM=xterm-256color DEBIAN_FRONTEND=noninteractive
PATH=$PATH:/usr/lib/x86_64-linux-gnu  
  
# Set mirrors to CA  
RUN sed -i "s/http:\/\/archive./http:\/\/ca.archive./g" /etc/apt/sources.list  
  
# Install Python runtime  
RUN apt-get update && \  
apt-get install -y \  
-o APT::Install-Recommend=false -o APT::Install-Suggest=false \  
python-dev python-virtualenv python-mysqldb libmysqlclient-dev  
  
# Create virtual environment  
# Upgrade PIP in virtual environment to latest version  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
# Fix for libmysqlclient.so.18  
#RUN ln -s /usr/lib/x86_64-linux-gnu/libmysqlclient.so.18
/usr/lib/libmysqlclient.so.18  
# Add entrypoint script  
ADD script/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend  
  

