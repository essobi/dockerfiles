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
FROM ubuntu:17.04  
MAINTAINER Dongjoon Hyun <dongjoon@apache.org>  
  
RUN \  
apt update && \  
apt install -y openssh-server openjdk-8-jdk-headless && \  
apt clean  
  
RUN \  
mkdir /var/run/sshd && \  
ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo 'StrictHostKeyChecking no' > /root/.ssh/config  
COPY start.sh /root/  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $PATH:$JAVA_HOME/bin  
RUN echo 'JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >> /etc/environment  

