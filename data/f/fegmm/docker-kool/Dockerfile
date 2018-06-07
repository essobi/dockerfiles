FROM ubuntu:14.04  
  
EXPOSE 80  
# update and upgrade packages  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y mysql-server apache2 php5 php5-gd texlive-latex-
recommended php5-imap unzip wget php5-mysql samba-client  
RUN apt-get clean  
  
RUN mkdir /var/lib/kOOL && cd /var/lib/kOOL && wget
http://www.churchtool.org/fileadmin/user_upload/packages/kOOL_source_R45.zip
&& unzip kOOL_source_R45.zip  
RUN cd /var/lib/kOOL && wget https://github.com/smarty-
php/smarty/archive/v2.6.28.zip && unzip v2.6.28.zip  
ADD ko.inc /var/lib/kOOL/lib/inc/ko.inc  
ADD kOOL.js /var/lib/kOOL/lib/inc/kOOL.js  
ADD index.php /var/lib/kOOL/lib/admin/index.php  
ADD menu.php /var/lib/kOOL/lib/menu.php  
RUN mkdir /var/www/html/kOOL && cp /var/lib/kOOL/lib/install/kOOL_setup.sh
/var/www/html/kOOL && cd /var/www/html/kOOL && bash ./kOOL_setup.sh  
ADD kool.cron /etc/cron.d/kool  
RUN chown root:root /etc/cron.d/kool  
RUN chmod 0644 /etc/cron.d/kool  
RUN /usr/sbin/php5enmod imap  
RUN chmod 0777 /var/www/html/kOOL/download  
RUN chmod 0777 /var/www/html/kOOL/download/*  
  
ADD mrbs.zip /var/www/html/mrbs.zip  
RUN cd /var/www/html/ && unzip /var/www/html/mrbs.zip && rm
/var/www/html/mrbs.zip  
ADD config.inc.php /var/www/html/mrbs/config.inc.php  
RUN locale-gen de_DE.UTF-8 && update-locale LANG=de_DE.UTF-8  
  
RUN mkdir /data  
  
ADD ko-config.php /var/www/html/kOOL/config/ko-config.php  
ADD setup.sh /var/lib/kOOL/setup.sh  
RUN chmod 755 /var/lib/kOOL/setup.sh  
ADD startup.sh /var/lib/kOOL/startup.sh  
RUN chmod 755 /var/lib/kOOL/startup.sh  
  
CMD ["/var/lib/kOOL/startup.sh"]  

