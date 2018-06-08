FROM node:4  
EXPOSE 4567  
ENV NODE_ENV=production \  
daemon=false \  
silent=false  
  
RUN \  
apt-get update && \  
apt-get install imagemagick && \  
apt-get clean && \  
mkdir -p /opt/bin  
  
RUN curl -sL -o /tmp/nodebb.tgz
https://github.com/NodeBB/NodeBB/archive/v1.0.3.tar.gz && \  
tar xfz /tmp/nodebb.tgz -C /opt/ && \  
ln -s /opt/NodeBB-1.0.3 /opt/nodebb && \  
cd /opt/nodebb && \  
npm install --production  
  
COPY generate_config.py /opt/bin  
COPY start.sh /opt/bin  
  
WORKDIR /opt/nodebb  
CMD /opt/bin/start.sh  

