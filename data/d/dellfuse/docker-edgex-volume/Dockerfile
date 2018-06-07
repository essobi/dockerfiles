###############################################################################  
# Copyright 2016-2017 Dell Inc.  
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
###############################################################################  
# Create a Docker volume for use by Mongo data files,  
# micro service log files, and Consul config and data files  
FROM ubuntu:latest  
MAINTAINER Cloud Tsai <Cloud.Tsai@Dell.com>  
  
# Create a consul user and group first so the IDs get set the same way, even
as  
# the rest of this may change over time.  
RUN addgroup consul && \  
adduser --system \--ingroup consul consul  
  
# standard mongo db data dir directories  
RUN mkdir /data  
RUN mkdir /data/db  
RUN echo "this directory is reserved for Dell Fuse database files" >
/data/db/README  
  
# EdgeX shared directories  
ENV EDGEX_BASE=/edgex  
RUN mkdir $EDGEX_BASE  
RUN mkdir $EDGEX_BASE/logs  
RUN echo "this directory is reserved for EdgeX Foundry log files" >
$EDGEX_BASE/logs/README  
  
# Consul config and data directories  
# The /consul/data dir is used by Consul to store state. The agent will be
started  
# with /consul/config as the configuration directory so you can add additional  
# config files in that location.  
RUN mkdir /consul  
RUN mkdir /consul/config  
RUN mkdir /consul/data  
RUN echo "this directory is reserved for EdgeX Foundry Consul config files" >
/consul/config/README  
RUN echo "this directory is reserved for EdgeX data files" >
/consul/data/README  
RUN chown -R 100:1000 /consul  
  
COPY static-services-config.json /consul/config  
  
ENTRYPOINT /usr/bin/tail -f /dev/null  

