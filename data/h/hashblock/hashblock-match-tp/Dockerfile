  
#
------------------------------------------------------------------------------  
# Copyright 2018 Frank V. Castellucci and Arthur Greef  
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
------------------------------------------------------------------------------  
# Description:  
# Builds a deployable production image for our hashblock-match-tp  
#  
# base image:  
# 1. Installs protobuf  
# 2. Generates protobuf files  
# final image:  
# 1. Installs sawtooth-sdk and crypto  
# 2. Copies relevant files from base  
# Build:  
# $ cd hashblock-exchange  
# $ docker build . -f docker/hashblock-match-tp -t hashblock/hashblock-match-
tp:latest  
#  
FROM ubuntu:xenial as base  
LABEL maintainers="Frank V. Castellucci, Arthur Greef"  
  
RUN apt-get update \  
&& apt-get install -y -q \  
apt-transport-https \  
python3-dev \  
python3-pip  
  
RUN mkdir -p /builder && \  
pip3 install \  
grpcio-tools \  
grpcio && \  
rm -rf /var/lib/apt/lists/  
  
WORKDIR /builder  
  
COPY bin bin  
COPY libs libs  
COPY apps apps  
COPY modules modules  
COPY protos protos  
COPY families families  
  
RUN bin/protogen && \  
pip3 uninstall -y grpcio grpcio-tools  
  
# The final image  
FROM ubuntu:xenial  
LABEL maintainers="Frank V. Castellucci, Arthur Greef"  
  
RUN apt-get update \  
&& apt-get install -y -q \  
apt-transport-https \  
libssl-dev \  
libffi-dev \  
python3-dev \  
python3-pip  
  
RUN pip3 install cryptography --no-binary cryptography  
  
RUN pip3 install sawtooth-sdk --upgrade && \  
mkdir -p /project/hashblock-exchange && \  
mkdir -p /project/hashblock-exchange/bin && \  
mkdir -p /project/hashblock-exchange/modules && \  
mkdir -p /project/hashblock-exchange/families/match && \  
mkdir -p /var/log/sawtooth  
  
COPY \--from=base /builder/bin/match-tp /project/hashblock-exchange/bin  
COPY \--from=base /builder/libs/hbzksnark /project/hashblock-exchange/bin  
COPY \--from=base /builder/modules /project/hashblock-exchange/modules  
COPY \--from=base /builder/families/match/hashblock_match /project/hashblock-
exchange/families/match/hashblock_match  
  
WORKDIR /project/hashblock-exchange  
ENV PATH $PATH:/project/hashblock-exchange/bin  

