FROM comptel/docker-alpine-base  
  
ENV MONGODB_VERSION 3.2.12  
ENV AUTH yes  
ENV STORAGE_ENGINE wiredTiger  
ENV JOURNALING yes  
  
ARG ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download"  
ARG ALPINE_GLIBC_PACKAGE_VERSION="2.25-r0"  
ARG
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"  
ARG ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk"  
ARG
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"  
# Instal glibc for alpine  
RUN apk add --no-cache --virtual=.build-dependencies wget && \  
wget \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
apk del glibc-i18n && \  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
# Install mongos  
RUN cd /tmp && \  
curl -SLo- https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-${MONGODB_VERSION}.tgz | \  
tar xz && \  
mv mongodb-linux-x86_64-${MONGODB_VERSION}/bin/* /usr/local/bin/ && \  
mkdir -p /data/db  
  
COPY *.sh /usr/local/bin/  
  
RUN chmod -R +x /usr/local/bin/*.sh && \  
mv /usr/local/bin/cmd.sh /usr/local/bin/cmd  
  
VOLUME /data/db  
EXPOSE 27017 28017  
ENTRYPOINT ["/entrypoint.sh", "cmd"]  
CMD [ "/bin/bash" ]  

