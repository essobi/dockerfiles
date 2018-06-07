FROM alpine:3.6  
LABEL maintainer "DI GREGORIO Nicolas <nicolas.digregorio@gmail.com>"  
  
### Environment variables  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
### Install Application  
RUN apk --no-cache upgrade && \  
apk add --no-cache --virtual=build-deps \  
make \  
gcc \  
g++ \  
python-dev \  
py2-pip \  
libressl-dev \  
libffi-dev \  
&& \  
apk add --no-cache --virtual=run-deps \  
ca-certificates \  
python \  
py-libxml2 \  
py-lxml \  
unrar \  
su-exec \  
git \  
bash \  
&& \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl && \  
git clone --depth 1 https://github.com/CouchPotato/CouchPotatoServer/
/opt/couchpotato && \  
apk del --no-cache --purge \  
build-deps && \  
rm -rf /opt/couchpotato/.git* \  
/tmp/* \  
/var/cache/apk/* \  
/var/tmp/*  
  
### Volume  
VOLUME ["/config", "/downloads", "/movies"]  
  
### Expose ports  
EXPOSE 5050  
### Running User: not used, managed by docker-entrypoint.sh  
#USER couchpotato  
WORKDIR /opt/couchpotato  
  
### Start CouchPotato  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["couchpotato"]  

