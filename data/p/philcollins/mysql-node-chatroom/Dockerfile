# Latest version of centos  
FROM centos:centos7  
MAINTAINER Steve Salevan <steve@spi.ne>  
  
ADD . /chatroom  
  
RUN curl -sL -o ns.rpm
https://rpm.nodesource.com/pub_6.x/el/7/x86_64/nodejs-6.2.0-1nodesource.el7.centos.x86_64.rpm
\  
&& rpm -i --nosignature --force ns.rpm \  
&& rm -f ns.rpm  
  
RUN npm install -g pangyp\  
&& ln -s $(which pangyp) $(dirname $(which pangyp))/node-gyp\  
&& npm cache clear\  
&& node-gyp configure || echo ""  
  
RUN yum -y update && \  
yum -y install epel-release && \  
yum install -y cyrus-sasl-md5 libcurl subversion  
  
RUN cd /chatroom && npm install  

