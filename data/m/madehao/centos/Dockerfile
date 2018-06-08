FROM centos:7  
MAINTAINER madehao1983@sina.com  
  
ENV TZ="Asia/Shanghai"  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN yum update -y  
  
RUN localedef -f UTF-8 -i zh_CN zh_CN.UTF-8  
RUN sed -i "s/en_US/zh_CN/" /etc/locale.conf  
ENV LANG="zh_CN.UTF-8"  

