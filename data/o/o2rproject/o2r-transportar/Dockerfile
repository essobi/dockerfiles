# (C) Copyright 2016 The o2r project. https://o2r.info  
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
#  
FROM alpine:3.4  
MAINTAINER o2r-project, https://o2r.info  
  
RUN apk add --no-cache \  
nodejs \  
git \  
ca-certificates \  
wget \  
&& update-ca-certificates \  
&& git clone \--depth 1 -b master
https://github.com/o2r-project/o2r-transportar /transportar \  
&& wget -O /sbin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \  
&& chmod +x /sbin/dumb-init \  
&& apk del \  
git \  
wget \  
ca-certificates \  
&& rm -rf /var/cache  
  
WORKDIR /transportar  
RUN npm install --production  
  
# Metadata params provided with docker build command  
ARG VERSION=dev  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata http://label-schema.org/rc1/  
LABEL org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r transportar" \  
org.label-schema.description="ERC download" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
ENTRYPOINT ["/sbin/dumb-init", "--"]  
CMD ["npm", "start" ]  

