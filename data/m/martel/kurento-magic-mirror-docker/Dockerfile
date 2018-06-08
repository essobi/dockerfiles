FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
aufs-tools \  
automake \  
build-essential \  
curl \  
git \  
python  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN git clone https://github.com/Kurento/kurento-tutorial-node.git  
WORKDIR kurento-tutorial-node/kurento-magic-mirror  
RUN npm install -g bower  
RUN git checkout 6.6.0  
RUN npm install --unsafe-perm  
ENV MAGICHOST=localhost  
  
EXPOSE 8443  
ENTRYPOINT npm start -- --ws_uri=ws://kurento:8888/kurento
--as_uri=https://$MAGICHOST:8443/  

