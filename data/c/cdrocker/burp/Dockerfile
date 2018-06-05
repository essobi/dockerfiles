FROM alpine:latest  
  
# meta  
LABEL \  
org.label-schema.maintainer="me codar nl" \  
org.label-schema.name="burp" \  
org.label-schema.description="Docker version of Burp based on Alpine Linux" \  
org.label-schema.version="1.0" \  
org.label-schema.vcs-url="https://github.com/githubcdr/docker-burp" \  
org.label-schema.schema-version="1.0"  
  
WORKDIR /tmp  
  
RUN apk add --update --no-cache bash s6 git ca-certificates alpine-sdk
autoconf \  
automake openssl openssl-dev uthash uthash-dev librsync librsync-dev acl-dev
ncurses-dev zlib-dev \  
&& git clone git://github.com/grke/burp.git \  
&& cd burp \  
&& autoreconf -vif \  
&& sed -i '/LT_INIT(disable-static)/d' ./configure \  
&& ./configure \  
&& make \  
&& make install-strip \  
&& make install-configs \  
&& rm -Rfv /tmp/burp  
  
# add files, this also creates the layout for the filesystem  
COPY files/root/ /  
  
# fixups  
RUN chmod a+x /service/*/run  
  
# ready to run  
EXPOSE 4971/tcp 4972/tcp  
  
# manage with s6  
ENTRYPOINT ["/bin/s6-svscan","/service"]  

