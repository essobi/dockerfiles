# Copyright 2015 The Kubernetes Authors All rights reserved.  
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
# This image relies on the zeppelin-build image to get the zeppelin  
# binaries built, and the Makefile to put it in this directory.  
FROM stratospire/spark:2.0.0  
MAINTAINER Ryan C Koch <ryanckoch@gmail.com>  
  
ENV ZEPPELIN_VERSION="0.6.2"  
RUN mkdir -p /opt && \  
cd /opt && \  
curl
http://archive.apache.org/dist/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-
all.tgz | \  
tar -zx && \  
ln -s zeppelin-${ZEPPELIN_VERSION}-bin-all zeppelin && \  
echo Zeppelin ${ZEPPELIN_VERSION} installed in /opt  
  
ADD conf/* /opt/zeppelin/conf/  
ADD bin/* /opt/zeppelin/bin/  
EXPOSE 8080  
ENTRYPOINT ["/opt/zeppelin/bin/docker-zeppelin.sh"]  

