#  
# development tool box for Google Apps Script.  
#  
FROM ubuntu:14.04  
MAINTAINER tyskdm <tsuyoshi.kodama@gmail.com>  
#  
# apt update & locale setting  
#  
RUN apt-get update && \  
locale-gen en_US.UTF-8  
ENV LANG="en_US.UTF-8" \  
LANGUAGE="en_US:en" \  
LC_ALL="en_US.UTF-8"  
#  
# git  
#  
RUN apt-get install -y git  
#  
# Java  
#  
RUN apt-get install -y openjdk-7-jdk  
#  
# Google closure compiler  
# https://developers.google.com/closure/compiler/  
#  
# RUN mkdir /usr/local/closure-compiler  
ADD http://dl.google.com/closure-compiler/compiler-latest.tar.gz
/usr/local/closure-compiler/compiler-latest.tar.gz  
RUN tar xvfz /usr/local/closure-compiler/compiler-latest.tar.gz -C
/usr/local/closure-compiler && \  
chmod 644 /usr/local/closure-compiler/compiler.jar  
#  
# Google closure linter  
# https://developers.google.com/closure/utilities/docs/linter_howto  
#  
RUN apt-get install -y python-pip subversion && \  
pip install https://closure-linter.googlecode.com/svn/trunk/  
#  
# nvm  
#  
RUN apt-get install -y build-essential libssl-dev wget && \  
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh
| bash  
ENV BASH_ENV="/root/.nvm/nvm.sh"  

