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
libffi-dev && \  
apk add --no-cache --virtual=run-deps \  
bash \  
ca-certificates \  
python \  
py-libxml2 \  
py-lxml \  
nodejs \  
unrar \  
su-exec \  
git && \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl cheetah requirements cfscrape
&& \  
git clone --depth 1 https://github.com/SickRage/SickRage.git /opt/sickrage &&
\  
apk del --no-cache --purge \  
build-deps && \  
rm -rf /opt/sickrage/.git* \  
/tmp/* \  
/var/cache/apk/* \  
/var/tmp/*  
  
### Volume  
VOLUME ["/config", "/downloads", "/tv", "/animes"]  
  
### Expose ports  
EXPOSE 8081  
  
### Running User: not used, managed by docker-entrypoint.sh  
#USER sickrage  
### Start Sickrage  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["sickrage"]  

