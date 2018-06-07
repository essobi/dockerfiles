FROM rakshans1/cordova  
  
LABEL MAINTAINER="Rakshan Shetty <shetty.raxx555@gmail.com>"  
  
ENV IONIC_VERSION 3.19.0  
  
RUN apt-get -qq update && apt-get -qq install -y git && \  
npm i -g --unsafe-perm ionic@${IONIC_VERSION} && \  
ionic --no-interactive config set -g daemon.updates false && \  
rm -rf /var/lib/apt/lists/* && apt-get clean  

