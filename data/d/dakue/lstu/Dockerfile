FROM alpine:latest  
  
ENV LSTU_HOME=/lstu \  
ENVPLATE_VERSION=0.0.8  
RUN set -x && \  
apk add --update wget ca-certificates tar bash build-base perl perl-dev
openssl-dev libidn-dev && \  
mkdir -p $LSTU_HOME && \  
wget -nv "https://github.com/ldidry/lstu/tarball/master" -O- \  
| tar xz --strip-component=1 -C $LSTU_HOME && \  
echo | cpan && \  
cpan install Carton && \  
cd $LSTU_HOME && \  
carton install && \  
apk del wget ca-certificates tar build-base perl-dev openssl-dev libidn-dev &&
\  
apk add libidn openssl && \  
rm -rf /root/.cpan && \  
rm -rf /root/.cpanm && \  
rm /var/cache/apk/*  
  
RUN set -x && \  
apk add --update curl ca-certificates && \  
curl -sSL
"https://github.com/kreuzwerker/envplate/releases/download/v${ENVPLATE_VERSION}/ep-
linux" -o /usr/local/bin/ep && \  
chmod +x /usr/local/bin/ep && \  
ln -s /usr/local/bin/ep /usr/local/bin/envplate && \  
apk del curl ca-certificates && \  
rm /var/cache/apk/*  
  
COPY lstu.conf $LSTU_HOME/  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["lstu"]  

