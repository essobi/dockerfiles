# Copyright (c) 2017, Nimbix, Inc.  
# All rights reserved.  
#  
# Redistribution and use in source and binary forms, with or without  
# modification, are permitted provided that the following conditions are met:  
#  
# 1. Redistributions of source code must retain the above copyright notice,  
# this list of conditions and the following disclaimer.  
# 2. Redistributions in binary form must reproduce the above copyright notice,  
# this list of conditions and the following disclaimer in the documentation  
# and/or other materials provided with the distribution.  
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"  
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE  
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE  
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR  
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF  
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS  
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN  
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)  
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  
# POSSIBILITY OF SUCH DAMAGE.  
#  
# The views and conclusions contained in the software and documentation are  
# those of the authors and should not be interpreted as representing official  
# policies, either expressed or implied, of Nimbix, Inc.  
FROM centos:7.1.1503  
MAINTAINER scot@descarteslabs.com  
  
WORKDIR /tmp  
VOLUME /tmp  
  
ADD ./scripts /usr/local/scripts  
#COPY build_torque.sh /tmp/build_torque.sh  
#RUN /tmp/build_torque.sh  
#RUN /usr/local/scripts/torque/install.sh  
RUN yum -y install openssh openssh-clients tmux vim wget  
  
RUN yum swap -y fakesystemd systemd && \  
yum install -y systemd-devel  
  
RUN curl -H 'Cache-Control: no-cache' \  
https://raw.githubusercontent.com/nimbix/image-common/master/install-nimbix.sh
\  
| bash -s  
RUN yum install -y epel-release  
RUN yum -y install htop aria2 numactl  

