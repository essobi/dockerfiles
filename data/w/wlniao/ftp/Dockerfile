FROM damienlagae/debian-base  
MAINTAINER Damien Lagae <damien@lagae.info>  
  
# Set the enviroment variable  
ENV FTP_USER wlniao  
ENV FTP_PASS 123456  
# Install required packages  
RUN apt-get clean all && apt-get update && apt-get -y dist-upgrade  
RUN apt-get -y install vsftpd db5.3-util  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Configure vsftpd  
RUN mkdir -p /var/run/vsftpd/empty && mkdir -p /etc/vsftpd && mkdir -p
/var/ftp  
  
# Add the Configurations files  
ADD conf/vsftpd.conf /etc/vsftpd.conf  
ADD conf/vsftpd.virtual /etc/pam.d/vsftpd.virtual  
ADD conf/supervisord-ftp.conf /etc/supervisor/conf.d/supervisord-ftp.conf  
  
# Add shell scripts for starting ftp  
ADD shell/ftpuser.sh /ftpuser.sh  
ADD shell/run.sh /run.sh  
  
# Give the right permissions  
RUN chmod 755 /*.sh  
RUN chmod 777 /var/ftp  
  
# Add volumes for ftp  
VOLUME ["/var/ftp"]  
  
# Set the port  
EXPOSE 21 12020 12021 12022 12023  
# Run  
CMD ["/run.sh"]  

