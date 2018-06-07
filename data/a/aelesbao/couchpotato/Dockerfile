## -*- docker-image-name: "docker-couchpotato" -*-  
#  
# CouchPotato Dockerfile  
# https://github.com/aelesbao/docker-couchpotato  
#  
FROM alpine:3.6  
LABEL maintainer="Augusto Elesbao <https://github.com/aelesbao>"  
  
# Set python to use UTF-8 rather than AscII  
ENV PYTHONIOENCODING "UTF-8"  
WORKDIR /opt/couchpotato  
  
RUN addgroup couchpotato && adduser -G couchpotato -D -h /opt/couchpotato
couchpotato  
  
# Install run dependencies  
RUN apk add --no-cache --virtual .run-deps \  
git \  
unrar \  
su-exec \  
openssl \  
py2-pip \  
py2-lxml \  
py2-openssl \  
py2-parsing \  
py2-packaging  
  
# Install CouchPotato  
ARG git_ref="master"  
RUN set -ex \  
&& git clone \--depth 1 -b ${git_ref}
https://github.com/CouchPotato/CouchPotatoServer ./server \  
&& mkdir ./data ./downloads ./movies  
  
ENV PATH /opt/couchpotato/server:$PATH  
  
VOLUME ["/opt/couchpotato/data", "/opt/couchpotato/downloads",
"/opt/couchpotato/movies"]  
  
EXPOSE 5050  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["CouchPotato.py", "--console_log", "--data_dir", "./data"]  

