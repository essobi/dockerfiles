FROM simplexsys/busybox-zulu-openjdk:latest  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
ENV VERTX_VERSION 2.1.5  
RUN (curl -L
https://bintray.com/artifact/download/vertx/downloads/vert.x-${VERTX_VERSION}.zip
-o /tmp/vertx.zip &&\  
unzip -q /tmp/vertx.zip -d /opt &&\  
rm /tmp/vertx.zip)  
RUN ln -s /opt/vert.x-${VERTX_VERSION} /opt/vertx  
  
VOLUME /opt/vertx/mods  
VOLUME /opt/vertx/sys-mods  
EXPOSE 8080  
ENTRYPOINT ["/opt/vertx/bin/vertx"]  

