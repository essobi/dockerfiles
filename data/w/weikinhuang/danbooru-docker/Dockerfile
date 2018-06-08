FROM ruby:2.4-slim-stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN set -x \  
&& BUILD_DEPS=" \  
autoconf \  
automake \  
bison \  
build-essential \  
git \  
flex \  
ragel \  
" \  
&& apt-get update && apt-get install --quiet --no-install-recommends -y \  
${BUILD_DEPS} \  
ca-certificates \  
curl \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libreadline-dev \  
libmemcached-dev \  
libcurl4-openssl-dev \  
libpq-dev \  
ncurses-dev \  
\  
imagemagick \  
libmagickcore-dev \  
libmagickwand-dev \  
nginx \  
\  
ffmpeg \  
mkvtoolnix \  
\  
postgresql-client-9.6 \  
\  
&& mkdir -p /var/www/danbooru2/shared \  
&& git clone --depth=1 https://github.com/r888888888/danbooru
/var/www/danbooru2/shared \  
&& cd /var/www/danbooru2/shared \  
&& git rev-parse --short HEAD > REVISION \  
&& git rev-parse HEAD > /REVISION \  
&& rm -rf /var/www/danbooru2/shared/.git \  
\  
&& cd /var/www/danbooru2/shared \  
&& bundle install --path vendor/bundle --no-cache --without development test \  
\  
&& apt-get remove --purge -y ${BUILD_DEPS} \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN set -x \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# s6 overlay  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KILL_FINISH_MAXTIME=5000 \  
S6_KILL_GRACETIME=3000 \  
S6_LOGGING=0 \  
S6_VERSION=v1.20.0.0  
RUN set -x \  
&& curl -sSL -o /tmp/s6-overlay.tar.gz https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
\  
&& tar xzvf /tmp/s6-overlay.tar.gz -C / \  
&& rm -f /tmp/s6-overlay.tar.gz  
  
# explicitly set user/group IDs  
RUN groupadd -r danbooru --gid=999 && useradd -r -g danbooru --uid=999
danbooru  
  
# create work directories  
RUN set -x \  
&& mkdir -p \  
/var/www/danbooru2/shared/public/data \  
/var/www/danbooru2/shared/public/data/preview \  
/var/www/danbooru2/shared/public/data/sample \  
/var/www/danbooru2/shared/log \  
/var/www/danbooru2/shared/tmp \  
/var/www/danbooru2/shared/tmp/pids \  
&& chown -R danbooru:danbooru \  
/var/www/danbooru2/shared/public/data \  
/var/www/danbooru2/shared/public/data/preview \  
/var/www/danbooru2/shared/public/data/sample \  
/var/www/danbooru2/shared/log \  
/var/www/danbooru2/shared/tmp \  
/var/www/danbooru2/shared/tmp/pids  
  
# copy container overlay  
COPY /container /  
# set up workdir  
WORKDIR /var/www/danbooru2/shared  
  
# boot up the application  
CMD [ "/init" ]  

