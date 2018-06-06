#  
# Copyright 2016 Hewlett-Packard Development Company, L.P.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing,  
# Software distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and
limitations under the License.  
FROM jenkinsci/jenkins:2.23  
# machine conf  
USER root  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y ca-certificates \  
bash git curl python nodejs build-essential yarn \  
dbus dbus-x11 && rm -rf /var/lib/apt/lists/*  
RUN npm install -g coffee-script grunt jshint coffeelint mocha \  
&& npm cache clean  
# make npm install work in jenkins+ docker env  
RUN mkdir -p /var/run/dbus && chmod -R 777 /var/run/dbus \  
&& chown -R jenkins: /var/run/dbus  
VOLUME /var/run/dbus  
  
USER jenkins  
ENV JENKINS_OPTS --httpPort=9090  
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false  
EXPOSE 9090  
RUN npm set prefix ~/.npm  
  
#jenkins conf  
COPY config/*.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY config/plugins.txt /usr/share/jenkins/plugins.txt  
RUN mkdir /var/tmp/templates  
COPY templates/* /var/tmp/templates/  
  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt)  

