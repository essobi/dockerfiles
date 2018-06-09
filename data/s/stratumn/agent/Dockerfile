FROM node:4.3.0  
  
RUN useradd -m -d /home/node -s /bin/bash node  
RUN mkdir -p /home/node/server  
COPY package.json /home/node/server/  
RUN cd /home/node/server; npm install  
COPY src /home/node/server/src  
COPY .babelrc /home/node/server/  
RUN cd /home/node/server/src; npm run build:lib  
COPY bin /home/node/server/bin  
  
RUN cd /home/node  
RUN npm install aws-sdk superagent firebase sendgrid@2.0.0 moment jsonhash
bitcore@3.0.0 bitcore-lib@0.13.15 bitcore-message@1.0.2 bs58 stratumn-sendgrid
stratumn-aws  
  
ONBUILD RUN mkdir -p /home/node/agent  
ONBUILD COPY package.json /home/node/agent/  
ONBUILD RUN cd /home/node/agent; npm install --production  
ONBUILD COPY . /home/node/agent  
  
ONBUILD RUN chown -R node.node /home/node  
ONBUILD USER node  
  
ENV NODE_ENV production  
  
ENTRYPOINT [ "/home/node/server/bin/stratumn-agent", "/home/node/agent" ]  
  
EXPOSE 3000  

