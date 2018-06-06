FROM debian:latest  
MAINTAINER Christian U. <info@cu-tec.de>  
# Installing packages  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install wget sqlite3 bsdiff libsane mysql-client postgresql-client
unzip nano libgtk2.0-0 fonts-liberation -y  
RUN wget http://downloads.free-erp.de/promet-erp-
services_7.0.439_amd64-gtk2.deb --level=23709 && dpkg -i promet-erp-
services_7.0.439_amd64-gtk2.deb && rm promet-erp-
services_7.0.439_amd64-gtk2.deb  
RUN wget http://downloads.free-erp.de/tools_x86_64-linux-7.0.439.zip
--level=23709 && unzip -o tools_x86_64-linux-7.0.439.zip -d /usr/lib/promet-
erp  
RUN apt-get clean && apt-get autoremove -y  
EXPOSE 8085  
VOLUME ["/usr/lib/promet-erp/web"]  
COPY entrypoint.sh /opt/entrypoint.sh  
RUN ["chmod", "+x", "/opt/entrypoint.sh"]  
ENTRYPOINT ["/opt/entrypoint.sh"]  

