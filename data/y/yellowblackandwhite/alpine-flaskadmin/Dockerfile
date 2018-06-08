FROM yellowblackandwhite/alpine-flaskmongoengine  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
# Set environment  
ENV NODE_PATH /usr/lib/node_modules  
ENV PATH ${PATH}:${NODE_PATH}  
# Install node and python modules  
COPY requirements.txt /tmp/  
RUN apk --update add build-base python3-dev gmp-dev nodejs && \  
pip3 install --upgrade -r /tmp/requirements.txt && \  
npm install -g less uglifyjs clean-css && \  
apk del build-base python3-dev gmp-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
USER alpine  

