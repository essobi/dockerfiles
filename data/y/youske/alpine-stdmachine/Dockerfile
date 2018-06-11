# Alpine Linux standard base image  
FROM alpine:3.4  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.stdmachine.description="alpine standard image" \  
com.stdmachine.vendor="stdmachine" \  
com.stdmachine.role="baseimage"  
  
ENV LC_ALL=C.UTF-8 \  
LANG=ja_JP.UTF-8 \  
TZ=Asia/Tokyo \  
WORK_DIR=/workdir  
ENV LANGUAGE=${LANG}  
  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
# timezone settings  
apk --update add tzdata && \  
cp /usr/share/zoneinfo/${TZ} /etc/localtime && echo $TZ > /etc/timezone && \  
apk del tzdata && \  
# package install & update  
apk update upgrade --no-cache && \  
apk add bash wget ca-certificates ncurses gawk --no-cache && \  
# entrykit install  
ENTRYKIT_VERSION='0.4.0' && \  
ENTRYKIT_FILE=entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz && \  
wget -q -nc
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/${ENTRYKIT_FILE}
-P /tmp/ && \  
tar zxf /tmp/${ENTRYKIT_FILE} -C /usr/bin && \  
chmod +x /usr/bin/entrykit && /usr/bin/entrykit --symlink && \  
# gosu install  
GOSU_VERSION='1.10' && \  
wget -q -nc
https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 -P
/usr/bin/ && \  
chmod +x /usr/bin/gosu-amd64 && ln -s /usr/bin/gosu-amd64 /usr/bin/gosu && \  
#S6OVERLAY install  
S6OVERLAY_VERSION='v1.18.1.5' && \  
wget -q -nc https://github.com/just-
containers/s6-overlay/releases/download/${S6OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz -P /tmp/ && \  
tar zxf /tmp/s6-overlay-amd64.tar.gz -C / && \  
# pre installed package remove  
rm -rf /tmp/* /var/cache/apk/* /root/.wget-hsts && \  
# admin user & work  
adduser -D -h /home/admin -s /bin/bash admin admin && \  
mkdir -p ${WORK_DIR} && chmod 777 ${WORK_DIR} && chown -R admin:admin
${WORK_DIR}  
  
WORKDIR ${WORK_DIR}  
ENTRYPOINT ["switch","shell=gosu admin
/bin/bash","--","switch","root=/bin/bash","--","/init"]  
CMD ["gosu","admin","/bin/bash"]  

