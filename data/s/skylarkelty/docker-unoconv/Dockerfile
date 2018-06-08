FROM centos:latest  
  
MAINTAINER "Skylar Kelty" <s.kelty@kent.ac.uk>  
  
RUN yum install -y libreoffice libreoffice-pyuno libreoffice-ure && yum clean
all  
RUN curl -SsL
https://raw.githubusercontent.com/dagwieers/unoconv/master/unoconv >
/usr/local/bin/unoconv  
RUN chmod 0755 /usr/local/bin/unoconv  
  
EXPOSE 2002  
CMD ["/usr/local/bin/unoconv", "--listener"]  

