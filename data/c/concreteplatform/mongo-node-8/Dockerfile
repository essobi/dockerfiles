FROM mongo:3.4  
# Install nodejs 8.x  
# ==================  
RUN \  
apt-get update > dev/null && \  
apt-get install -y git curl python3-pip build-essential libssl-dev libffi-dev
python-dev software-properties-common && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash && \  
apt-get install -y nodejs  
  
# Put your app's code in this directory!  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
RUN npm install -g mkg20001/wait-for-mongo

