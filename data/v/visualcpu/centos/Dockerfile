# Copyright 2017 - Present Visual CPU (Dave Kirk)  
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
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
FROM centos:7  
MAINTAINER Dave Kirk <dave@visualcpu.com>  
  
# some initial 'housekeeping'  
#  
# - ensure we have the latest packages and delete obsolete packages  
# - install some useful commands child images may need  
#  
RUN set -xe \  
&& yum upgrade -y \  
&& yum install -y \  
sudo \  
curl \  
which \  
psmisc  
  
# set up some mount points that we can use with Docker volumes  
RUN set -xe \  
&& mkdir -m 0777 /workspace \  
&& mkdir -m 0777 /logs \  
&& mkdir -m 0777 /data \  
&& mkdir -m 0777 /config  
  
# install and configure supervisor  
RUN set -xe \  
&& yum install -y python-setuptools \  
&& easy_install pip \  
&& pip install supervisor \  
&& mkdir -p -m 0755 /etc/supervisor/conf.d/  
COPY etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
  
# my favourite bit of the image, the startup feature...  
#  
# this script will look for other scripts to execute on startup, making it
easy  
# to provide custom scripts for any image startup  
RUN mkdir -p -m 0755 /usr/local/container-startup  
COPY usr/local/sbin/container-start.sh /usr/local/sbin/container-start.sh  
RUN chmod 0755 /usr/local/sbin/container-start.sh  
  
# and lastly, our entry command - run the startup script  
CMD ["/usr/local/sbin/container-start.sh"]  

