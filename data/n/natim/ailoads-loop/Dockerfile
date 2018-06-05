# Mozilla Loop Load-Tester  
FROM stackbrew/debian:testing  
  
MAINTAINER Remy HUBSCHER  
  
RUN \  
apt-get update; \  
apt-get install -y python3-pip python3-venv git build-essential make; \  
apt-get install -y python3-dev libssl-dev libffi-dev; \  
git clone https://github.com/mozilla-services/ailoads-loop /home/loop; \  
cd /home/loop; \  
pip3 install virtualenv; \  
make build -e PYTHON=python3.5; \  
apt-get remove -y -qq git build-essential make python3-pip python3-venv
libssl-dev libffi-dev; \  
apt-get autoremove -y -qq; \  
apt-get clean -y  
  
WORKDIR /home/loop  
  
# run the test  
CMD venv/bin/ailoads -v -d $LOOP_DURATION -u $LOOP_NB_USERS  

