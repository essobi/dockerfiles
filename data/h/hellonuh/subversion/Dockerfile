FROM oraclelinux:7-slim  
LABEL maintainer="nuhaque@gmail.com"  
  
RUN yum install -y httpd subversion mod_dav_svn && \  
yum clean all && rm -rf /var/cache/yum && \  
mkdir -p /var/local/svn && \  
mkdir /etc/httpd/dav_svn  
  
ADD files/dav_svn.conf /etc/httpd/conf.modules.d/  
ADD files/dav_svn.authz /etc/httpd/dav_svn/  
ADD files/svn-project-creator.sh /usr/local/bin/  
ADD files/svn-entrypoint.sh /usr/local/bin/  
  
RUN chmod a+x /usr/local/bin/svn*  
VOLUME ["/var/local/svn", "/etc/httpd/dav_svn"]  
  
CMD ["svn-entrypoint.sh"]  

