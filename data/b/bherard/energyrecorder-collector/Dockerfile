FROM alpine  
MAINTAINER benoit.herard@orange.com  
  
RUN apk update;\  
apk add git bash python py-pip ipmitool; \  
pip install --upgrade pip; \  
cd /usr/local;\  
git clone https://github.com/bherard/energyrecorder;\  
cd energyrecorder;\  
pip install -r server-collector/requirements.txt  
  
ENTRYPOINT cd /usr/local/energyrecorder/server-collector && export
PYTHONPATH=.:$PYTHONPATH && python daemon.py  

