# FTP Public  
#  
# VERSION 0.1  
FROM debian:jessie  
MAINTAINER Romain Vermot <romain@vermot.eu>  
  
# Install vsftpd  
RUN apt-get update && apt-get install -y --no-install-recommends vsftpd  
RUN apt-get clean  
  
# Config vsftpd  
RUN sed -i "s/anonymous_enable=NO/anonymous_enable=YES/" /etc/vsftpd.conf  
RUN sed -i "s/local_enable=YES/local_enable=NO/" /etc/vsftpd.conf  
RUN sed -i "s/#write_enable=YES/write_enable=NO/" /etc/vsftpd.conf  
RUN sed -i "s/#anon_upload_enable=YES/anon_upload_enable=NO/" /etc/vsftpd.conf  
RUN sed -i "s/#anon_mkdir_write_enable=YES/anon_mkdir_write_enable=NO/"
/etc/vsftpd.conf  
RUN echo "anon_other_write_enable=NO" >> /etc/vsftpd.conf  
RUN sed -i
"s/secure_chroot_dir=\/var\/run\/vsftpd\/empty/secure_chroot_dir=\/public/"
/etc/vsftpd.conf  
RUN echo "anon_world_readable_only=YES" >> /etc/vsftpd.conf  
RUN echo "anon_root=/public" >> /etc/vsftpd.conf  
RUN echo "hide_ids=YES" >> /etc/vsftpd.conf  
RUN echo "pasv_min_port=50000" >> /etc/vsftpd.conf  
RUN echo "pasv_max_port=50100" >> /etc/vsftpd.conf  
  
RUN mkdir /public  
  
VOLUME /public  
  
EXPOSE 21  
EXPOSE 20  
EXPOSE 50000-50100  
CMD /usr/sbin/vsftpd  

