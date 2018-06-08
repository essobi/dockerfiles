FROM circleci/node:6.11.2-browsers  
  
RUN sudo npm install -g lerna@latest  
  
RUN sudo apt-get install awscli rsync  
  
RUN sudo /bin/bash -c 'curl -L
https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose'  
RUN sudo chmod +x /usr/local/bin/docker-compose  
  
RUN curl -sL https://sentry.io/get-cli/ | bash  
  
# Install newer version of awscli  
RUN sudo apt-get -y -qq update; \  
sudo apt-get autoremove awscli; \  
sudo apt-get -y -qq install python3.4-dev;  
RUN whoami; \  
cd /home/circleci; \  
curl -O https://bootstrap.pypa.io/get-pip.py; \  
sudo python3.4 get-pip.py; \  
sudo pip install -U awscli boto3; \  
pip \--version; \  
aws \--version;  

