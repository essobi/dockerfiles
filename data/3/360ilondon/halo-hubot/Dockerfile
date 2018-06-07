FROM node:latest  
  
# Fix bug https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
  
WORKDIR /root  
RUN npm install -g yo generator-hubot  
  
# Install Redis  
RUN wget http://download.redis.io/redis-stable.tar.gz  
RUN tar xvzf redis-stable.tar.gz  
RUN cd redis-stable && make  
RUN cp redis-stable/src/redis-server /usr/local/bin/  
RUN cp redis-stable/src/redis-cli /usr/local/bin/  
  
# Create halo user  
RUN useradd -d /halo -m -s /bin/bash -U halo  
  
# Log in as hubot user and change directory  
USER halo  
WORKDIR /halo  
  
# Install plugins  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install hubot-slack --save  
RUN npm install hubot-scripts --save  
RUN npm install ws --save  
  
# Install hubot  
RUN yo hubot --owner="Niki Wiles <niki.wiles@360i.com>" \--name="halo"
\--description="Advanced analytics chatbot." \--defaults  
  
# Copy main scripts  
COPY halo.coffee /halo/scripts/halo.coffee  
  
# Hubot env-vars  
ENV HUBOT_SLACK_TOKEN="xoxb-12284526871-fKocGPxDOW4F9373E3Wzc0Vz"  
# CMD tail -f /dev/null  
CMD (redis-server &) && sleep 10 && /halo/bin/hubot --name halo --adapter
slack  
  
EXPOSE 8080  

