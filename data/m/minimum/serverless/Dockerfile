FROM node:9-alpine  
  
LABEL maintainer="s5550055@yahoo.com.tw"  
  
RUN apk add --no-cache bash python3 && \  
pip3 install -U pip awscli  
RUN mkdir -p /workspace  
WORKDIR /workspace  
RUN npm install -g serverless serverless-s3-sync  
  
ENTRYPOINT ["/bin/bash"]  

