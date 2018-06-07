FROM domecloud/openresty:edge  
MAINTAINER Dome C. <dome@tel.co.th>  
  
RUN \  
apk update \  
&& apk upgrade \  
&& apk add \--no-cache bash --virtual=.build-dependencies wget ca-certificates  
  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
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
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
RUN apk add --update alpine-sdk \  
&& apk add --update perl \  
&& apk add --update libssl1.0  
WORKDIR /root  
RUN git clone https://github.com/wg/wrk.git  
WORKDIR /root/wrk  
RUN make \  
&& mv /root/wrk/wrk /usr/local/bin \  
&& rm -rf /root/wrk \  
&& apk del --purge alpine-sdk \  
&& apk add libgcc drill  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
COPY bin/prometheus /bin/prometheus  
COPY bin/promtool /bin/promtool  
COPY bin/prometheus.yml /etc/prometheus/prometheus.yml  
COPY bin/console_libraries/ /etc/prometheus/  
COPY bin/consoles/ /etc/prometheus/  
  
WORKDIR /prometheus  
  
ENV TERM screen-256color  
ENV SHELL=/bin/bash  
EXPOSE 9090 80  
ENTRYPOINT ["/start.sh"]  

