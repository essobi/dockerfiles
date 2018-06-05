FROM alpine:latest  
MAINTAINER ClusterboxCloud <clusterbox@clusterboxcloud.com>  
  
# global environment settings  
ENV RCLONE_VERSION="current"  
ENV PLATFORM_ARCH="amd64"  
# s6 environment settings  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
ENV S6_KEEP_ENV=1  
# install packages  
RUN \  
apk update && \  
apk add --no-cache \  
ca-certificates  
  
# Install Node.js  
RUN apk add --update nodejs nodejs-npm && npm install npm@latest -g  
  
# Install CURL  
RUN apk add --update curl  
  
# Install CURL  
RUN apk add --update nano  
  
# Install Bash  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
# install build packages  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
wget \  
curl \  
unzip && \  
  
cd tmp && \  
wget -q
http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip
&& \  
unzip /tmp/rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip && \  
mv /tmp/rclone-*-linux-${PLATFORM_ARCH}/rclone /usr/bin && \  
  
apk add \--no-cache --repository
http://nl.alpinelinux.org/alpine/edge/community \  
shadow && \  
  
# cleanup  
apk del --purge \  
build-dependencies && \  
rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/cache/apk/*  
  
# create abc user  
RUN \  
mkdir -p /config /app /defaults /data && \  
touch /var/lock/rclone.lock  
  
# add local files  
COPY root/ /  
  
# Install express.js  
RUN npm install  
  
VOLUME ["/config"]  
  
EXPOSE 8080  
#ENTRYPOINT ["/init"]  
CMD ["node", "server.js"]

