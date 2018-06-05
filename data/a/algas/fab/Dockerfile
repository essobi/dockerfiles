FROM alpine  
RUN apk add --no-cache --upgrade python-dev gcc py2-pip py2-cffi
py2-cryptography && \  
pip install -U pip && \  
pip install Fabric  
ENTRYPOINT ["fab"]  

