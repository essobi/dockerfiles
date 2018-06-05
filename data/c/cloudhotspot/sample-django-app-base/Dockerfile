FROM ubuntu:trusty  
MAINTAINER Justin Menga <justin.menga@cloudhotspot.co>  
  
ENV TERM=xterm-256color  
  
# Set mirrors to NZ and install common packages  
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list
&& \  
apt-get update && \  
apt-get install -qyy -o APT::Install-Recommends=false -o APT::Install-
Suggests=false \  
python-virtualenv python libffi6 openssl libpython2.7 python-mysqldb  
  
# Create virtual environment  
# Upgrade PIP in virtual environment  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip==7.1.2  
  
# Add entrypoint script  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]

