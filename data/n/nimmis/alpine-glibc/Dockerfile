FROM nimmis/alpine-micro:3.6  
MAINTAINER nimmis <kjell.havneskold@gmail.com>  
  
ENV GLIBC_VERSION=2.26-r0  
  
RUN apk update && apk upgrade && \  
  
# Make info file about this build  
mkdir -p /etc/BUILDS/ && \  
printf "Build of nimmis/alpine-glibc:3.5, date: %s\n" `date -u
+"%Y-%m-%dT%H:%M:%SZ"` > /etc/BUILDS/alpine-glibc && \  
  
# add curl for download  
apk add curl && \  
  
# download packages for glibc, see https://github.com/sgerrand/alpine-pkg-
glibc for more info  
curl -L -o glibc-${GLIBC_VERSION}.apk \  
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \  
curl -L -o glibc-bin-${GLIBC_VERSION}.apk \  
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" && \  
  
# install them  
apk add \--allow-untrusted glibc-${GLIBC_VERSION}.apk glibc-
bin-${GLIBC_VERSION}.apk && \  
  
# remove curl  
apk del curl && \  
  
# remove cache and downloaded files  
rm -fr glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk
/var/cache/apk/*  
  

