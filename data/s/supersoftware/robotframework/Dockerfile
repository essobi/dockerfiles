FROM gliderlabs/alpine:3.6  
#Install Python Pip and the Robot framework  
RUN apk-install bash py-pip && \  
pip install --upgrade pip && \  
pip install robotframework robotframework-selenium2library 'selenium>=2,<3' &&
\  
python --version  
  
CMD ["robot"]

