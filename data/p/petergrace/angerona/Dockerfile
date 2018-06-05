FROM dockerfile/python  
MAINTAINER Peter Grace, pete.grace@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y supervisor unixodbc-dev tdsodbc freetds-dev freetds-bin
freetds-common unixodbc libgmp-dev nginx  
  
RUN /bin/sed -i '1s#^#daemon off\;\n#' /etc/nginx/nginx.conf  
  
RUN ["mkdir", "-p", "/opt/angerona"]  
  
ADD docker/supervisor-angerona.conf /etc/supervisor/conf.d/angerona.conf  
ADD docker/supervisor-system.conf /etc/supervisor/conf.d/system.conf  
ADD docker/supervisor-nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD docker/supervisor-makecert.conf /etc/supervisor/conf.d/makecert.conf  
  
ADD . /opt/angerona/  
WORKDIR /opt/angerona  
#nginx config file  
ADD docker/nginx-ssl.conf /etc/nginx/conf.d/ssl.conf  
ADD docker/angerona-ossl.cnf /opt/angerona/angerona-ossl.cnf  
ADD docker/makeCert.sh /opt/angerona/makeCert.sh  
ADD docker/angerona-sqlite-blank /opt/angerona/angerona.sqlite  
RUN ["python", "setup.py", "install"]  
  
CMD ["/usr/bin/supervisord"]  
EXPOSE 443  

