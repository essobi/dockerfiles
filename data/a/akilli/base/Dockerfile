FROM scratch  
  
LABEL maintainer="Ayhan Akilli"  
  
#  
# Build variables  
#  
ARG ID=1000  
ARG LANG=de_DE.UTF-8  
ARG TZ=Europe/Berlin  
  
#  
# Environment variables  
#  
ENV LANG=$LANG  
  
#  
# Setup  
#  
ADD rootfs.tar.xz /  
  
RUN addgroup -g $ID app && \  
adduser -u $ID -G app -s /bin/ash -D app && \  
mkdir \  
/app \  
/data \  
/var/log/app && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --no-cache add \  
su-exec \  
tini \  
tzdata && \  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
apk del \  
tzdata  
  
#  
# Command  
#  
COPY app-entry.sh /usr/local/bin/app-entry  
  
ENTRYPOINT ["tini", "--", "app-entry"]  
CMD ["ash"]  

