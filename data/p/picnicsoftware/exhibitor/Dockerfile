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
#  
# 2016-03-30 Forked from github.com/Netflix-Skunkworks/zerotodocker  
# - Modified to fix zombie reaping problem  
FROM netflixoss/java:7  
# Original MAINTAINER: Netflix Open Source Development <talent@netflix.com>  
MAINTAINER Picnic Software <dev@picnicsoftware.com>  
  
RUN apt-get update &&\  
apt-get -y install ca-certificates &&\  
wget -q
http://archive.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz.md5
&&\  
wget -q
http://archive.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
&&\  
md5sum -c zookeeper-3.4.6.tar.gz.md5 &&\  
tar xzf zookeeper-3.4.6.tar.gz &&\  
rm /zookeeper-3.4.6.tar.gz* &&\  
mv /zookeeper-3.4.6 /zookeeper  
  
RUN apt-get -y install maven &&\  
mkdir /exhibitor &&\  
cd /exhibitor  
  
ADD pom.xml /exhibitor/pom.xml  
ADD launch.sh /  
  
RUN chmod +x /launch.sh &&\  
cd /exhibitor &&\  
mvn assembly:single &&\  
mv target/exhibitor-1.0-jar-with-dependencies.jar . &&\  
rm -rf /exhibitor/target &&\  
rm /exhibitor/pom.xml  
  
ADD exhibitor.properties /exhibitor/exhibitor.properties  
  
EXPOSE 2181 2888 3888 8080  
WORKDIR /exhibitor  
  
CMD ["/bin/bash", "-c", "/launch.sh"]  

