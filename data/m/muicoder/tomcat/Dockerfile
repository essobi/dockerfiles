FROM muicoder/glibc:server-jre  
  
ARG TOMCAT_VERSION=8.0.42  
ARG WORK=/opt  
  
ENV CATALINA_HOME=$WORK/tomcat  
ENV CATALINA_OUT=/dev/null  
  
ENV PATH=$CATALINA_HOME/bin:$PATH  
  
SHELL ["bash", "-c"]  
RUN apk add --no-cache pwgen && \  
curl -jksSL
http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_VERSION:0:1}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz | tar -xzf - -C $WORK && \  
ln -s $WORK/apache-tomcat-$TOMCAT_VERSION $CATALINA_HOME && \  
curl -fsSL https://github.com/muicoder/tomcat/raw/master/entrypoint.sh -o
/sbin/entrypoint.sh && \  
chmod +x /sbin/*  
  
WORKDIR $CATALINA_HOME  
VOLUME $CATALINA_HOME/logs  
EXPOSE 8080 8443 8009  
ENTRYPOINT ["tini", "-s", "--", "entrypoint.sh"]  
CMD ["catalina.sh", "run"]  

