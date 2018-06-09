#  
# build docker image to run the subversion  
#  
FROM centos:latest  
MAINTAINER XiangJL xjl-tommy@qq.com  
  
# install software  
RUN yum makecache fast && \  
yum install -y subversion httpd mod_dav_svn && \  
yum clean all && \  
sed -i 's/#ServerName www.example.com:80/ServerName 0.0.0.0:80/g'
/etc/httpd/conf/httpd.conf && \  
mkdir -p /subversion/config /subversion/logs /repos /docker  
  
COPY startup.sh /docker  
COPY subversion.conf /docker  
COPY authz.conf /docker  
  
VOLUME ["/subversion","/repos"]  
EXPOSE 80/tcp 443/tcp  
  
ENTRYPOINT ["/docker/startup.sh"]  

