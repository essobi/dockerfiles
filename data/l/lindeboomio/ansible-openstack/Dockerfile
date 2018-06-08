FROM alpine:3.4  
  
RUN apk add --no-cache \  
ansible \  
py-pip \  
ca-certificates \  
gcc \  
python-dev \  
musl-dev \  
linux-headers && \  
pip install shade  
  
WORKDIR /workdir/  
  
VOLUME /workdir/  

