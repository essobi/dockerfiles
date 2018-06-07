FROM evild/alpine-ruby:2.3  
MAINTAINER Domninique HAAS <contact@dominique-haas.fr>  
  
ARG WPSCAN_VERSION=2.9  
ENV UID=991 \  
GID=991  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
git \  
ca-certificates \  
openssl \  
curl-dev \  
libffi-dev \  
procps \  
zlib-dev \  
ruby-dev \  
&& apk add --no-cache --virtual .persistent-deps \  
readline-dev \  
libxslt-dev \  
libxml2-dev \  
&& echo "gem: --no-ri --no-rdoc" > /etc/gemrc \  
&& mkdir /wpscan \  
&& cd /wpscan \  
&& git clone https://github.com/wpscanteam/wpscan.git . \  
&& bundle config build.nokogiri --use-system-libraries \  
&& bundle install --without test \  
&& /wpscan/wpscan.rb --update \  
&& apk del .build-deps \  
&& rm -rf /tmp \  
&& addgroup -g ${GID} wpscan && adduser -H -s /bin/sh -D -G wpscan -u ${UID}
wpscan \  
&& chown -R wpscan:wpscan /wpscan  
  
USER wpscan  
WORKDIR /wpscan  
ENTRYPOINT ["/wpscan/wpscan.rb"]  
CMD ["--help"]  

