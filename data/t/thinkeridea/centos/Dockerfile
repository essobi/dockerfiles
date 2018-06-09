FROM centos:6.6  
  
MAINTAINER thinkeridea <thinkeridea@sina.com>  
  
COPY ./gosu/gosu-amd64 /usr/local/bin/gosu  
COPY ./gosu/gosu-amd64.asc /tmp/gosu.asc  
  
ENV GOSU_VERSION 1.7  
  
RUN set -ex \  
# 使用阿里yum源，安装wget  
&& curl http://mirrors.aliyun.com/repo/Centos-6.repo -o
/etc/yum.repos.d/CentOS-Base.repo \  
&& yum clean all \  
&& yum install -y wget \  
\  
# 安装配置gosu  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch \--verify /tmp/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /tmp/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
\  
# clear  
&& yum clean all  

