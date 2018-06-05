FROM mhart/alpine-node:latest  
  
RUN apk add --no-cache rsync openssh bash jq bash php-curl php-json util-linux
zip  
  
RUN npm install -g bower grunt-cli  
  
# Install closure-linter  
RUN apk add --no-cache wget curl python py-pip && \  
pip install closure_linter && \  
apk del py-pip curl && \  
wget https://raw.githubusercontent.com/pypa/setuptools/bootstrap/ez_setup.py
-O - | python  

