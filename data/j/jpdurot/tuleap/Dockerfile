FROM centos:6.6  
# Dockerfile built from information at :
https://tuleap.net/doc/en/installation-guide/full-installation.html  
RUN yum install -y epel-release wget  
  
RUN echo '[Tuleap]' > /etc/yum.repos.d/tuleap.repo  
RUN echo 'name=Tuleap' >> /etc/yum.repos.d/tuleap.repo  
RUN echo 'baseurl=http://ci.tuleap.net/yum/tuleap/rhel/6/dev/\$basearch' >>
/etc/yum.repos.d/tuleap.repo  
RUN echo 'enabled=1' >> /etc/yum.repos.d/tuleap.repo  
RUN echo 'gpgcheck=0' >> /etc/yum.repos.d/tuleap.repo  
  
RUN yum install -y \  
tuleap-install \  
tuleap-all \  
tuleap-plugin-git-gitolite3 \  
tuleap-plugin-agiledashboard \  
tuleap-customization-default \  
tuleap-theme-flamingparrot-1.142 \  
mysql-server \  
python-setuptools \  
postfix  
  
RUN yum clean all  
  
RUN easy_install supervisor  
  
RUN service mysqld start && mysqladmin -u root password root  
  
RUN service mysqld start && /usr/share/tuleap-install/setup.sh \  
\--sys-default-domain=mytuleaphost \  
\--sys-org-name=MyOrganization \  
\--sys-long-org-name=MyOrganization \  
\--mysql-host=localhost \  
\--mysql-user=root \  
\--mysql-user-password=root \  
\--disable-domain-name-check  
  
COPY supervisord.conf /etc/supervisord.conf  
COPY app /app  
  
RUN chmod u+x /app/*.sh  
  
EXPOSE 443  
ENV TULEAP_HOSTNAME tuleap  
ENV MYSQL_HOST localhost  
  
CMD ["/app/run.sh"]  

