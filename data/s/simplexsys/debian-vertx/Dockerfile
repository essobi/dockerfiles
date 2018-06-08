FROM simplexsys/debian-zulu-jdk:latest  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
ENV VERTX_VERSION 2.1.5  
  
RUN (curl -L
https://bintray.com/artifact/download/vertx/downloads/vert.x-${VERTX_VERSION}.tar.gz
-o /tmp/vertx.tar.gz &&\  
gunzip < /tmp/vertx.tar.gz | tar xvf - -C /usr/share &&\  
rm /tmp/vertx.tar.gz)  
RUN mkdir /usr/lib/vertx &&\  
ln -s /usr/share/vert.x-${VERTX_VERSION} /usr/share/vertx &&\  
mkdir /usr/share/vertx/mods &&\  
ln -s /usr/share/vertx/mods /usr/lib/vertx/mods &&\  
mkdir /usr/share/vertx/sys-mods &&\  
ln -s /usr/share/vertx/sys-mods /usr/lib/vertx/sys-mods &&\  
ln -s /usr/share/vertx/conf /etc/vertx &&\  
ln -s /usr/share/vertx/bin/vertx /usr/bin/vertx  
  
VOLUME ["/etc/vertx", "/usr/lib/vertx/mods", "/usr/lib/vertx/sys-mods"]  
EXPOSE 8080  
  
WORKDIR /usr/share/vertx  
ENTRYPOINT ["/usr/share/vertx/bin/vertx"]  

