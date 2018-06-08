FROM debian:latest  
MAINTAINER Udo Meijer (udo.meijer@gmail.com)  
  
RUN apt-get update \  
&& apt-get install -y apache2 libapache2-mod-security2 \  
&& rm -r /var/lib/apt/lists/*  
  
RUN a2enmod security2  
  
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf  
COPY security2.conf /etc/apache2/mods-enabled/security2.conf  
  
RUN for f in `ls /usr/share/modsecurity-crs/base_rules/` ; do ln -s
/usr/share/modsecurity-crs/base_rules/$f /usr/share/modsecurity-
crs/activated_rules/$f ; done  
  
EXPOSE 80  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  

