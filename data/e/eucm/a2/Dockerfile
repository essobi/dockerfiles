FROM node:8.5.0  
  
ENV USER_NAME="user" \  
WORK_DIR="/app"  
# setup user, group and workdir  
COPY ./ ${WORK_DIR}/  
RUN groupadd -r ${USER_NAME} \  
&& useradd -r -d ${WORK_DIR} -g ${USER_NAME} ${USER_NAME} \  
&& chown -R ${USER_NAME}:${USER_NAME} ${WORK_DIR} \  
&& npm install -g bower  
ENV HOME=${WORK_DIR}  
USER ${USER_NAME}  
WORKDIR ${WORK_DIR}  
# get dependencies sorted out  
RUN npm install \  
&& bower install  
  
# configure & gen apidoc  
RUN npm run fast-setup \  
&& npm run gen-apidoc  
  
# expose & run  
EXPOSE 3000  
CMD [ "npm", "run", "docker-start" ]  
  
# EXPECTS: Mongo at 27017, Redis at 6379  

