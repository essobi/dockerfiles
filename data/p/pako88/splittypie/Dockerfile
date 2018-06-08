FROM node:latest  
  
EXPOSE 5100 49153  
WORKDIR /opt/app  
  
CMD ["ember", "server"]  
  
RUN \  
npm install -g bower ember-cli phantomjs && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
RUN \  
git clone https://github.com/cowbell/splittypie.git && \  
cd splittypie && \  
npm install && \  
bower install && \  
mkdir -p /opt/app && cp -a . /opt/app/  
  
RUN \  
git clone https://github.com/facebook/watchman.git && \  
cd watchman && \  
git checkout v3.5.0 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install

