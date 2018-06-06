FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
ARG KHIPU_HOME=/opt/khipu  
ENV KHIPU_HOME ${KHIPU_HOME}  
  
ONBUILD ARG PROJECT_NAME  
ONBUILD ARG PROJECT_VERSION  
ONBUILD ENV PROJECT_NAME ${PROJECT_NAME}  
ONBUILD ENV PROJECT_VERSION ${PROJECT_VERSION}  
  
ONBUILD LABEL name=${PROJECT_NAME}  
ONBUILD LABEL version=${PROJECT_VERSION}  
  
RUN apk -U add openjdk8 \  
&& rm -rf /var/cache/apk/*  
  
# jvm fixes  
RUN sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \  
&& sed -i
's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g'
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security  
  
COPY entrypoint.sh /  
COPY docker/confd ${KHIPU_HOME}/etc/confd  
COPY docker/zorka/scripts ${KHIPU_HOME}/var/${PROJECT_NAME}/zorka/scripts  
  
ONBUILD RUN mkdir -p ${KHIPU_HOME}/etc/${PROJECT_NAME}
${KHIPU_HOME}/var/${PROJECT_NAME}/zorka/log \  
&& mkdir -p ${KHIPU_HOME}/share/${PROJECT_NAME}/ \  
&& chown -R khipu:khipu ${KHIPU_HOME}/  
  
ONBUILD COPY docker/confd ${KHIPU_HOME}/etc/confd/  
ONBUILD COPY build/libs/${PROJECT_NAME}-capsule.jar
${KHIPU_HOME}/share/${PROJECT_NAME}/  
  
ONBUILD ENTRYPOINT ["/entrypoint.sh"]  

