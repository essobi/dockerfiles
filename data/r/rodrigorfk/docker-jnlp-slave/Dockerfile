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
  
FROM jenkinsci/slave  
MAINTAINER Nicolas De Loof <nicolas.deloof@gmail.com>  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
  
USER root  
RUN apt-get update && apt-get install -y libltdl7 python-pip zip && rm -rf
/var/lib/apt/lists/* && pip install awscli && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl && \  
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >
get_helm.sh && chmod 700 get_helm.sh && ./get_helm.sh && \  
rm get_helm.sh && groupadd docker && usermod -aG docker jenkins  
USER jenkins  
  
ENTRYPOINT ["jenkins-slave"]  

