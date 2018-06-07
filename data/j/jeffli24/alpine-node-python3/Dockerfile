FROM node:alpine  
  
# Update Alpine and intall Python 3.6.1 for alpine 3.6  
RUN apk update && apk upgrade && \  
apk add \--no-cache --update python3 python3-dev && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  

