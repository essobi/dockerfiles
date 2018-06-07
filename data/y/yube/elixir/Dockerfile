# base image elixer to start with  
FROM elixir:1.6.5-alpine  
  
# build with command:  
# docker build -t hive-elixir:1.6.5-alpine ./  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
ENV TERM xterm  
ENV REPLACE_OS_VARS true  
  
# Install dependencies  
RUN set -xe \  
&& apk add --no-cache \  
build-base \  
bash \  
ca-certificates \  
postgresql-client \  
imagemagick \  
git \  
curl \  
openssh \  
ncurses \  
httpie \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
ENV SHELL=/bin/bash  
  
# install hex package manager  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
# install dockerize  
RUN set -ex \  
&& DOCKERIZE_URL="https://circle-downloads.s3.amazonaws.com/circleci-
images/cache/linux-amd64/dockerize-latest.tar.gz" \  
&& curl --silent --show-error --location --fail --retry 3 --output
/tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \  
&& tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \  
&& rm -rf /tmp/dockerize-linux-amd64.tar.gz  
  
# Procfile runner  
RUN set -ex \  
&& curl https://github.com/chrismytton/shoreman/raw/master/shoreman.sh -sLo
/bin/shoreman \  
&& chmod 755 /bin/shoreman  
  
# create app folder  
RUN mkdir /app  
WORKDIR /app  
  
CMD ["iex"]  

