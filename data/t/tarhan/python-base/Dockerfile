FROM python:3.6.3-alpine3.6  
MAINTAINER Dmitriy Lekomtsev <lekomtsev@gmail.com>  
  
COPY ./prepare_alpine.sh /prepare_alpine.sh  
# Prepare script for installing runtime and buildtime dependencies of child
images  
COPY ./pip_install.sh /pip_install.sh  
# Script for installing packages via pip only if requirements.txt exists.  
COPY ./postinstall_alpine.sh /postinstall_alpine.sh  
  
RUN apk --no-cache add curl \  
# Sadly curl needed to download tini executable  
&& mkdir /app/ \  
&& pip install pip setuptools wheel \  
# Updating Python install system. Not mandatory I will always do this at start  
&& pip install shyaml \  
# Installing YAML command line parser  
&& curl -L https://github.com/krallin/tini/releases/download/v0.9.0/tini-
static -o /usr/local/bin/tini \  
&& chmod +x /usr/local/bin/tini \  
# Installing minimal init system for container  
# as defence from https://blog.phusion.nl/2015/01/20/docker-and-the-
pid-1-zombie-reaping-problem/  
&& chmod +x /prepare_alpine.sh \  
&& chmod +x /pip_install.sh \  
&& chmod +x /postinstall_alpine.sh  
  
WORKDIR /app  
  
ENTRYPOINT ["tini", "--"]  
CMD ["python"]  
  
ONBUILD COPY ./app.yaml /app/app.yaml  
ONBUILD COPY ./requirements.txt /app/requirements.txt  
ONBUILD RUN /prepare_alpine.sh \  
&& /pip_install.sh \  
&& /postinstall_alpine.sh  
# app.yaml contains two keys 'runtime' and 'buildtime' under
dependencies.alpine key.  
# 'runtime' enlist OS packages contains libraries needed by Python packages  
# to work. For example, lxml Python package uses libxml2 and libxslt libraries  
# at runtime.  
# 'buildtime' enlist OS packages contains header files needed by Python
packages  
# while pip installing them. For example, lxml Python package uses lixml2-dev  
# and libxslt-dev during its installation process. This list does not include  
# standard OS packages needed at build time like gcc or cmake.  
ONBUILD COPY . /app/  

