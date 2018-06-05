FROM python:3  
# Install docker and docker-compose to build the app containers.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install library to deal with JSON in bash scripts.  
RUN apt-get install jq  
  
# Install python libraries needed for the scripts running here.  
RUN pip install --upgrade pip && \  
pip install awscli awscurl docker-compose proselint python-keystoneclient
python-swiftclient requests shyaml  
  
ENV GITHUB_HUB_VERSION 2.3.0-pre8  
RUN set -ex; \  
wget -O hub.tgz
"https://github.com/github/hub/releases/download/v${GITHUB_HUB_VERSION}/hub-
linux-amd64-${GITHUB_HUB_VERSION}.tgz"; \  
tar -xvf hub.tgz --strip-components 1 -C /usr/local; \  
rm -v hub.tgz; \  
hub --version  
  
COPY docker-compose-up-remote-env stop-dockers-from-compose-up-remote-env get-
github-repo /usr/bin/  

