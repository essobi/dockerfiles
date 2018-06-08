FROM selenium/standalone-chrome  
MAINTAINER Tim Perry <pimterry@gmail.com>  
  
USER root  
  
# Install and configure an anonymous FTP server  
RUN apt-get update \  
&& apt-get install vsftpd \  
&& mkdir -p /var/run/vsftpd/empty \  
&& mkdir -p /var/ftp/uploaded \  
&& chmod a+rw /var/ftp/uploaded  
  
ADD vsftpd.conf /etc/vsftpd.conf  
  
# Update the default selenium entry_point script to also start vsftpd  
RUN sed -i '/xvfb-run/i vsftpd &' /opt/bin/entry_point.sh  
  
EXPOSE 21

