# Ubuntu 16.04 with SonarQube/GoLand scanning tools installed.  
# Barebones installation with GoLang,GoMetaLinter and Sonar-scanner installed
and configured  
# Creation Date: March 15, 2018  
# OS Version - Note that this Dockerfile was created with Ubuntu in mind.  
FROM ubuntu:16.04  
# Author  
MAINTAINER Dennis Christilaw (https://github.com/Talderon)  
  
# extra metadata  
LABEL version="0.6.9"  
LABEL description="Beta build of SonarQube Scanner for GoLang - Dev
Environment."  
  
ENV HOME /root  
ENV GOPATH=$HOME/go_projects  
ENV GOBIN=$GOPATH/bin  
  
# Add the hostname to the hosts file  
RUN uhost=$(cat /etc/hostname ) && \  
echo '127.0.0.1 '$uhost >> /etc/hosts  
  
# Run updates to ensure the repo's are updated  
RUN apt-get update -qy && apt-get upgrade -qy  
  
# Installs software in order to allow for independent vendor software sources,
in particular the “add-apt-repository” command that is used elsewhere  
# As well as come CLI Tools that are needed for various functions.  
RUN apt-get install -qy \  
software-properties-common \  
apt-transport-https \  
ca-certificates curl \  
software-properties-common \  
make \  
vim \  
unzip \  
wget \  
git \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Elevate to Sudo  
RUN sudo -s  
  
# Set GoLang Environment  
RUN mkdir -p $HOME/go_projects/{bin,src,pkg} && \  
mkdir -p /usr/local/sonar-scanner/bin && \  
mkdir -p /usr/local/go/bin && \  
touch $HOME/.profile  
  
# Configure Path  
RUN echo
'PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/go/bin:/root/go_projects/bin:/usr/local:/usr/local/sonar-
scanner/bin:/usr/local/go/bin"' >>/root/.profile && \  
echo 'GOPATH=$HOME/go_projects' >>/root/.profile && \  
echo 'GOBIN=$GOPATH/bin' >>$HOME/.profile  
  
# Source the .profile to get path changes  
RUN /bin/bash -c "source $HOME/.profile"  
  
# Install Docker  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - &&
\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" && \  
apt-get update -qy && \  
apt-get install -qy docker-ce  
  
# Install Kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/v1.9.4/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl  
  
# Install GoLang (1.10)  
RUN wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.10.linux-amd64.tar.gz  
  
# Install Sonar-Scanner  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.3.778-linux.zip && \  
unzip sonar-scanner-cli-3.0.3.778-linux.zip -d /usr/local/ && \  
mv -f /usr/local/sonar-scanner-3.0.3.778-linux /usr/local/sonar-scanner  
  
# Install GoMetaLinter (breaking up for troubleshooting)  
RUN wget
https://github.com/alecthomas/gometalinter/releases/download/v2.0.5/gometalinter-2.0.5-linux-
amd64.tar.gz  
  
RUN tar -C /root/go_projects/bin -xzf gometalinter-2.0.5-linux-amd64.tar.gz  
  
RUN cd /root/go_projects/bin/gometalinter-2.0.5-linux-amd64 && \  
mv /root/go_projects/bin/gometalinter-2.0.5-linux-amd64/*
/root/go_projects/bin/ && \  
cd /root  
  
# Commenting below command for troubleshooting  
RUN $GOBIN/gometalinter --install  
  
# Cleanup  
RUN apt-get -qy autoremove && \  
rm -rf /root/go_projects/bin/gometalinter-2.0.5-linux-amd64/ && \  
rm -f /root/go_projects/bin/go1.10.linux-amd64.tar.gz && \  
rm -f /root/sonar-scanner-cli-3.0.3.778-linux.zip  

