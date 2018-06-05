FROM ppodgorsek/httpd-custom-configuration:2.4.0  
MAINTAINER Paul Podgorsek <ppodgorsek@users.noreply.github.com>  
LABEL description Httpd load-balancer with SSL termination in Docker  
  
EXPOSE 443  
ENV BACKEND_HOSTS localhost  
ENV BACKEND_PORT 8009  
ENV BACKEND_PROTOCOL ajp  
  
ENV SSL_KEY_FILE localhost.key  
ENV SSL_CRT_FILE localhost.crt  
  
RUN dnf upgrade -y\  
&& dnf install -y\  
mod_ssl-1:2.4.29-*\  
iputils\  
&& dnf clean all  
  
RUN mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/001-ssl.conf\  
&& rm -f /etc/httpd/conf.d/README\  
/etc/httpd/conf.d/autoindex.conf\  
/etc/httpd/conf.d/welcome.conf  
  
COPY ssl/* /opt/ssl/  
COPY conf/* /httpd-conf-fragments/  
  
COPY scripts/assemble-conf-fragments.sh /usr/local/bin/  
  
CMD ["assemble-conf-fragments.sh"]  

