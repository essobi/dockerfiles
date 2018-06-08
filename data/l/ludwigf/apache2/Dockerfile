FROM fedora:21  
MAINTAINER "Florian Ludwig" <f.ludwig@greyrook.com>  
  
COPY ./install.sh /  
COPY ./page.conf /etc/httpd/conf.d/page.conf  
  
RUN /install.sh  
COPY ./run.sh /  
  
CMD ["/run.sh"]  
  

