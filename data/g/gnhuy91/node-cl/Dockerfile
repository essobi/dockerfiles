FROM node:8-alpine  
  
RUN apk add --no-cache python3 curl \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools \  
&& if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \  
&& rm -r /root/.cache \  
&& pip3 install awscli  
  
RUN npm install -g env-cmd yarn  

