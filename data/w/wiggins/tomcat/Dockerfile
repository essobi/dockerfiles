from wiggins/jdk:jdk8u151  
MAINTAINER wiggins  
  
ENV VERSION 8.0.48  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_HOME=/data/tomcat  
ENV
DOWN_URL="http://mirror.rise.ph/apache/tomcat/tomcat-${TOMCAT_MAJOR}/v${VERSION}/bin/apache-
tomcat-${VERSION}.tar.gz"  
#ENV FILENAME=${DOWN_URL##*/}  
#ENV TOMCAT_NAME=${FILENAME%.tar*}  
#ENV SHACHK d2446c127c9b11f88def11e542af98998071d91d  
RUN set -x && \  
FILENAME=${DOWN_URL##*/} && \  
TOMCAT_NAME=${FILENAME%.tar*} && \  
mkdir -p $(dirname ${TOMCAT_HOME}) && cd $(dirname ${TOMCAT_HOME}) && \  
curl -Lk ${DOWN_URL} | tar xz && \  
mv ${TOMCAT_NAME} ${TOMCAT_HOME}  
  
EXPOSE 8080  
#ADD etc /etc  
#ADD entrypoint.sh /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  
CMD /data/tomcat/bin/startup.sh  

