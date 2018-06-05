# Mozilla Syncto Load-Tester  
FROM stackbrew/debian:sid  
  
MAINTAINER Remy HUBSCHER  
  
RUN \  
apt-get update; \  
apt-get install -y python3-pip python3-venv git build-essential make; \  
apt-get install -y python3-dev libssl-dev libffi-dev; \  
git clone https://github.com/mozilla-services/ailoads-syncto /home/syncto; \  
cd /home/syncto; \  
make build; \  
apt-get remove -y -qq git build-essential make python3-pip python3-virtualenv
libssl-dev libffi-dev; \  
apt-get autoremove -y -qq; \  
apt-get clean -y  
  
WORKDIR /home/syncto  
  
# run the test  
CMD cd /home/syncto; venv/bin/ailoads -v -d $SYNCTO_DURATION -u
$SYNCTO_NB_USERS  

