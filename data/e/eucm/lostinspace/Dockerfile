FROM maven  
  
ENV USER_NAME="user" \  
WORK_DIR="/app"  
# setup user, group and workdir  
COPY ./ ${WORK_DIR}/  
  
RUN groupadd -r ${USER_NAME} \  
&& useradd -r -d ${WORK_DIR} -g ${USER_NAME} ${USER_NAME} \  
&& chown -R ${USER_NAME}:${USER_NAME} ${WORK_DIR}  
  
ENV HOME=${WORK_DIR}  
USER ${USER_NAME}  
WORKDIR ${WORK_DIR}  
  
# install a pesky dependency into the m2 cache  
RUN mkdir xt \  
&& cd xt \  
&& git clone \--single-branch https://github.com/e-ucm/xmltools . \  
&& mvn install \  
&& rm -rf ../xt  
  
# get (others) dependencies sorted out, and compile everything  
RUN mvn install -P html,-default  
  
# expose & run  
EXPOSE 9090  
CMD [ "mvn", "-Djetty.port=9090", "install", "-P", "html,jetty" ]  
  
# access via ip:9090/setup  

