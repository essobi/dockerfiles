FROM mariadb:5.5  
MAINTAINER Dustin Rue <dustin.rue@forumcomm.com>  
  
ADD backup.sh /usr/local/sbin/backup.sh  
ADD restore.sh /usr/local/sbin/restore.sh  
ADD showmake.sh /usr/local/sbin/showmake.sh  
RUN chmod +x /usr/local/sbin/*.sh && ln -s /usr/local/sbin/showmake.sh
/usr/local/sbin/showmake  
ADD Makefile /root/Makefile  
RUN mkdir /mnt/backup  

