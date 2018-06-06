FROM ruby:2.3.1-alpine  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
  
# We add some build dependency packages, then purge them later to make sure
our  
# final image uses what we just built.  
#  
# readline-dev is added due to:  
# https://bugs.ruby-lang.org/issues/11869 and https://github.com/docker-
library/ruby/issues/75  
RUN set -ex \  
&& apk update \  
&& apk add --no-cache --virtual .bundle-builddeps \  
autoconf \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
coreutils \  
curl \  
g++ \  
gcc \  
gdbm-dev \  
glib-dev \  
libc-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
make \  
ncurses-dev \  
openssl-dev \  
procps \  
readline-dev \  
ruby \  
yaml-dev \  
zlib-dev \  
&& bundle install \  
&& apk del .bundle-builddeps  
  
RUN echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk -U add shadow@community \  
&& groupadd -r user_grp \  
&& useradd -r -g user_grp user  
USER user  
EXPOSE 8080  
ADD . /app  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

