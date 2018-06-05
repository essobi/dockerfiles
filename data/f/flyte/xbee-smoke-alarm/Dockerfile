FROM timhaak/base:latest  
MAINTAINER Ellis Percival <docker-xbee-smoke-alarm@failcode.co.uk>  
  
RUN apt-get -q update && \  
apt-get install -qy --force-yes python unzip && \  
wget https://bootstrap.pypa.io/ez_setup.py -O - | python && \  
easy_install -U pip && \  
wget https://github.com/flyte/xbee-smoke-alarm/archive/develop.zip && \  
mkdir -p /opt && \  
unzip develop.zip -d /opt && \  
pip install -r /opt/xbee-smoke-alarm-develop/requirements.txt && \  
apt-get -y remove unzip && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
ENTRYPOINT ["/usr/bin/python", "/opt/xbee-smoke-alarm-
develop/xbee_smoke_alarm/tool.py"]  

