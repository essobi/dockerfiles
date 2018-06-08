FROM alpine:latest  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8"  
  
RUN GLIBC_VERSION="2.23-r3" && \  
  
apk \--no-cache add \--virtual .build-deps \  
wget \  
ca-certificates && \  
  
cd /tmp && \  
  
wget -nv -O /etc/apk/keys/sgerrand.rsa.pub https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub && \  
  
wget -nv https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk && \  
  
echo "823b54589c93b02497f1ba4dc622eaef9c813e6b0f0ebbb2f771e32adf9f4ef2
/etc/apk/keys/sgerrand.rsa.pub" > sgerrand && \  
sha256sum -c sgerrand && \  
echo "5b77a1bc456f486a31df0a3ce9dd8f7a442582680a0404a01edb4c78a030e835
glibc-2.23-r3.apk" > glibc-${GLIBC_VERSION} && \  
sha256sum -c glibc-${GLIBC_VERSION} && \  
echo "7b8dfbf027b4fc80137b18c620cad07618395725ae466bb5d66fee55d9e70c88 glibc-
bin-2.23-r3.apk" > glibc-bin-${GLIBC_VERSION} && \  
sha256sum -c glibc-bin-${GLIBC_VERSION} && \  
echo "a3f03beba1958b3699bedafab108ae73477e58cc4d9f8d9e446b1b6eb3bf26e4
glibc-i18n-2.23-r3.apk" > glibc-i18n-${GLIBC_VERSION} && \  
sha256sum -c glibc-i18n-${GLIBC_VERSION} && \  
  
apk \--no-cache add glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk
glibc-i18n-${GLIBC_VERSION}.apk && \  
/usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 && \  
echo "export LANG=en_US.UTF-8" > /etc/profile.d/locale.sh && \  
  
apk del glibc-bin glibc-i18n .build-deps && \  
  
rm -rvf /tmp/* /etc/apk/keys/sgerrand.rsa.pub /root/.wget-hsts  

