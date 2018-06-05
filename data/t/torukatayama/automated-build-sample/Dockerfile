FROM centos:centos6  
RUN yum -y update  
RUN yum -y install vsftpd  
RUN cat /etc/vsftpd/vsftpd.conf | sed -e
"s/anonymous_enable=YES/anonymous_enable=NO/" -e
"s/#ascii_upload_enable=YES/ascii_upload_enable=YES/" -e
"s/#ascii_download_enable=YES/ascii_download_enable=YES/" -e
"s/#chroot_local_user=YES/chroot_local_user=YES/" -e
"s/#chroot_list_enable=YES/chroot_list_enable=YES/" -e
"s/#chroot_list_file=\/etc\/vsftpd\/chroot_list/chroot_list_file=\/etc\/vsftpd\/chroot_list/"
-e "s/#ls_recurse_enable=YES/ls_recurse_enable=YES/" > vsftpd.conf.new  
RUN echo "local_root=public_html" >> vsftpd.conf.new  
RUN echo "use_localtime=YES" >> vsftpd.conf.new  
RUN echo "background=NO" >> vsftpd.conf.new  
RUN /bin/cp vsftpd.conf.new /etc/vsftpd/vsftpd.conf  
RUN useradd demo  
RUN echo "demo" | passwd --stdin demo  
RUN usermod -G root demo  
RUN echo "demo" >> /etc/vsftpd/chroot_list  
ENTRYPOINT /usr/sbin/vsftpd  

