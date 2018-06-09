# Copyright (C) 2016 THRON S.p.A.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
FROM ubuntu:xenial  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV JAVA_VERSION_MINOR=9 \  
JAVA_VERSION_MAINTENANCE=0 \  
JAVA_VERSION_PATCH=4 \  
JAVA_VERSION_BUILD=11 \  
BUILD_RND_ID=c2514751926b4512b076cc82f959763f \  
JAVA_HOME=/usr/lib/jvm/default \  
TERM=xterm \  
PATH=${PATH}:/usr/lib/jvm/default/bin  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
nano \  
iputils-ping \  
net-tools \  
openssh-server \  
&& echo "[INFO] Configuring SSH" \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd \  
&& mkdir -p /var/run/sshd \  
&& echo "[INFO] Configuring Java" \  
&& mkdir -p /opt \  
&& mkdir -p /usr/lib/jvm \  
&& wget \  
\--no-check-certificate \  
\--header="Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MINOR}.${JAVA_VERSION_MAINTENANCE}.${JAVA_VERSION_PATCH}+${JAVA_VERSION_BUILD}/${BUILD_RND_ID}/serverjre-${JAVA_VERSION_MINOR}.${JAVA_VERSION_MAINTENANCE}.${JAVA_VERSION_PATCH}_linux-x64_bin.tar.gz"
\  
-O /tmp/java.tar.gz \  
&& tar -xzvf /tmp/java.tar.gz -C /usr/lib/jvm \  
&& rm /tmp/java.tar.gz \  
&& ln -s
/usr/lib/jvm/jdk-${JAVA_VERSION_MINOR}.${JAVA_VERSION_MAINTENANCE}.${JAVA_VERSION_PATCH}
${JAVA_HOME} \  
&& ln -s
/usr/lib/jvm/jdk-${JAVA_VERSION_MINOR}.${JAVA_VERSION_MAINTENANCE}.${JAVA_VERSION_PATCH}/bin/java
/usr/bin/java \  
&& echo "[INFO] Cleaning container" \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

