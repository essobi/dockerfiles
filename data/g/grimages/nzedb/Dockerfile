FROM ubuntu:yakkety  
LABEL maintainer "Grimeton (Grimages) <grimages@fullmesh.de>"  
  
ARG S6_VERSION="v1.19.1.1"  
ARG S6_ARCH="amd64"  
ARG DEBIAN_FRONTEND="noninteractive"  
ARG LANG="en_US.UTF-8"  
ARG LC_ALL="C.UTF-8"  
ARG LANGUAGE="en_US.UTF-8"  
ARG TERM="xterm-256color"  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install apt-utils locales\  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
curl \  
ffmpeg \  
gettext-base \  
git \  
libtext-micromason-perl \  
mediainfo \  
nginx-extras \  
p7zip-full \  
php7.0 \  
php7.0-cgi \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-gd \  
php7.0-json \  
php7.0-mysql \  
php7.0-readline \  
php7.0-recode \  
php7.0-tidy \  
php7.0-xml \  
php7.0-xmlrpc \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-dba \  
php7.0-fpm \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-soap \  
php7.0-xsl \  
php7.0-zip \  
php-imagick \  
php-pear \  
tzdata \  
unrar \  
  
&& locale-gen $LANG  
  
ADD "https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-${S6_ARCH}.tar.gz"
"/tmp/s6.tar.gz"  
RUN tar xfz /tmp/s6.tar.gz -C /  
RUN apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
  
EXPOSE 80 443  
HEALTHCHECK NONE  
COPY rootfs/ /  
ENTRYPOINT ["/init"]  
  

