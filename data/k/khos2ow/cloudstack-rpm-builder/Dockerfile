# Licensed to the Apache Software Foundation (ASF) under one  
# or more contributor license agreements. See the NOTICE file  
# distributed with this work for additional information  
# regarding copyright ownership. The ASF licenses this file  
# to you under the Apache License, Version 2.0 (the  
# "License"); you may not use this file except in compliance  
# with the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing,  
# software distributed under the License is distributed on an  
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  
# KIND, either express or implied. See the License for the  
# specific language governing permissions and limitations  
# under the License.  
  
FROM centos:7  
LABEL maintainer="Khosrow Moossavi <me@khosrow.io> (@khos2ow)"  
  
RUN \  
yum clean metadata && \  
yum install -y epel-release && \  
yum clean metadata && \  
yum install -y \  
make \  
which \  
mlocate \  
tar \  
rpm-build \  
yum-utils \  
createrepo \  
mkisofs \  
git \  
maven \  
java-1.8.0-openjdk-devel \  
tomcat \  
python-argparse \  
python-yaml \  
python-pip \  
python-wheel \  
mysql-connector-python \  
gcc \  
gcc-c++ \  
jq \  
ws-commons-util && \  
yum upgrade python-setuptools && \  
yum clean all && rm -rf /var/cache/yum  
  
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk  
  
VOLUME /mnt/build  
WORKDIR /mnt/build  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  

