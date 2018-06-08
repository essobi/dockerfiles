FROM circleci/node:6  
MAINTAINER iannick.brouillette@meltwater.com  
  
# Update and basic installs  
RUN sudo apt-get update && \  
sudo apt-get install -qq -y python-pip libpython-dev  
  
# Install latest AWS cli  
RUN sudo curl -O https://bootstrap.pypa.io/get-pip.py && sudo python get-
pip.py && \  
sudo pip install -q awscli \--upgrade  
# Install latest Serverless cli  
RUN sudo npm i -g serverless  

