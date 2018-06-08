FROM nvidia/cuda:8.0-devel-ubuntu16.04  
# Copyright (c) 2012-2016 Codenvy, S.A.  
# All rights reserved. This program and the accompanying materials  
# are made available under the terms of the Eclipse Public License v1.0  
# which accompanies this distribution, and is available at  
# http://www.eclipse.org/legal/epl-v10.html  
# Contributors:  
# Codenvy, S.A. - initial API and implementation  
# Patrick Collins  
# Run on EOL versions:  
# RUN sed -i -re 's/([a-z]{2}\\.)?archive.ubuntu.com|security.ubuntu.com/old-
releases.ubuntu.com/g' /etc/apt/sources.list  
  
USER root  
  
ENV LANG en_US.UTF-8  
ENV JAVA_MAJOR_VERSION=8  
ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64  
ENV PATH=$JAVA_HOME/bin:$PATH  
  
RUN apt-get update; \  
apt-get install -y \  
vim man \  
# unnecessary.  
locales \  
rsync \  
openssh-server \  
sudo \  
procps \  
wget \  
unzip \  
mc \  
ca-certificates \  
curl \  
software-properties-common \  
bash-completion && \  
if [ "$UBUNTUVERSION" != "18.04" ]; then apt-get install -y python-software-
properties; fi && \  
mkdir /var/run/sshd && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
useradd -u 1000 -G users,sudo -d /home/user --shell /bin/bash -m user && \  
usermod -p "*" user && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN add-apt-repository ppa:git-core/ppa && \  
apt-get update; \  
apt-get install -y git subversion && \  
apt-get -y autoremove && \  
apt-get install openjdk-$JAVA_MAJOR_VERSION-jdk openjdk-$JAVA_MAJOR_VERSION-
source -y && \  
update-ca-certificates -f && \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
sudo locale-gen $LANG  
  
USER user  
RUN svn --version && \  
sed -i 's/# store-passwords = no/store-passwords = yes/g'
/home/user/.subversion/servers && \  
sed -i 's/# store-plaintext-passwords = no/store-plaintext-passwords = yes/g'
/home/user/.subversion/servers  
USER root  
EXPOSE 22 4403  
WORKDIR /projects  
  
USER user  
  
CMD sudo /usr/sbin/sshd -D && tail -f /dev/null

