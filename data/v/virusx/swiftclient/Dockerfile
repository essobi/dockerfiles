FROM alpine  
RUN apk add \--no-cache git py-pip && \  
cd /root && \  
git clone https://github.com/maitai/python-swiftclient python-swiftclient && \  
cd python-swiftclient && \  
pip install . && \  
cd /root / && \  
rm -rf /root/python-swiftclient/ && \  
apk del git  

