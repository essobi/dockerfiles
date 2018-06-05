FROM ruby:2.4-alpine  
MAINTAINER Yoan Blanc yoan@dosimple.ch  
  
  
RUN apk update \  
&& apk add --update --no-cache \  
build-base \  
curl \  
curl-dev \  
file \  
git \  
imagemagick \  
libmagic \  
libxml2-dev \  
libxslt-dev \  
mysql-client \  
mysql-dev \  
nodejs \  
postgresql-client \  
postgresql-dev \  
sqlite \  
sqlite-dev \  
yaml \  
zlib-dev \  
&& rm -rf /var/cache/apk/*  
  
# the user  
RUN adduser -h /usr/src/app -s /bin/sh -D ruby  
  
USER ruby  
RUN gem install -N bundler foreman rails rake  
  
USER root  
COPY build/boot.sh /usr/local/bin/boot.sh  
RUN chmod +x /usr/local/bin/boot.sh  
  
EXPOSE 3000  
#VOLUME /usr/src  
# Fix /etc/profile to not override the containers' env.  
RUN sed -i 's/^export PATH/#export PATH/' /etc/profile  
  
ENTRYPOINT [ "/usr/local/bin/boot.sh" ]  

