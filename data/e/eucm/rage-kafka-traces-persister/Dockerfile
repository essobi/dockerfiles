FROM node  
  
ENV USER_NAME="user" \  
WORK_DIR="/app"  
# setup user, group and workdir  
COPY ./ ${WORK_DIR}/  
RUN groupadd -r ${USER_NAME} \  
&& useradd -r -d ${WORK_DIR} -g ${USER_NAME} ${USER_NAME} \  
&& chown ${USER_NAME}:${USER_NAME} -R ${WORK_DIR}  
ENV HOME=${WORK_DIR}  
USER ${USER_NAME}  
WORKDIR ${WORK_DIR}  
# get dependencies sorted out  
RUN npm install  
  
# configure & gen apidoc  
RUN npm run fast-setup  
  
# run  
EXPOSE 3003  
CMD [ "npm", "run", "docker-start" ]  
  
# EXPECTS: mongo at 27017  
# EXPECTS: kafka at 2181

