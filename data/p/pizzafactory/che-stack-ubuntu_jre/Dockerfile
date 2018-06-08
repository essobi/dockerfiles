# Copyright (c) 2012-2016 Codenvy, S.A.  
# All rights reserved. This program and the accompanying materials  
# are made available under the terms of the Eclipse Public License v1.0  
# which accompanies this distribution, and is available at  
# http://www.eclipse.org/legal/epl-v10.html  
# Contributors:  
# Codenvy, S.A. - initial API and implementation  
# Monami-ya LLC, Japan. - Update to 16.04  
  
FROM ubuntu:16.04  
MAINTAINER Masaki Muranaka <monaka@monami-ya.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
RUN apt-get update && \  
apt-get -y install \  
git \  
subversion \  
openjdk-8-jre-headless \  
openssh-server \  
sudo \  
procps \  
wget \  
unzip \  
mc \  
ca-certificates \  
curl \  
software-properties-common \  
python-software-properties && \  
mkdir /var/run/sshd && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
useradd -u 1000 -G users,sudo -d /home/user --shell /bin/bash -m user && \  
PASS=$(openssl rand -base64 32) && \  
echo "${PASS}\n${PASS}" | passwd user && \  
apt-get -y remove software-properties-common && \  
apt-get clean && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo "#! /bin/bash\n set -e\n sudo /usr/sbin/sshd -D &\n exec \"\$@\"" >
/home/user/entrypoint.sh && chmod a+x /home/user/entrypoint.sh  
  
ENV LANG en_US.UTF-8  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >>
/home/user/.bashrc && \  
sudo locale-gen en_US.UTF-8  
USER user  
EXPOSE 22 4401 4403  
WORKDIR /projects  
ENTRYPOINT ["/home/user/entrypoint.sh"]  
CMD tail -f /dev/null  

