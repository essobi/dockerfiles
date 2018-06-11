# alpine linux with embulk-digdag  
from youske/alpine-java:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
ENV DIGDAG_VERSION=latest \  
EMBULK_VERSION=latest \  
INSTALL_DIR=/opt/bin  
  
ENV PATH=${INSTALL_DIR}:$PATH  
  
RUN mkdir -p /opt/bin  
  
# digdag setup  
ADD https://dl.digdag.io/digdag-${DIGDAG_VERSION} ${INSTALL_DIR}/digdag  
RUN chmod 755 ${INSTALL_DIR}/digdag  
  
# embulk setup  
ADD http://dl.embulk.org/embulk-${EMBULK_VERSION}.jar" ${INSTALL_DIR}/embulk  
RUN chmod 755 ${INSTALL_DIR}/embulk  
  
ENTRYPOINT ["switch","shell=gosu admin
/bin/bash","\--","switch","root=/bin/bash","\--","/init"]  
CMD ["gosu","admin","/bin/bash"]  

