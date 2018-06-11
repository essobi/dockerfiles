FROM alpine:3.7 as build  
  
ENV VERSION 0.6.0  
RUN apk --update add \  
bash \  
curl \  
git \  
g++ \  
make \  
openssh \  
openssl \  
openssl-dev  
  
RUN curl -L https://github.com/AGWA/git-crypt/archive/$VERSION.tar.gz | tar
zxv -C /tmp && \  
cd /tmp/git-crypt-$VERSION && \  
make && \  
make install PREFIX=/usr/local  
  
FROM alpine:3.7  
MAINTAINER Gabriel Melillo <gabriel@melillo.me>  
  
COPY \--from=build /usr/local/bin/git-crypt /usr/local/bin/  
COPY \--from=build /lib/libcrypto* /lib/  
COPY \--from=build /usr/lib/libgcc_s* /usr/lib/  
COPY \--from=build /usr/lib/libstdc++.* /usr/lib/  
  
COPY git-crypt-entrypoint.sh /git-crypt-entrypoint.sh  
  
RUN apk --no-cache add \  
git \  
gnupg && \  
rm -rf /var/cache/apk/* && \  
adduser -D git && \  
chmod +x /git-crypt-entrypoint.sh  
  
USER git  
WORKDIR /home/git  
  
VOLUME /home/git  
  
ENTRYPOINT ["/git-crypt-entrypoint.sh"]  
CMD ["/usr/local/bin/git-crypt"]  

