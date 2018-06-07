FROM nginx:alpine  
LABEL maintainer="ninhpham@hotmail.com"  
  
ARG VERSION="0.4.0"  
LABEL build_version="AriaNg version: ${VERSION}"  
  
RUN set -xe && \  
apk add --no-cache unzip wget && \  
wget -N --no-check-certificate
https://github.com/mayswind/AriaNg/releases/download/${VERSION}/aria-
ng-${VERSION}.zip && \  
unzip -o aria-ng-${VERSION}.zip -d /usr/share/nginx/html && \  
rm -rf aria-ng-${VERSION}.zip && \  
apk del unzip wget

