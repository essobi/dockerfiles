# Alpine Linux standard image  
FROM alpine:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.geeplus.description="alpine standard image" \  
com.geeplus.role="baseimage"  
  
ENV S6OVERLAY_VERSION="v1.11.0.1"  
ENV S6OVERLAY_URL="https://github.com/just-
containers/s6-overlay/releases/download/${S6OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz"  
ENV ENTRYKIT_VERSION=0.4.0  
ENV ENTRYKIT_FILE=entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz  
ENV
ENTRYKIT_DOWNLOAD=https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/${ENTRYKIT_FILE}  
  
ENV GOSU_VERSION=1.7  
ENV
GOSU_DOWNLOAD=https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64  
  
ENV PACKAGE='bash python ca-certificates' \  
BUILDPACK='build-base musl-dev linux-headers' \  
PATH=$PATH \  
LANG=C.UTF-8 \  
WORKDIR=/home/admin  
  
# admin user  
RUN adduser -D -h /home/admin -s /bin/bash admin admin  
  
# package install & update  
RUN apk update --no-cache && apk add ${PACKAGE} \--no-cache && apk add
${BUILDPACK} \--no-cache -t buildpack  
  
# s6-overlay  
ADD ${S6OVERLAY_URL} /tmp/  
  
# entrykit install  
ADD ${ENTRYKIT_DOWNLOAD} /tmp/  
RUN tar zxf /tmp/${ENTRYKIT_FILE} -C /usr/bin && \  
chmod +x /usr/bin/entrykit && /usr/bin/entrykit --symlink  
  
# gosu  
ADD ${GOSU_DOWNLOAD} /usr/bin/  
RUN chmod +x /usr/bin/gosu-amd64 && ln -s /usr/bin/gosu-amd64 /usr/bin/gosu  
  
# s6-overlay  
RUN tar zxf /tmp/s6-overlay-amd64.tar.gz -C /  
  
# pre installed package remove  
RUN apk del buildpack --no-cache && rm -rf /tmp/* /var/cache/apk/*  
  
WORKDIR ${WORKDIR}  
ENTRYPOINT ["switch","shell=/bin/sh","--","/init"]  
CMD ["/bin/bash"]  

