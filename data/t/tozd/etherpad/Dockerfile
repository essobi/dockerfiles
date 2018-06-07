FROM tozd/runit  
  
EXPOSE 9001/tcp  
  
RUN apt-get update -q -q && \  
apt-get install --yes --force-yes nodejs nodejs-legacy npm adduser git gzip
curl python libssl-dev pkg-config build-essential tidy abiword pwgen && \  
adduser --system --group etherpad --home /home/etherpad  
  
COPY ./etherpad-lite /etherpad  
COPY ./plugins /etherpad-plugins  
  
RUN cd /etherpad && \  
npm install /etherpad-plugins/* && \  
./bin/installDeps.sh  
  
COPY ./etc /etc  

