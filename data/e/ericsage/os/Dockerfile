  
FROM fedora:25  
MAINTAINER Eric Sage <eric.david.sage@gmail.com>  
  
#Clean root  
RUN rm /root/*  
  
#Configure dnf  
RUN \  
echo "deltarpm=0" >> /etc/dnf/dnf.conf && \  
echo "group_package_types=default, mandatory, optional" >> /etc/dnf/dnf.conf  
  
#Place config files  
ADD /configfiles /root  
  
#Add repositories  
ADD repos /etc/yum.repos.d/  
  
#Install base packages  
RUN \  
dnf clean all && dnf update -y && \  
dnf group install -y "Standard" && \  
dnf install -y $(cat /root/.packages) && \  
dnf clean all  
  
#Install and update Python3 tools  
RUN \  
pip3 install --upgrade pip setuptools && \  
pip3 install virtualenv wheel  
  
#Install SDKs and Cloud Management Tools  
RUN \  
dnf install -y docker-engine google-cloud-sdk kubectl && \  
pip3 install awscli  
  
#Install the protocol buffers compiler  
RUN \  
wget
https://github.com/google/protobuf/releases/download/v3.1.0/protoc-3.1.0-linux-x86_64.zip
&& \  
unzip protoc-3.1.0-linux-x86_64.zip -d protobuf && mv protobuf/bin/protoc
/usr/bin && rm -rf proto*  
  
#Install vim plugins  
RUN vim -u NONE +'silent! source ~/.vimrc' +PlugInstall +qa  
  
#Set the initial directory  
WORKDIR /root/Code/src  
  
#Set command to shell  
CMD ["/bin/bash"]  

