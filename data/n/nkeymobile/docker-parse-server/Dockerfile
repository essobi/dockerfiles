FROM node:5  
ENV PARSE_HOME /parse  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git openssh-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY package.json ${PARSE_HOME}/  
COPY jsconfig.json ${PARSE_HOME}/  
  
ENV CLOUD_CODE_HOME ${PARSE_HOME}/cloud  
COPY cloud/cloud/ $CLOUD_CODE_HOME/cloud/  
  
WORKDIR $PARSE_HOME  
RUN npm install  
  
COPY index.js ${PARSE_HOME}/  
  
## ENV  
ENV PORT 1337  
EXPOSE $PORT  
VOLUME $CLOUD_CODE_HOME  
ENV NODE_PATH .  
  
CMD ["npm", "start"]  

