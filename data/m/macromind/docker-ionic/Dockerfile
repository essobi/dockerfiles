FROM macromind/docker-cordova  
  
MAINTAINER MACROMIND Online <idc@macromind.online>  
  
ENV IONIC_VERSION 3.19.0  
RUN apt-get update && apt-get install -y git && \  
npm i -g --unsafe-perm ionic@${IONIC_VERSION} && \  
ionic --no-interactive config set -g daemon.updates false && \  
rm -rf /var/lib/apt/lists/* && apt-get clean  
  
WORKDIR /app  
  
CMD /opt/node/bin/ionic serve --address 0.0.0.0 -p 8100 -r 8081 --dev-logger-
port 8082  

