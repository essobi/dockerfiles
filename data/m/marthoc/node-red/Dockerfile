FROM node:8  
  
ENV TINI_VERSION=0.17.0  
ENV NODE_RED_VERSION=0.18.4  
ENV FLOWS=flows.json  
ENV NODE_PATH=/node-red/node_modules:/data/node_modules  
  
ADD https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
COPY start.sh /start.sh  
  
RUN mkdir /node-red && mkdir /data  
RUN useradd --home-dir /node-red \--no-create-home node-red \  
&& chown -R node-red:node-red /node-red \  
&& chown -R node-red:node-red /data  
  
USER node-red  
WORKDIR /node-red  
RUN npm install node-red@${NODE_RED_VERSION}  
  
VOLUME [ "/data" ]  
EXPOSE 1880  
WORKDIR /data  
  
ENTRYPOINT [ "/tini", "--", "/start.sh" ]

