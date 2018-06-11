FROM uhurunet/fedora21  
MAINTAINER Uhurunet <support@uhurunet.com>  
  
RUN yum -y update  
RUN yum -y install mariadb-server bind-utils mlocate pwgen supervisor psmisc
net-tools hostname community-mysql  
  
ADD ./start.sh /start.sh  
ADD ./config_mariadb.sh /config_mariadb.sh  
ADD ./supervisord.conf /etc/supervisord.conf  
  
RUN mkdir /dbdata  
RUN rm -rf /var/lib/mysql  
RUN ln -s /dbdata /var/lib/mysql  
RUN chown -R mysql:mysql /dbdata*  
  
RUN chmod 755 /start.sh  
RUN chmod 755 /config_mariadb.sh  
  
EXPOSE 3306  
#CMD ["/bin/bash"]  
CMD ["/start.sh"]  

