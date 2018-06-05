FROM alpine:3.6  
MAINTAINER mzyy94 <mizuyuu0904@gmail.com>  
  
ENV DOCKER="YES"  
  
ARG REPOSITORY="git://github.com/Chinachu/Chinachu.git"  
ARG BRANCH="gamma"  
  
ARG WORK_DIR="/usr/local/chinachu"  
  
ARG USER_NAME="chinachu"  
ARG USER_ID="1000"  
  
RUN set -x \  
&& apk upgrade --update \  
&& apk add \  
bash \  
'nodejs>=6.2.0' \  
nodejs-npm \  
coreutils \  
curl \  
procps \  
ca-certificates \  
\  
&& apk add --virtual .build-deps \  
git \  
make \  
gcc \  
g++ \  
autoconf \  
automake \  
wget \  
curl \  
sudo \  
tar \  
xz \  
libc-dev \  
musl-dev \  
eudev-dev \  
libevent-dev \  
\  
&& adduser -D -u ${USER_ID} -h ${WORK_DIR} chinachu \  
&& mkdir -p ${WORK_DIR} \  
&& git clone ${REPOSITORY} ${WORK_DIR} \  
&& chown -R ${USER_NAME} ${WORK_DIR} \  
&& cd ${WORK_DIR} \  
&& git checkout ${BRANCH} \  
&& echo 1 | sudo -u ${USER_NAME} ./chinachu installer \  
&& ./chinachu service operator initscript | sudo -u ${USER_NAME} tee
/tmp/chinachu-operator \  
&& ./chinachu service wui initscript | sudo -u ${USER_NAME} tee /tmp/chinachu-
wui \  
&& sudo -u ${USER_NAME} mkdir log \  
\  
&& sudo -u ${USER_NAME} mkdir conf \  
&& sudo -u ${USER_NAME} ln -s ${WORK_DIR}/conf/config.json ./config.json \  
&& sudo -u ${USER_NAME} ln -s ${WORK_DIR}/conf/rules.json ./rules.json \  
\  
&& chown root. /tmp/chinachu-operator /tmp/chinachu-wui \  
&& chmod u+x /tmp/chinachu-operator /tmp/chinachu-wui \  
&& mv /tmp/chinachu-operator /etc/init.d/ \  
&& mv /tmp/chinachu-wui /etc/init.d/ \  
\  
# cleaning  
&& cd / \  
&& apk del --purge .build-deps \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
# forward request and error logs to docker log collector  
#&& ln -sf /dev/stdout ${WORK_DIR}/log/operator \  
#&& ln -sf /dev/stdout ${WORK_DIR}/log/scheduler \  
#&& ln -sf /dev/stdout ${WORK_DIR}/log/wui  
  
WORKDIR ${WORK_DIR}  
COPY services.sh /usr/local/bin  
COPY config.sample.json ${WORK_DIR}  
  
CMD ["/usr/local/bin/services.sh"]  
EXPOSE 10772 20772 5353  

