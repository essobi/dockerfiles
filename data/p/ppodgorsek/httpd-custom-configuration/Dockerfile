FROM fedora:27  
MAINTAINER Paul Podgorsek <ppodgorsek@users.noreply.github.com>  
LABEL description httpd in Docker with custom configuration  
  
EXPOSE 80  
ENV SERVER_NAME localhost  
  
RUN dnf upgrade -y\  
&& dnf install -y httpd-2.4.29-1.fc27.x86_64\  
&& dnf clean all  
  
COPY scripts/define-server-name-and-start.sh /usr/local/bin/  
  
CMD ["define-server-name-and-start.sh"]  

