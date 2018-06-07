FROM node:8  
RUN mkdir -p /usr/src/restya-orchestrator  
  
WORKDIR /usr/src/restya-orchestrator  
  
RUN npm i -g pm2 babel-cli  
  
COPY package.json /usr/src/restya-orchestrator  
  
RUN npm i  
  
COPY . /usr/src/restya-orchestrator  
  
ENV URL_RESTYA=http://cicd.develop.sinapse-ps.com:9006/api/v1  
ENV URL_JENKINS=http://cicd.develop.sinapse-ps.com:9000  
ENV JENKINS_TOKEN=iULsBPy6xs6ghaPE3rxY  
ENV JOB_NAME=board-create-feature  
ENV LOGIN=admin  
ENV PASSWORD=restya  
ENV ADMIN_ROLE_ID=1  
ENV URL_RANCHER=http://rancher-server.develop.sinapse-
ps.com:8080/v2-beta/projects/1a41455  
  
CMD npm run prod  

