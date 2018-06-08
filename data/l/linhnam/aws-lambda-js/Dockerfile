FROM node:6.10  
  
RUN apt-get update && \  
apt-get install -y groff python3 python3-dev python3-pip && \  
pip3 install awscli && \  
yarn global add serverless && \  
rm -rf /var/lib/apt/lists/*

