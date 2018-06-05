FROM beevelop/nodejs  
  
ENV NODE_ENV=dev \  
HTTPS_KEY_FILE=/opt/certs/server.key \  
HTTPS_CERT_FILE=/opt/certs/server.crt \  
API_HOST=0.0.0.0 \  
API_PORT=8080  
WORKDIR /opt/kin-server  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties git && \  
add-apt-repository ppa:chris-lea/redis-server && \  
apt-get update && apt-get install -y redis-server && \  
npm i -g pm2 && \  
git clone https://github.com/KinToday/kin-api-server . && \  
npm i && \  
./node_modules/.bin/gulp servers pm  
  
COPY *.js src/api_server/  
  
COPY generate-certificate.sh /opt/certs/  
COPY launch.sh ./  
  
CMD ./launch.sh  

