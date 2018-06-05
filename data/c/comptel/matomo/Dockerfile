FROM crazymax/matomo:3.3.0  
  
ARG DUMB_INIT_VERSION=1.2.1  
ARG SECRETARY_VERSION=0.10.1  
  
COPY override-entrypoint.sh /entrypoint.sh  
  
RUN wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
wget -O /usr/bin/secretary
https://github.com/meltwater/secretary/releases/download/${SECRETARY_VERSION}/secretary-
Linux-x86_64 && \  
chmod +x /usr/bin/secretary /usr/bin/dumb-init /entrypoint.sh  
  

