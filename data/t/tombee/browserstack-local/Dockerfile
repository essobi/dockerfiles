FROM openjdk:8-jre-alpine  
LABEL maintainer="Tom Barlow <tomwbarlow@gmail.com>"  
  
RUN apk add --update \  
ca-certificates \  
openssl  
  
ENV GLIBC_VERSION 2.26-r0  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk" && \  
apk --no-cache add "glibc-$GLIBC_VERSION.apk" && \  
rm "glibc-$GLIBC_VERSION.apk" && \  
wget "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk" && \  
apk --no-cache add "glibc-bin-$GLIBC_VERSION.apk" && \  
rm "glibc-bin-$GLIBC_VERSION.apk" && \  
wget "https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC_VERSION/glibc-i18n-$GLIBC_VERSION.apk" && \  
apk --no-cache add "glibc-i18n-$GLIBC_VERSION.apk" && \  
rm "glibc-i18n-$GLIBC_VERSION.apk"  
  
RUN cd /usr/local/bin && \  
wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip && \  
unzip BrowserStackLocal-linux-x64.zip && \  
chmod +x BrowserStackLocal && \  
rm BrowserStackLocal-linux-x64.zip  
  
ENTRYPOINT ["/usr/local/bin/BrowserStackLocal"]  
CMD ["-h"]  

