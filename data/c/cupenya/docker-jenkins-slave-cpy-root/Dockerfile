# The MIT License  
#  
# Copyright (c) 2015, CloudBees, Inc.  
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
FROM cupenya/docker-jenkins-slave-mongo-es-ivy2-cache  
MAINTAINER Elmar Weber <elmar(.)weber(@)cupenya(.)com>  
  
# add npm, gulp and bower  
USER root  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs && \  
npm --global install yarn && \  
npm --global install gulp && \  
npm --global install bower && \  
# fix permissions done during install  
chown jenkins:jenkins -R /home/jenkins/.npm  
  
# add ES plugin  
COPY elasticsearch-business-hours-2-3-3-SNAPSHOT.zip /tmp  
RUN /usr/share/elasticsearch/bin/plugin install -t 30s
file:///tmp/elasticsearch-business-hours-2-3-3-SNAPSHOT.zip && \  
rm /tmp/elasticsearch-business-hours-2-3-3-SNAPSHOT.zip  
  
# add k8s  
ENV K8S_VERSION 1.6.4  
RUN set -x && \  
wget -O /bin/kubectl "https://storage.googleapis.com/kubernetes-
release/release/v1.6.4/bin/linux/amd64/kubectl" && \  
chmod +x /bin/kubectl  
  
# add other utils required for k8s pipelines  
RUN apt-get install -y jq  
RUN npm install -g mustache  
  
# add gcloud  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && apt-get install -y google-cloud-sdk  
  
# add docker setup script, docker daemon is bound via host path  
USER root  
  
COPY setup-docker-and-start-jenkins.sh /setup-docker-and-start-jenkins.sh  
RUN chmod 755 /setup-docker-and-start-jenkins.sh  
  
# overwrite default entry point to wrap docker user and group creation  
ENTRYPOINT ["/setup-docker-and-start-jenkins.sh"]  

