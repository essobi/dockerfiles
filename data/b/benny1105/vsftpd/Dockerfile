from ubuntu:16.04  
ENV REFRESHED_AT=2018-01-30  
user root  
copy ftp.sh /ftp.sh  
copy Shanghai /usr/share/zoneinfo/Asia/Shanghai  
copy sources.list /etc/apt/sources.list  
run apt-get update -qq && apt-get install -yqq --no-install-recommends vsftpd
libpam-pwdfile apache2-utils\  
&& mv /etc/localtime /etc/localtime.bak && ln -s
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apt-get autoclean && rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/locale/* && rm -rf /usr/share/man/* \  
&& rm -rf /usr/share/doc/* \  
&& mkdir -p /var/run/vsftpd/empty /etc/vsftpd/vir_user_conf /data/ftp \  
&& chown -R ftp.ftp /data/ftp \  
&& chmod 700 /ftp.sh  
volume ["/data/ftp", "/etc/vsftpd"]  
copy pam_vsftpd /etc/pam.d/vsftpd  
copy vsftpd.conf /etc/vsftpd.conf  
entrypoint ["/ftp.sh"]  
cmd ["vsftpd"]  
expose 21 28990-28999  

