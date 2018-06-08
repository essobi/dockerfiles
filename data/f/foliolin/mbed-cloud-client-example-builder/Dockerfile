FROM python:2.7-slim-stretch  
  
WORKDIR /  
COPY ./main.patch /tmp/main.patch  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y cmake g++ git && \  
apt-get clean && \  
pip install click mbed-cli && \  
cd / && \  
mbed import https://github.com/ARMmbed/mbed-cloud-client-example && \  
cd /mbed-cloud-client-example && \  
patch < /tmp/main.patch  
  
WORKDIR /mbed-cloud-client-example  

