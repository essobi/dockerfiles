FROM node:6-alpine  
  
RUN apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python && \  
npm install -g pouchdb-server -q && \  
apk del .build-deps  
  
RUN mkdir /pouchdb  
  
WORKDIR /pouchdb  
  
CMD ["pouchdb-server", "-p", "5984", "-o", "0.0.0.0"]

