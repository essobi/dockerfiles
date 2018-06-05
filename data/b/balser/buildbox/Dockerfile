#  
# Buildbox image based off the official Centos image. Packages for CI, builds,  
# and deploys are installed. Langage specific images are built from this.  
#  
  
FROM centos:centos7  
MAINTAINER balser  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
  
# Build tools  
RUN yum -y install \  
autoconf \  
automake \  
bzip2 \  
bzr \  
fontconfig \  
gcc \  
gcc-c++ \  
git \  
groff \  
libtool \  
make \  
mercurial \  
openssl \  
pkgconfig \  
python-devel \  
python-docutils \  
python-pip \  
patch \  
tar \  
unzip \  
wget \  
&& yum clean all  
  
# Libraries  
RUN yum -y install \  
bison-devel \  
gdbm-devel \  
jemalloc-devel \  
libcurl-devel \  
libedit-devel \  
libffi-devel \  
libpng-dev \  
libxml2-devel \  
libxslt-devel \  
libyaml-devel \  
openssl-devel \  
ncurses-devel \  
pcre-devel \  
readline-devel \  
zlib-devel \  
&& yum clean all  
  
# Database clients  
RUN yum -y install \  
mariadb-devel \  
postgresql-devel \  
&& yum clean all  
  
# Packer  
RUN \  
cd /tmp && \  
curl -sOL
https://releases.hashicorp.com/packer/0.9.0/packer_0.9.0_linux_amd64.zip && \  
curl -sL https://releases.hashicorp.com/packer/0.9.0/packer_0.9.0_SHA256SUMS |
\  
grep packer_0.9.0_linux_amd64.zip | sha256sum -c - && \  
unzip packer_0.9.0_linux_amd64.zip -d /usr/local/bin && \  
rm packer_0.9.0_linux_amd64.zip  
  
# Install Node 6.4.0  
RUN rpm -ivh
https://rpm.nodesource.com/pub_6.x/el/7/x86_64/nodejs-6.4.0-1nodesource.el7.centos.x86_64.rpm  
  
# aws-cli is needed for uploading assets to S3  
RUN pip install awscli  
  
# gcloud tool - used for authenticating with Google Cloud and pushing to
Google Cloud Storage  
# Add Google Cloud SDK repo to yum repos  
ADD ./google-cloud-sdk.repo /etc/yum.repos.d/google-cloud-sdk.repo  
# Install gcloud  
RUN yum install -y google-cloud-sdk  
  
# Useful tools for manual testing and debugging  
RUN yum -y install \  
lsof \  
vim \  
tree \  
&& yum clean all  

