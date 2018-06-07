FROM alpine:latest  
MAINTAINER Youngman <58945591@qq.com>  
LABEL description="JumpServer集成coco和luna,使用nginx进行反向代理,不包含数据库和队列管理,需要自行准备MySQL
Server或使用SQLite3."  
  
ARG APK_FLAGS_COMMON="-q"  
ARG APK_FLAGS_PERSISTANT="${APK_FLAGS_COMMON} --clean-protected --no-cache"  
ARG APK_FLAGS_DEV="${APK_FLAGS_COMMON} --no-cache"  
ARG COCO_VERSION="0.5-beta-2"  
RUN set -xe && \  
apk add ${APK_FLAGS_PERSISTANT} \  
tini \  
tzdata \  
sqlite \  
nginx \  
supervisor \  
python3 \  
openssh-client \  
sshpass && \  
mkdir /etc/supervisor.d && \  
rm -f /usr/bin/python && \  
ln -s /usr/bin/python3 /usr/bin/python  
  
RUN set -xe && \  
apk add ${APK_FLAGS_DEV} \--virtual .fetch-deps \  
ca-certificates \  
openssl \  
git && \  
apk add ${APK_FLAGS_DEV} \--virtual .build-deps \  
musl-dev \  
gcc \  
autoconf \  
make \  
python3-dev \  
mariadb-dev \  
libffi-dev \  
heimdal-dev \  
openldap-dev \  
jpeg-dev \  
freetype-dev \  
linux-headers &&\  
mkdir /opt && \  
cd /opt && \  
git clone \--depth=1 https://github.com/jumpserver/jumpserver.git && \  
cd jumpserver && \  
git checkout dev && \  
pip3 install -r requirements/requirements.txt && \  
cd /opt && \  
git clone https://github.com/jumpserver/coco.git && \  
cd coco && \  
git checkout dev && \  
cp conf_example.py conf.py && \  
mkdir keys && \  
pip3 install -r requirements/requirements.txt && \  
cd /opt && \  
wget -q
https://github.com/jumpserver/luna/releases/download/${COCO_VERSION}/luna.tar.gz
&& \  
tar xf luna.tar.gz && rm -f luna.tar.gz && \  
apk del ${APK_FLAGS_COMMON} \--purge .fetch-deps && \  
apk del ${APK_FLAGS_COMMON} \--purge .build-deps && \  
runDeps1="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" && \  
runDeps2="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/lib/python3.6 \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" && \  
apk add --no-cache --virtual .jms-rundeps1 $runDeps1 && \  
apk add --no-cache --virtual .jms-rundeps2 $runDeps2  
  
EXPOSE 80/tcp 2222/tcp 8080/tcp  
  
WORKDIR /opt/jumpserver  
  
COPY ./docker-entrypoint.sh /  
  
COPY ./jms.conf /etc/nginx/conf.d/  
  
COPY ./supervisord.conf /etc  
  
COPY ./config.py /opt/jumpserver/  
  
VOLUME ["/opt/jumpserver/logs","/opt/coco/logs"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

