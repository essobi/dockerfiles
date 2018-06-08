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
FROM python:3.6-stretch  
  
## based on https://github.com/rocker-
org/rocker/blob/master/r-base/Dockerfile, but use simply the available R
version  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
r-base \  
#r-base-dev \  
#r-recommended \  
&& echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site \  
##&& echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /o2r-meta  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# Install potentially failing dependencies, but do not fail build if optional
requirements are missing  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libgdal-dev  
COPY requirements-opt.txt requirements-opt.txt  
#RUN pip install -r requirements-opt.txt; exit 0  
RUN pip install -r requirements-opt.txt 2>&1 > /tmp/o2r-meta-optional.log \  
|| echo "\n\nErrors installing optional dependencies\n\n" && cat
/tmp/o2r-meta-optional.log  
  
COPY broker broker  
COPY extract extract  
COPY harvest harvest  
COPY helpers helpers  
COPY parsers parsers  
COPY schema schema  
COPY validate validate  
COPY o2rmeta.py o2rmeta.py  
  
# Metadata params provided with docker build command  
ARG VERSION=dev  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# Metadata http://label-schema.org/rc1/  
LABEL maintainer="o2r-project <https://o2r.info>" \  
org.label-schema.vendor="o2r project" \  
org.label-schema.url="http://o2r.info" \  
org.label-schema.name="o2r meta" \  
org.label-schema.description="Metadata toolsuite for an extract-map-validate
workflow supporting ERC" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
RUN useradd o2r  
USER o2r  
  
SHELL ["sh", "-lc"]  
  
ENTRYPOINT ["python3", "/o2r-meta/o2rmeta.py"]

