FROM centos:7  
ENV LANG C.UTF-8  
LABEL author=ipple1986 email=ipple1986@gmail.com
site=https://zhaozhiwen.net.cn  
WORKDIR /opt/hexo  
RUN yum install -y epel-release && \  
yum install -y nodejs && npm config set registry
https://registry.npm.taobao.org \  
&& npm install hexo-cli -g && hexo init ipple1986 && cd ipple1986 && npm
install  
WORKDIR ipple1986  
EXPOSE 4000  
ENTRYPOINT ["hexo","server"]  
  

