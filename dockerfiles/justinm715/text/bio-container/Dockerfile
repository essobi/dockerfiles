FROM centos:centos7
MAINTAINER Justin Martinez <justinm715@gmail.com>

RUN yum update -y
RUN yum install -y git tar

# install rvm, ruby
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
RUN \curl -sSL https://get.rvm.io | bash -s stable
RUN \source /etc/profile.d/rvm.sh
RUN /bin/bash -l -c 'rvm requirements'
RUN /bin/bash -l -c 'rvm install 2.2.0'
