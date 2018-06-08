FROM debian:jessie  
  
ARG DEST_DIR=/kerio-reprepro-webapi  
ENV DEST_DIR=$DEST_DIR  
  
RUN mkdir -p $DEST_DIR  
COPY ruby/Gemfile* $DEST_DIR/  
  
RUN \  
apt-get -y update && \  
apt-get -y install --no-install-recommends g++ make reprepro ruby bundler
ruby-dev zlib1g-dev && \  
cd $DEST_DIR && \  
bundler install && \  
apt-get -y remove ruby-dev zlib1g-dev g++ make && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
COPY ruby/bin $DEST_DIR/bin  
COPY ruby/config.ru $DEST_DIR  
COPY ruby/lib $DEST_DIR/lib  
  
RUN \  
mkdir -p /usr/lib/kerio-reprepro-webapi && \  
echo "#!/bin/sh\nruby -I $DEST_DIR/lib/ $DEST_DIR/bin/xmlgen \$@" >
/usr/lib/kerio-reprepro-webapi/xmlgen && \  
chmod +x /usr/lib/kerio-reprepro-webapi/xmlgen && \  
ln -s "$DEST_DIR/bin/xmlgen-outhook" /usr/lib/kerio-reprepro-webapi/xmlgen-
outhook && \  
ln -s "$DEST_DIR/bin/xmlgen-loghook" /usr/lib/kerio-reprepro-webapi/xmlgen-
loghook  
  
ADD webapi-entrypoint /  
  
WORKDIR $DEST_DIR  
  
VOLUME /gpg  
  
ENTRYPOINT ["/webapi-entrypoint"]  
  

