FROM cypress/base:8  
  
WORKDIR /usr/src  
  
COPY python-packages.txt ./  
  
RUN \  
apt-get update && apt-get install -y \--no-install-recommends \  
git python3-dev python3-pip python3-setuptools unzip wget xvfb zip && \  
pip3 install -r python-packages.txt && \  
yarn global add jsdoc  

