FROM centos:7.3.1611  
MAINTAINER Søren Roug <soren.roug@eea.europa.eu>  
  
VOLUME /var/local/svn  
  
EXPOSE 80 443  
COPY entrypoint.sh /  
  
RUN chmod 755 /entrypoint.sh \  
&& yum install -y epel-release httpd mod_ssl mod_dav_svn subversion
mod_authz_ldap mod_ldap subversion-python  
  
CMD /entrypoint.sh  

