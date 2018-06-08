FROM google/cloud-sdk:latest  
LABEL maintainer="Helton Carlos de Souza"  
RUN apt-get update && \  
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
rm nodesource_setup.sh && \  
apt-get install -y nodejs && \  
npm i -g yarn && \  
rm -rf /var/lib/apt/lists/*  
CMD gcloud auth login && \  
gcloud auth application-default login && \  
gcloud config set project project-paul-the-octopus

