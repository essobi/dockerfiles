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
FROM python:3.6-alpine  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
  
RUN apk add --no-cache gcc musl-dev dumb-init  
  
WORKDIR /shipper  
COPY repos repos  
COPY shipper.py shipper.py  
COPY config.json config.json  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
#RUN apk del gcc musl-dev  
# Metadata params provided with docker build command  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata http://label-schema.org/rc1/  
LABEL maintainer="o2r-project <https://o2r.info>" \  
org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r shipper" \  
org.label-schema.description="ERC shipping to repositories" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["python", "shipper.py"]  
  
# docker build -t o2r-shipper .

