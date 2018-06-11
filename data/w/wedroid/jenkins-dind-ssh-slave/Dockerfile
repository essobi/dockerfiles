# The MIT License  
#  
# Original Work Copyright (c) 2015, CloudBees, Inc.  
# Modified work Copyright 2017 Cyril Siman  
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
from docker:17.11-rc-dind  
LABEL MAINTAINER="Cyril Siman <wedroid@gmail.com>"  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG JENKINS_AGENT_HOME=/home/${user}  
  
ENV JENKINS_AGENT_HOME ${JENKINS_AGENT_HOME}  
  
RUN addgroup -g ${gid} ${group} \  
&& adduser -D -h "${JENKINS_AGENT_HOME}" -u "${uid}" -G "${group}" -s
/bin/bash "${user}" \  
&& passwd -u jenkins  
  
# setup SSH server  
RUN apk update \  
&& apk add --no-cache sudo bash openssh openjdk8 git subversion curl wget  
RUN sed -i /etc/ssh/sshd_config \  
-e 's/#PermitRootLogin.*/PermitRootLogin no/' \  
-e 's/#RSAAuthentication.*/RSAAuthentication yes/' \  
-e 's/#PasswordAuthentication.*/PasswordAuthentication no/' \  
-e 's/#SyslogFacility.*/SyslogFacility AUTH/' \  
-e 's/#LogLevel.*/LogLevel INFO/' \  
&& mkdir /var/run/sshd \  
&& echo "%${group} ALL=(ALL) NOPASSWD: /usr/local/bin/docker" >> /etc/sudoers  
  
#Update credential for Jenkins user  
RUN delgroup ping \  
&& addgroup -g 999 docker \  
&& addgroup jenkins docker \  
&& ln -s /usr/local/bin/docker /usr/bin/docker  
  
VOLUME "${JENKINS_AGENT_HOME}" "/tmp" "/run" "/var/run"  
WORKDIR "${JENKINS_AGENT_HOME}"  
  
COPY setup /usr/local/bin/setup  
  
EXPOSE 22  
ENTRYPOINT ["setup"]  
  

