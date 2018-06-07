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
#  
# Pull base image.  
FROM java:8  
#RUN apt-get update && \  
# apt-get install -y software-properties-common wget git  
#  
#  
#RUN \  
# echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections && \  
# apt-add-repository universe && \  
# add-apt-repository -y ppa:webupd8team/java && \  
# apt-get update && \  
# apt-get install -y oracle-java8-installer && \  
# rm -rf /var/lib/apt/lists/* && \  
# rm -rf /var/cache/oracle-jdk8-installer  
#  
## Define commonly used JAVA_HOME variable  
#ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
RUN apt-get update && apt-get install -y git maven emacs-nox  
  
# Define working directory.  
WORKDIR /data  
  
# Copies sparkler  
# ADD ./ /data/sparkler  
RUN git clone https://github.com/USCDataScience/sparkler /data/sparkler  
RUN cd sparkler && git pull --all && git checkout memex-dd  
  
# Setup Solr  
RUN wget http://archive.apache.org/dist/lucene/solr/6.2.1/solr-6.2.1.tgz -O
/data/solr.tgz && \  
cd /data/ && tar xzf /data/solr.tgz  
  
RUN mv /data/solr-* /data/solr && rm /data/solr.tgz  
RUN apt-get -y install lsof  
RUN /data/solr/bin/solr start && \  
/data/solr/bin/solr create_core -c crawldb -d
/data/sparkler/conf/solr/crawldb/ && \  
/data/solr/bin/solr stop  
RUN cd /data/sparkler/sparkler-ui/ && mvn clean package  
  
RUN export MAVEN_OPTS="-Xmx2g -Xss1g -XX:MaxPermSize=2g
-XX:+CMSClassUnloadingEnabled"&& \  
cd /data/sparkler && mvn clean install -DskipTests  
  
# Setup Sparkler Web Dashboard UI  
RUN cp -r /data/sparkler/sparkler-ui/sparkler-dashboard
/data/solr/server/solr-webapp/ && \  
cp /data/sparkler/conf/solr/sparkler-jetty-context.xml
/data/solr/server/contexts/  
  
RUN apt-get update && apt-get install -y --fix-missing openjfx # needed by the
Jbrowser  
  
ENV PATH="${JAVA_HOME}/bin:${PATH}"  
# Define default command.  
#CMD ["/data/solr/bin/solr", "start", "|", "tail", "-f", "/dev/null"]  
RUN apt-get install -y python && \  
apt-get install -y python-setuptools python-dev build-essential && \  
easy_install pip  
  
CMD /data/solr/bin/solr start -m 6g && cd /data/sce-cmd/webui && pip install
-r requirements.txt && python run.py  

