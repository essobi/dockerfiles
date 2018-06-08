# Licensed to the Apache Software Foundation (ASF) under one or more  
# contributor license agreements. See the NOTICE file distributed with  
# this work for additional information regarding copyright ownership.  
# The ASF licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM centos:7  
MAINTAINER Marco Tagliabue <marco.tagliabue@radicalbit.io>  
  
# `Z_VERSION` will be updated by `dev/change_zeppelin_version.sh`  
ENV Z_VERSION="0.7.1" \  
STACK_VERSION="2.5.0.0" \  
DISTRO_VERSION="rblight10"  
ENV LOG_TAG="[ZEPPELIN_${Z_VERSION}]:" \  
Z_HOME="/zeppelin" \  
LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8  
RUN echo "$LOG_TAG update and install basic packages" && \  
yum -y update && \  
yum -y install gcc gcc-c++ make openssl-devel wget && \  
yum -y clean all  
  
ENV JAVA_HOME=/usr/java/jdk1.8.0_131/  
RUN echo "$LOG_TAG Install java8" && \  
wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm"
-O /root/jdk-8u131-linux-x64.rpm && \  
yum install /root/jdk-8u131-linux-x64.rpm -y && \  
rm -f /root/jdk-8u131-linux-x64.rpm  
  
RUN echo "$LOG_TAG Download Zeppelin binary" && \  
wget -O /tmp/zeppelin-${Z_VERSION}-bin-all.rpm https://public-
repo.radicalbit.io/rbd/centos7/${STACK_VERSION}/${DISTRO_VERSION}/zeppelin-${Z_VERSION}-1.noarch.rpm
&& \  
useradd -ms /bin/bash zeppelin && \  
rpm -Uvh --nodeps /tmp/zeppelin-${Z_VERSION}-bin-all.rpm && \  
rm -rf /tmp/zeppelin-${Z_VERSION}-bin-all.rpm && \  
rm -rf /zeppelin* && \  
mv /usr/lib/zeppelin ${Z_HOME}  
  
RUN echo "$LOG_TAG Cleanup" && \  
yum clean all && \  
mv /etc/zeppelin/conf.dist/* /etc/zeppelin && \  
mkdir ${Z_HOME}/notebook/  
  
EXPOSE 8080  
ADD note.json ${Z_HOME}/notebook/2BTRWA9EV/  
ADD interpreter.json ${Z_HOME}/conf/interpreter.json  
WORKDIR ${Z_HOME}  
CMD ["bin/zeppelin.sh"]

