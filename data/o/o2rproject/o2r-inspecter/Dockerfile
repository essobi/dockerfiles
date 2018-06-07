# (C) Copyright 2017 Opening Reproducible Research (http://o2r.info)  
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
FROM rocker/r-ver:3.4.3  
RUN apt-get update -qq && apt-get install -y \  
git-core \  
libssl-dev \  
libcurl4-gnutls-dev \  
zlib1g-dev  
  
RUN R -q -e 'install.packages(c("devtools"))'  
  
COPY . /inspecter  
WORKDIR /inspecter  
RUN R -q -e 'devtools::install()'  
  
WORKDIR /  
RUN rm -r /inspecter  
  
ARG VERSION=dev  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
ENV DEBUGME=inspecter  
  
LABEL maintainer="o2r-project <https://o2r.info>" \  
org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="inspecter" \  
org.label-schema.description="Inspect binary files from compendia" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
  
ENTRYPOINT ["R"]  
CMD ["-e", "library('inspecter', verbose = TRUE); inspecter::start()"]  

