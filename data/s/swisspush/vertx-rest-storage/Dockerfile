FROM java:8  
MAINTAINER florian kammermann "florian@kammermann.me"  
ENV VERTX_VERSION 2.1.6  
RUN curl -sSL
https://bintray.com/artifact/download/vertx/downloads/vert.x-$VERTX_VERSION.tar.gz
| tar xzf - -C /usr/share/ && \  
mkdir /usr/share/vert.x-$VERTX_VERSION/sys-mods  
ENV PATH /usr/share/vert.x-$VERTX_VERSION/bin:$PATH  
  
ENV REST_STORAGE_VERSION 1.2.3  
RUN mkdir /usr/lib/vertx && \  
curl -sL http://search.maven.org/remotecontent?filepath=li/chee/vertx/rest-
storage/$REST_STORAGE_VERSION/rest-storage-$REST_STORAGE_VERSION-mod.zip -o
/usr/lib/vertx/rest-storage-mod.zip  
  
ENV MOD_REDIS_VERSION 1.1.3  
RUN mkdir /usr/share/vert.x-$VERTX_VERSION/sys-mods/io.vertx~mod-
redis~$MOD_REDIS_VERSION && \  
curl -sL http://search.maven.org/remotecontent?filepath=io/vertx/mod-
redis/$MOD_REDIS_VERSION/mod-redis-$MOD_REDIS_VERSION-mod.zip -o mod-redis-
mod.zip && \  
unzip mod-redis-mod.zip -d /usr/share/vert.x-$VERTX_VERSION/sys-
mods/io.vertx~mod-redis~$MOD_REDIS_VERSION && \  
rm mod-redis-mod.zip  
  
COPY redis-conf.json /usr/lib/vertx/rest-storage-redis-conf.json  
  
RUN useradd -ms /bin/bash reststorage  
USER reststorage  
WORKDIR /home/reststorage  
  
# the port where the rest-storage will listen on  
EXPOSE 8989  
CMD ["vertx", "runzip", "/usr/lib/vertx/rest-storage-mod.zip"]  

