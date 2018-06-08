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
FROM node:8-slim  
# FROM alpine:3.6 and node:8-alpine does not work because of
https://github.com/sonicdoe/detect-character-encoding/issues/8  
# Python, based on frolvlad/alpine-python3  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
unzip \  
# needed for npm install gyp  
make \  
g++ \  
&& wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb \  
&& dpkg -i dumb-init_*.deb \  
&& pip install bagit  
  
# Install app  
WORKDIR /loader  
COPY package.json package.json  
RUN npm install --production  
  
RUN apt-get purge -y \  
make \  
g++ \  
&& rm -rf /var/cache  
  
COPY config config  
COPY controllers controllers  
COPY lib lib  
COPY index.js index.js  
  
# Metadata params provided with docker build command  
ARG VERSION=dev  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata http://label-schema.org/rc1/  
LABEL org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r loader" \  
org.label-schema.description="compendium and workspace loading from uploaded
files and cloud resources" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
# If running in a container the app is root, so the second order container
also must have root access, otherwise permission problems  
ENV LOADER_META_TOOL_CONTAINER_USER=root  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["npm", "start" ]  

