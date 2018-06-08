FROM anapsix/alpine-java:8u144b01_server-jre  
MAINTAINER Martin Hoffesommer <3dcoder@gmail.com>  
  
# environment  
ENV SCM_VERSION 1.56  
ENV SCM_PKG_URL https://maven.scm-
manager.org/nexus/content/repositories/releases/sonia/scm/scm-
server/${SCM_VERSION}/scm-server-${SCM_VERSION}-app.tar.gz  
ENV SCM_HOME /var/lib/scm  
  
RUN apk add --update curl mercurial \  
&& apk add nano \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt && curl -Lks "$SCM_PKG_URL" | tar -zxC /opt \  
&& adduser -D -h /opt/scm-server -s /bin/bash scm \  
&& chown -R scm:scm /opt/scm-server \  
&& chmod +x /opt/scm-server/bin/scm-server \  
&& mkdir -p $SCM_HOME \  
&& chown -R scm:scm $SCM_HOME  
  
WORKDIR $SCM_HOME  
VOLUME $SCM_HOME  
EXPOSE 8080  
COPY ./docker-entrypoint.sh /  
COPY ./users.xml.template /opt/scm-server/  
  
RUN chmod +x /docker-entrypoint.sh  
  
USER scm  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/opt/scm-server/bin/scm-server"]  

