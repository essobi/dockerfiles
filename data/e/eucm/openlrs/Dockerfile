FROM maven  
  
ENV USER_NAME="user" \  
WORK_DIR="/app"  
# setup user, group and workdir  
COPY ./ ${WORK_DIR}/  
RUN groupadd -r ${USER_NAME} \  
&& useradd -r -d ${WORK_DIR} -g ${USER_NAME} ${USER_NAME} \  
&& chown -R ${USER_NAME}:${USER_NAME} ${WORK_DIR}  
USER ${USER_NAME}  
ENV HOME=${WORK_DIR}  
WORKDIR ${WORK_DIR}  
# get dependencies sorted out  
# running tests would require Redis, ElasticSearch up and running  
RUN mvn -Dmaven.test.skip=true package  
  
# expose & run (may lookup env. variables to make links work)  
EXPOSE 8080  
CMD [ "./run.sh" ]  
  
# EXPECTS: ElasticSearch at 9300, Redis at 6379 (see run.sh)  

