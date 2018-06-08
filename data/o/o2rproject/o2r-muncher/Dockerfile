# (C) Copyright 2017 o2r project. https://o2r.info  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
FROM node:8-alpine  
  
# Python, based on frolvlad/alpine-python3  
RUN apk add --no-cache \  
python2 \  
&& python2 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip install --upgrade pip setuptools \  
&& if [ ! -e /usr/bin/pip ]; then ln -s pip /usr/bin/pip ; fi \  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python2
/usr/bin/python; fi \  
&& rm -r /root/.cache  
  
# for vips-dev, needed by sharp, needed by o2r-checker  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
# App build time dependencies  
RUN apk add --no-cache \  
git \  
g++ \  
# next 4 needed for sharp, see
http://sharp.dimens.io/en/stable/install/#alpine-linux  
make \  
vips-dev \  
fftw-dev \  
binutils  
  
# App system dependencies & init system  
RUN apk add --no-cache \  
unzip \  
icu-dev \  
dumb-init \  
&& pip install --upgrade pip \  
&& pip install bagit  
  
# App installation  
WORKDIR /muncher  
COPY package.json package.json  
  
RUN npm install --production  
  
# Clean up  
RUN apk del git make binutils g++ \  
&& rm -rf /var/cache  
  
# Copy files after npm install to utilize build caching  
COPY config config  
COPY controllers controllers  
COPY lib lib  
COPY index.js index.js  
  
# Metadata params provided with docker build command  
ARG VERSION=dev  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
ARG META_VERSION  
  
# Metadata http://label-schema.org/rc1/  
LABEL maintainer="o2r-project <https://o2r.info>" \  
org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r muncher" \  
org.label-schema.description="ERC execution and CRUD" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1" \  
info.o2r.meta.version=$META_VERSION  
  
# If running in a container the app is root, so the second order containers
also must have root access, otherwise permission problems arise  
ENV MUNCHER_META_TOOL_CONTAINER_USER=root  
ENV MUNCHER_CONTAINERIT_USER=root  
ENV MUNCHER_CONTAINER_USER=root  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["npm", "start" ]

