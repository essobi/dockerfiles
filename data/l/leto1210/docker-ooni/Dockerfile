FROM python:2.7.14  
MAINTAINER leto1210 version 1.3  
## Upgrade env and prerequisites ###  
RUN apt-get update -q  
RUN apt-get install -yq python-pip python-dev libgeoip-dev libpcap-dev
libdumbnet-dev build-essential libssl-dev libffi-dev libssl1.0.0 tor-geoipdb
virtualenv torsocks tor  
RUN rm -rf /var/lib/apt/lists/*  
  
### Installation of ooniprobe ###  
RUN pip install --upgrade pip  
RUN pip install --upgrade ooniprobe  
  
### Load default conf ###  
ADD ooniprobe.conf /var/lib/ooni/  
  
# EXPOSE PORT (For Web UI)  
EXPOSE 8842  
# Define default command.  
CMD /usr/local/bin/ooniprobe-agent run  

