FROM azul/zulu-openjdk-alpine:8  
LABEL maintainer="thanhbv@sandinh.net"  
  
ARG APP_VERSION=2017.3  
ARG APP_BUILD=2593  
# preparing user+group  
RUN apk add --no-cache --update-cache --repository="http://dl-
cdn.alpinelinux.org/alpine/edge/community/" \  
shadow ca-certificates openssl && \  
useradd --system --user-group --uid 500 upsource && \  
# downloading build dependencies,  
# downloading and unpacking the distribution, changing file permissions,
removing bundled JVMs,  
# removing build dependencies  
apk add -q --no-cache --virtual .build-deps wget unzip && \  
mkdir -p /opt && cd /opt && \  
wget -qO upsource.zip
https://download.jetbrains.com/upsource/upsource-${APP_VERSION}.${APP_BUILD}.zip
&& \  
unzip -q upsource.zip -x */internal/java/* */apps/hub/* && \  
mv upsource-${APP_VERSION}.${APP_BUILD} upsource && \  
chown -R upsource:upsource /opt/upsource && \  
rm upsource.zip && \  
apk del .build-deps  
  
USER upsource  
WORKDIR /opt/upsource  
  
EXPOSE 8080  
ENTRYPOINT ["bin/upsource.sh"]  
CMD ["run"]  

