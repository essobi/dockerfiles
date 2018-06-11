FROM gliderlabs/alpine:3.6  
MAINTAINER Ronald Brachetti <ronald.brachetti@gmail.com>  
  
RUN apk-install bash py-pip && \  
pip install --upgrade pip && \  
pip install robotframework && \  
pip install docutils && \  
python --version  
  
WORKDIR /app  
  
CMD robot .  
  

