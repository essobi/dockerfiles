FROM python:3-alpine  
WORKDIR /root  
RUN mkdir build  
COPY electrum-key.asc build  
RUN { set -ex; \  
cd build; \  
apk update; \  
apk add --no-cache --virtual .build-deps gnupg curl; \  
apk add --no-cache jq; \  
gpg --import < electrum-key.asc; \  
curl -sO https://download.electrum.org/3.0.2/Electrum-3.0.2.tar.gz.asc; \  
curl -sO https://download.electrum.org/3.0.2/Electrum-3.0.2.tar.gz; \  
gpg --verify Electrum-3.0.2.tar.gz.asc; \  
pip3 install --no-cache Electrum-3.0.2.tar.gz; \  
apk del .build-deps; \  
cd .. ; \  
rm -rf build .gnupg .cache; \  
}  
  
CMD /bin/sh

