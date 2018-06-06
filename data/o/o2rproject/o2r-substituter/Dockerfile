# (C) Copyright 2017 o2r project  
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
FROM node:9-alpine  
  
RUN echo \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
# Add app and dependencies  
RUN apk add --no-cache \  
dumb-init \  
&& rm -rf /var/cache  
  
# Install app  
WORKDIR /substituter  
COPY package.json package.json  
RUN npm install --production  
  
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
LABEL maintainer="o2r-project <https://o2r.info>" \  
org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r substituter" \  
org.label-schema.description="ERC content substitution" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["npm", "start" ]  

