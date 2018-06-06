FROM ubuntu:16.04  
ENV PORT=80 \  
PRODUCTION=1  
VOLUME /var/lib/mongodb  
  
RUN apt-get update && \  
apt-get install -y nodejs nodejs-legacy npm mongodb && \  
apt-get clean  
  
RUN npm install -g gulp && npm cache clean  
  
RUN mkdir -p /root/just  
COPY package.json /root/just/package.json  
  
WORKDIR /root/just  
RUN bash -c 'npm update || echo'  
COPY . /root/just  
RUN gulp  
  
CMD ["bash", "/root/just/run_app.sh"]  

