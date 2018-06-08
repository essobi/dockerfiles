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
FROM centos:centos7  
  
RUN echo root:changeme | chpasswd  
  
## Install some basic utilities that aren't in the default image  
RUN yum clean all -y && yum update -y  
RUN yum -y install vim wget sudo which tar openssh-clients ntp git httpd
python-setuptools python-setuptools-devel glibc-common gcc* python-devel  
  
WORKDIR /tmp/  
RUN easy_install pip  
  
RUN pip install setuptools --upgrade  
RUN pip install
"git+https://github.com/chuyqa/kernel_gateway_demos.git#egg=nb2kg&subdirectory=nb2kg"  
  
RUN jupyter serverextension enable \--py nb2kg --sys-prefix  
  
ADD scripts/launchnb.sh /tmp/launchnb.sh  
  
CMD ["/tmp/launchnb.sh"]  
  

