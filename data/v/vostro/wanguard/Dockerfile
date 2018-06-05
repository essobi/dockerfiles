  
FROM centos:7  
RUN yum update -y  
  
RUN rpm -Uvh https://www.andrisoft.com/files/redhat7/WANrepo-6.3-0.noarch.rpm
\  
&& yum install -y epel-release \  
&& yum install -y php-pecl-radius WANconsole socat \  
&& yum clean all && rm -rf /var/cache/yum  
  
VOLUME ["/opt/andrisoft/etc/", "/opt/andrisoft/dumps/",
"/opt/andrisoft/flows/"]  
  
RUN ln -s /opt/andrisoft/etc/andrisoft_apache.conf
/etc/httpd/conf.d/andrisoft_apache.conf &> /dev/null  
  
COPY startup.sh /startup.sh  
RUN chmod +x /startup.sh  
COPY install.sh /install.sh  
RUN chmod +x /install.sh  
CMD ["/startup.sh"]

