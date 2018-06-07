FROM centos:7  
RUN yum -y install epel-release  
  
RUN yum -y install gcc  
  
RUN yum -y install python-devel python-pip mysql-devel  
  
RUN pip install --upgrade pip  
  
RUN pip install virtualenv  
  
RUN yum -y install pcre pcre-devel pcre-static  
  
RUN yum -y clean all  
  
RUN mkdir /var/www  
  
COPY ./start.sh /  
  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  
  
EXPOSE 8000  

