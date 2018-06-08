# The MIT License  
#  
# Copyright (c) 2018, Octasic, inc.  
# Derived from docker-slave, Copyright (c) 2015-2017, CloudBees, Inc. and  
# other Jenkins contributors  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in  
# all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
# THE SOFTWARE.  
FROM ubuntu:16.04  
RUN apt-get -y update && \  
apt-get install -y curl wget make \  
cccc cppcheck cmake \  
openjdk-8-jre-headless \  
git \  
bsdmainutils  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /home/jenkins  
RUN groupadd -g 10000 jenkins  
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins  
LABEL Description="Jenkins base image for Octasic builds"  
  
ARG VERSION=3.16  
ARG AGENT_WORKDIR=/home/jenkins/agent  
  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER jenkins  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
VOLUME /home/jenkins/.jenkins  
VOLUME ${AGENT_WORKDIR}  
  
WORKDIR $HOME  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
ENTRYPOINT ["jenkins-slave"]  

