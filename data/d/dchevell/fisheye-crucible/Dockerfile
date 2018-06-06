FROM openjdk:8-jdk-alpine  
MAINTAINER Dave Chevell  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
# https://confluence.atlassian.com/fisheye/fisheye-folder-
layout-298976940.html  
ENV FISHEYE_INST /var/atlassian/application-data/fecru  
ENV FISHEYE_HOME /opt/atlassian/fecru  
  
VOLUME ["${FISHEYE_INST}"]  
  
# Expose HTTP port  
EXPOSE 8060  
WORKDIR $FISHEYE_INST  
  
CMD ["/entrypoint.sh", "run"]  
ENTRYPOINT ["/sbin/tini", "--"]  
  
RUN apk update -qq \  
&& update-ca-certificates \  
&& apk add ca-certificates wget curl git openssh bash procps openssl perl ttf-
dejavu tini \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ARG FECRU_VERSION=4.4.6  
ARG
DOWNLOAD_URL=https://www.atlassian.com/software/fisheye/downloads/binary/fisheye-${FECRU_VERSION}.zip  
COPY . /tmp  
  
RUN mkdir -p /opt/atlassian \  
&& wget -nv $DOWNLOAD_URL \  
&& unzip -q fisheye-${FECRU_VERSION}.zip \  
&& rm fisheye-${FECRU_VERSION}.zip \  
&& mv fecru-${FECRU_VERSION} ${FISHEYE_HOME} \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${FISHEYE_HOME}/

