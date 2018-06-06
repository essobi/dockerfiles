# (c) Wong Hoi Sing Edison <hswong3i@pantarei-design.com>  
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
FROM ubuntu:16.04  
ENV CROWD_OWNER "daemon"  
ENV CROWD_GROUP "daemon"  
ENV CROWD_HOME "/var/atlassian/application-data/crowd"  
ENV CROWD_CATALINA "/opt/atlassian/crowd"  
ENV CROWD_DOWNLOAD_URL
"https://downloads.atlassian.com/software/crowd/downloads/atlassian-
crowd-3.2.1.tar.gz"  
ENV JAVA_HOME "/usr/java/default"  
ENV JVM_MINIMUM_MEMORY "128m"  
ENV JVM_MAXIMUM_MEMORY "512m"  
ENV CATALINA_CONNECTOR_PROXYNAME ""  
ENV CATALINA_CONNECTOR_PROXYPORT ""  
ENV CATALINA_CONNECTOR_SCHEME "http"  
ENV CATALINA_CONNECTOR_SECURE "false"  
ENV CATALINA_CONTEXT_PATH ""  
ENV JVM_SUPPORT_RECOMMENDED_ARGS "-Datlassian.plugins.enable.wait=300"  
VOLUME $CROWD_HOME  
WORKDIR $CROWD_HOME  
  
EXPOSE 8020  
EXPOSE 8095  
ENTRYPOINT [ "dumb-init", "--" ]  
CMD [ "/etc/init.d/crowd", "start", "-fg" ]  
  
# Prepare APT depedencies  
RUN set -ex \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y alien apt-transport-https
apt-utils aptitude bzip2 ca-certificates curl debian-archive-keyring debian-
keyring git htop patch psmisc python-apt rsync software-properties-common sudo
unzip vim wget zip \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Oracle JRE  
RUN set -ex \  
&& ln -s /usr/bin/update-alternatives /usr/sbin/alternatives \  
&& ARCHIVE="`mktemp --suffix=.rpm`" \  
&& curl -skL -j -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/jre-8u172-linux-x64.rpm
> $ARCHIVE \  
&& DEBIAN_FRONTEND=noninteractive alien -i -k --scripts $ARCHIVE \  
&& rm -rf $ARCHIVE  
  
# Install Atlassian Crowd  
RUN set -ex \  
&& ARCHIVE="`mktemp --suffix=.tar.gz`" \  
&& curl -skL $CROWD_DOWNLOAD_URL > $ARCHIVE \  
&& mkdir -p $CROWD_CATALINA \  
&& tar zxf $ARCHIVE \--strip-components=1 -C $CROWD_CATALINA \  
&& chown -Rf $CROWD_OWNER:$CROWD_GROUP $CROWD_CATALINA \  
&& rm -rf $ARCHIVE  
  
# Install MySQL Connector/J JAR  
RUN set -ex \  
&& ARCHIVE="`mktemp --suffix=.tar.gz`" \  
&& curl -skL https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.46.tar.gz > $ARCHIVE \  
&& tar zxf $ARCHIVE \--strip-components=1 -C $CROWD_CATALINA/apache-
tomcat/lib/ mysql-connector-java-5.1.46/mysql-connector-java-5.1.46-bin.jar \  
&& rm -rf $ARCHIVE  
  
# Install dumb-init  
RUN set -ex \  
&& curl -skL https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 > /usr/local/bin/dumb-init \  
&& chmod 0755 /usr/local/bin/dumb-init  
  
# Copy files  
COPY files /  
  
# Apply patches  
RUN set -ex \  
&& patch -d/ -p1 < /.patch  
  
# Ensure required folders exist with correct owner:group  
RUN set -ex \  
&& mkdir -p $CROWD_HOME \  
&& chown -Rf $CROWD_OWNER:$CROWD_GROUP $CROWD_HOME \  
&& chmod 0755 $CROWD_HOME \  
&& mkdir -p $CROWD_CATALINA \  
&& chown -Rf $CROWD_OWNER:$CROWD_GROUP $CROWD_CATALINA \  
&& chmod 0755 $CROWD_CATALINA  

