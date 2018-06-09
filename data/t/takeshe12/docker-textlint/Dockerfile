FROM centos:7.4.1708  
LABEL maintainer "tk117 <kondo.takeshi@jp.fujitsu.com>"  
  
RUN yum update -y  
RUN yum install -y epel-release  
RUN yum install -y \  
gcc-c++ \  
make \  
nodejs \  
npm  
  
RUN npm install -g \  
textlint \  
textlint-rule-preset-ja-technical-writing \  
textlint-rule-preset-jtf-style \  
textlint-rule-preset-ja-spacing \  
textlint-rule-spellcheck-tech-word  

