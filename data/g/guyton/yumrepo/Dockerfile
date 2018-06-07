FROM guyton/centos6  
RUN yum install -y createrepo httpd; yum clean all  
COPY update_repo /usr/bin/update_repo  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
EXPOSE 80  
CMD /usr/sbin/httpd -DFOREGROUND  
VOLUME /var/repo  

