# Dockerfile for yeoman  
FROM uwegerdes/nodejs  
MAINTAINER Uwe Gerdes <entwicklung@uwegerdes.de>  
  
USER root  
  
COPY . ${APP_HOME}/  
  
WORKDIR ${NODE_HOME}  
  
COPY package.json ${NODE_HOME}/  
  
RUN npm install -g \  
eslint \  
eslint-config-xo-space \  
jest \  
yo && \  
npm install && \  
chown -R ${USER_NAME}:${USER_NAME} ${NODE_HOME}  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
USER ${USER_NAME}  
  
WORKDIR ${APP_HOME}  
  
CMD bash  

