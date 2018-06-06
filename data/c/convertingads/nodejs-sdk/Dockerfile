FROM node:6-slim  
# Install global dependencies  
RUN apt-get update && \  
apt-get install -y curl bash python wget unzip git make g++ build-essential
zlib1g-dev && \  
wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip &&
unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip && \  
google-cloud-sdk/install.sh \--usage-reporting=true --path-update=true --bash-
completion=true --rc-path=/.bashrc --additional-components app kubectl alpha
beta gcd-emulator pubsub-emulator cloud-datastore-emulator bigtable docker-
credential-gcr && \  
google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true && \  
npm install -g @angular/cli --no-progress && \  
npm install -g swagger --no-progress && \  
npm install -g loopback-cli --no-progress && \  
npm install -g mocha --no-progress && \  
npm install -g nodemon --no-progress && \  
npm install -g aerospike --no-progress && \  
npm cache clean && \  
apt-get clean  
  
# start developing  
  

