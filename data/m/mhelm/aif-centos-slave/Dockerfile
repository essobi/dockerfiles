# The MIT License  
#  
# Copyright (c) 2017, Markus Helm  
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
FROM mhelm/docker-centos-slave:latest  
MAINTAINER Markus Helm <markus.m.helm@live.de>  
  
# Switch to user `root` to install the packages  
USER root  
  
# Enable epel repository  
RUN yum -y install epel-release  
  
# Install the additional packages which are need for build the project's
software  
RUN \  
yum -y install \  
xorg-x11-server-Xvfb \  
unzip \  
tar \  
git \  
perl-Data-Dumper \  
perl-Sort-Versions \  
perl-XML-Parser \  
gcc-c++ \  
make \  
boost \  
boost-devel \  
rpm-build \  
p7zip \  
p7zip-plugins \  
&& \  
yum clean all  
  
# Switch back to user `jenkins`  
USER jenkins  

