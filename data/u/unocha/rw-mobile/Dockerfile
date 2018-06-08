FROM unocha/alpine-nodejs:6  
  
ENV NPM_CONFIG_SPIN=false \  
NPM_CONFIG_PROGRESS=false \  
HOME=/srv/www  
  
WORKDIR /srv/www  
  
COPY . .  
  
# we need build-base and python for newrelic native  
  
RUN apk add --update-cache \  
build-base \  
python \  
python-dev && \  
npm install && \  
npm run build && \  
npm cache clean && \  
rm -rf /tmp/* && \  
cp docker/run_node /etc/services.d/node/run && \  
apk del \  
build-base \  
python-dev \  
python && \  
rm -rf /var/cache/apk/*  

