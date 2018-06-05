FROM centos:7  
LABEL maintainer="Steffen Vinther Sørensen <svinther@gmail.com>"  
  
RUN yum -y install epel-release \  
&& yum -y clean all  
  
RUN yum -y install httpd clamav clamav-server clamav-update python-argparse \  
&& yum -y clean all  
  
RUN freshclam  
  
RUN ln -s /dev/stdout /var/log/httpd/access_log \  
&& ln -s /dev/stderr /var/log/httpd/error_log  
  
ADD var /var  
ADD etc /etc  
ADD entrypoint.sh /  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["antivirus"]  
  

