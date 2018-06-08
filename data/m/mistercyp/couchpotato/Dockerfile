FROM xataz/alpine:3.3  
MAINTAINER xataz <https://github.com/xataz>  
  
ENV WEBROOT="" \  
UID=991 \  
GID=991  
LABEL description="Couchpotato based on alpine" \  
build_ver="2016042601"  
  
RUN export BUILD_DEPS="py-pip \  
build-base \  
libxml2-dev \  
python-dev \  
libxslt-dev \  
libffi-dev \  
openssl-dev" \  
&& apk add -U python \  
libxml2 \  
libxslt \  
libffi \  
git \  
${BUILD_DEPS} \  
&& git clone https://github.com/CouchPotato/CouchPotatoServer \  
&& cd /CouchPotatoServer \  
&& pip install lxml pyopenssl \  
&& apk del ${BUILD_DEPS} \  
&& rm -fr /var/cache/apk/*  
  
VOLUME ["/config"]  
EXPOSE 5050  
COPY startup /usr/bin/startup  
COPY config.ini /tmp/config.ini  
RUN chmod +x /usr/bin/startup  
  
CMD ["tini","--","/usr/bin/startup"]  

