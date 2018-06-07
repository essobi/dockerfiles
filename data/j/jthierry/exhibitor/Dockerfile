# Copyright 2014 Netflix, Inc.  
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
FROM netflixoss/java:8  
MAINTAINER Netflix Open Source Development <talent@netflix.com>  
  
RUN ZK_VERSION=3.4.9 &&\  
apt-get update &&\  
apt-get -y install --no-install-recommends --force-yes ca-certificates &&\  
wget
http://archive.apache.org/dist/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz.md5
&&\  
wget
http://archive.apache.org/dist/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
&&\  
md5sum -c zookeeper-${ZK_VERSION}.tar.gz.md5 &&\  
tar xzf zookeeper-${ZK_VERSION}.tar.gz &&\  
rm /zookeeper-${ZK_VERSION}.tar.gz* &&\  
mv /zookeeper-${ZK_VERSION} /zookeeper  
  
RUN apt-get -y install --no-install-recommends --force-yes maven &&\  
mkdir /exhibitor &&\  
cd /exhibitor  
  
ADD pom.xml /exhibitor/pom.xml  
  
RUN cd /exhibitor &&\  
mvn clean package &&\  
mv target/exhibitor-1.0.jar . &&\  
rm -rf /exhibitor/target &&\  
rm /exhibitor/pom.xml  
  
ADD exhibitor.properties /exhibitor/exhibitor.properties  
  
EXPOSE 2181 2888 3888 8080  
WORKDIR /exhibitor  
  
ENTRYPOINT ["java", "-jar", "exhibitor-1.0.jar", "-c", "file"]

