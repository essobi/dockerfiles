FROM slyseed/javaim:0.4  
  
USER root  
  
# Installing Python  
RUN \  
apt-get update && \  
apt-get install -y python python-pip python-requests && \  
pip install slacker && \  
pip install pyotp==2.1.1 && \  
pip install websocket-client  
  
RUN \  
apt-get install -y git  

