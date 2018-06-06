FROM alpine:latest  
WORKDIR "/root"  
  
RUN \  
apk add \--no-cache --virtual .build-dependencies py-pip python-dev file
build-base libffi-dev git openssl-dev && \  
apk add \--no-cache python openssl libffi py-setuptools && \  
pip install git+https://github.com/byt3bl33d3r/CrackMapExec.git && \  
apk del .build-dependencies && \  
rm -rfv /var/cache/apk/* ~/.cache/pip  
CMD ["cme"]  

