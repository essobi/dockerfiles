FROM debian:stretch  
MAINTAINER Patrick Laurin <plaurin@inocybe.ca>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y install \  
apache2 \  
libapache2-mod-auth-mellon  
  
RUN a2enmod \  
ssl \  
rewrite \  
headers \  
proxy \  
proxy_http \  
proxy_wstunnel \  
auth_mellon \  
authn_core \  
authz_user  
  
RUN a2ensite default-ssl  
  
EXPOSE 80  
EXPOSE 443  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

