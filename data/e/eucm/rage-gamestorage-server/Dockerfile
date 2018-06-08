FROM node  
  
ENV USER_NAME="user" \  
WORK_DIR="/app"  
# setup sources, user, group and workdir  
COPY ./ ${WORK_DIR}/  
RUN groupadd -r ${USER_NAME} \  
&& useradd -r -d ${WORK_DIR} -g ${USER_NAME} ${USER_NAME} \  
&& chown -R ${USER_NAME}:${USER_NAME} ${WORK_DIR}  
ENV HOME=${WORK_DIR}  
USER ${USER_NAME}  
WORKDIR ${WORK_DIR}  
# get dependencies sorted out  
RUN npm install  
  
# gen apidocumentation  
RUN npm run gen-apidoc  
  
# expose & run  
EXPOSE 3400  
CMD [ "npm", "run", "docker-start" ]  
  
# EXPECTS: a2 at 3000, mongo at 27017

