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
FROM ubuntu:16.04  
MAINTAINER Stock Software  
  
# Setup RBENV configuration  
ENV
PATH=/home/buildbot/.nodenv/shims:/home/buildbot/.nodenv/bin:/home/buildbot/.rbenv/shims:/home/buildbot/.rbenv/bin:${PATH}
RBENV_ROOT=/home/buildbot/.rbenv NODENV_ROOT=/home/buildbot/.nodenv
LANG=C.UTF-8  
RUN apt-get update && apt-get install -y --force-yes apt-transport-https &&
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >
/etc/apt/sources.list.d/docker.list && apt-get update && apt-get install -y
--force-yes docker-engine build-essential curl git zlib1g-dev libssl-dev
libreadline-dev libyaml-dev libxml2-dev libxslt-dev libxtst6 libxi6 freetds-
dev zip nsis imagemagick libpq-dev xvfb inetutils-ping vim && apt-get clean &&
useradd -ms /bin/bash buildbot  
  
USER buildbot  
  
RUN echo "gem: --no-ri --no-rdoc" > /home/buildbot/.gemrc  
  
RUN git clone \--depth 1 git://github.com/sstephenson/rbenv.git ${RBENV_ROOT}
&& git clone \--depth 1 https://github.com/sstephenson/ruby-build.git
${RBENV_ROOT}/plugins/ruby-build && export CONFIGURE_OPTS=--disable-install-
doc && echo 'eval "$(rbenv init -)"' >> /home/buildbot/.bashrc  
  
RUN git clone \--depth 1 https://github.com/nodenv/nodenv.git ${NODENV_ROOT}
&& git clone \--depth 1 https://github.com/nodenv/node-build.git
${NODENV_ROOT}/plugins/node-build && cd ${NODENV_ROOT} && src/configure &&
make -C src && rm -f src/Makefile src/*.o echo 'eval "$(nodenv init -)"' >>
/home/buildbot/.bashrc  
  
WORKDIR /home/buildbot  
  
ENV JAVA_HOME=/opt/jdk \  
PATH=/opt/jdk/bin:${PATH} \  
CONFIGURE_OPTS=--disable-install-doc  
  
USER root  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="CI Build Image" \  
org.label-schema.description="An image that contains our the tools required
for our automated build pipeline" \  
org.label-schema.url="https://github.com/stocksoftware/build" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/stocksoftware/build" \  
org.label-schema.vendor="Stocksoftware" \  
org.label-schema.schema-version="1.0"  
  
RUN set -ex && \  
mkdir -p /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-
cookie" -o /tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz
&& \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
rm -rf /tmp/java.tar /tmp/java.tar.gz && \  
ln -s /opt/jdk1.8.0_131 /opt/jdk  
  
USER buildbot  
  
RUN rbenv install 1.9.3-p327 && \  
rbenv global 1.9.3-p327 && \  
rm -rf /tmp/ruby-build* && \  
gem install bundler && \  
gem install nokogiri -v 1.5.6 && \  
gem install ffi-yajl -v 1.4.0 && \  
gem install eventmachine -v 1.0.3 && \  
gem install ffi -v 1.9.8 && \  
gem install libyajl2 -v 1.2.0 && \  
rbenv rehash  
  
RUN rbenv install 2.3.1 && \  
rbenv global 2.3.1 && \  
rm -rf /tmp/ruby-build* && \  
gem install bundler && \  
gem install octokit -v 4.6.2 && \  
gem install netrc -v 0.11.0 && \  
gem install rjb -v 1.5.4 && \  
gem install sass -v 3.4.22 && \  
gem install nokogiri -v 1.7.2 && \  
gem install tiny_tds -v 1.0.5 && \  
gem install pg -v 0.19.0 && \  
rbenv rehash  
  
RUN nodenv install 6.10.3 && \  
nodenv global 6.10.3 && \  
nodenv rehash && \  
npm install -g yarn && \  
nodenv rehash  

