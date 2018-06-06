FROM node:6  
# Home directory for Node-RED application source code.  
RUN mkdir -p /usr/src/node-red  
# User data directory, contains flows, config and nodes.  
RUN mkdir /data  
  
WORKDIR /usr/src/node-red  
# Add node-red user so we aren't running as root.  
RUN useradd --home-dir /usr/src/node-red \--no-create-home node-red \  
&& chown -R node-red:node-red /data \  
&& chown -R node-red:node-red /usr/src/node-red  
USER node-red  
# COPY node-red settings  
COPY BEF-server /usr/src/node-red/BEF-server  
COPY BEF-UI /usr/src/node-red/BEF-UI  
COPY HTML /usr/src/node-red/HTML  
COPY package.json /usr/src/node-red/  
COPY app.js /usr/src/node-red/  
  
# create symbolic links for User SSL Certs  
#RUN ln -s /bef/nodered/client-ssl/user_cert.pem /usr/src/node-
red/user_cert.pem  
#RUN ln -s /bef/nodered/client-ssl/user_key.pem /usr/src/node-red/user_key.pem  
#RUN ln -s /bef/nodered/client-ssl/user_ca.pem /usr/src/node-red/user_ca.pem  
# COPY default flows.json  
COPY flows.json /usr/src/node-red/  
  
# COPY node-red modules (core changed)  
COPY node_modules /usr/src/node-red/node_modules  
  
USER root  
RUN chown -R node-red:node-red /usr/src/node-red  
USER node-red  
#RUN npm config set registry http://bef-dev-ci:8081/repository/npm-all  
RUN npm install  
  
# Environment variable holding file path for flows configuration  
ENV FLOWS=flows.json  
#ENV FEATURE_SERVICE=http://50.1.111.54:8060  
# User configuration directory volume  
EXPOSE 1880  
  
CMD ["npm", "start"]  
  

