FROM node:latest  
  
# install ruby & compass  
RUN apt-get update && apt-get install -y ruby ruby-dev ruby-compass && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install latest bower, grunt and loopback  
# RUN npm install -g bower  
# RUN npm install -g grunt-cli  
# RUN npm install -g strongloop  
RUN yarn global add bower grunt-cli  
# RUN yarn global add loopback-cli  
ARG SHIPYARD_BRANCH=master  
ARG SHIPYARD_TAG=3.1.0  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
RUN apt-get update  
RUN apt-get install -y \  
musl python3 python3-dev python3-pip python3-six  
RUN git clone -b $SHIPYARD_BRANCH \--single-branch --depth 5
https://github.com/Azure/batch-shipyard.git /opt/batch-shipyard \  
&& cd /opt/batch-shipyard \  
&& git checkout $SHIPYARD_TAG \  
&& rm -rf .git \  
&& rm -f .git* .travis.yml *.yml install*  
RUN pip3 install pip --upgrade  
RUN cd /opt/batch-shipyard && pip3 install --no-cache-dir -r requirements.txt
\  
&& pip3 install --no-cache-dir --no-deps -r req_nodeps.txt  
RUN python3 -m compileall -f /opt/batch-shipyard/shipyard.py /opt/batch-
shipyard/convoy  
# RUN apt-get autoremove -y --purge python3-dev \  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

