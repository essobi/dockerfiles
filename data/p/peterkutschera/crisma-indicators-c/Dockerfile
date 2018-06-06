# 2014-11-04  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-indicators-c .  
# docker run -P -d peterkutschera/crisma-indicator_c  
# Test:  
# docker run -t -i -P peterkutschera/indicator_c /bin/bash  
# apache2ctl start  
# tail -f /var/log/apache2/error.log &  
FROM debian:7.7  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
RUN apt-get update && apt-get install -y apache2 python python-magic python-
requests python-dateutil curl vim && apt-get clean  
  
# If pythoin-requests is too old get the newer version instead:  
# RUN apt-get install python-pip  
# RUN pip install requests  
COPY var/www /var/www/  
COPY usr/local/wps /usr/local/wps/  
ADD pywps-3.2.1.tgz /usr/local/  
  
RUN chmod 777 /usr/local/pywps-3.2.1/pywps/Templates/1_0_0  
  
COPY usr/lib/* /usr/lib/cgi-bin/  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# RUN /bin/ln -sf ../sites-available/default-ssl /etc/apache2/sites-
enabled/001-default-ssl  
# RUN /bin/ln -sf ../mods-available/ssl.conf /etc/apache2/mods-enabled/  
# RUN /bin/ln -sf ../mods-available/ssl.load /etc/apache2/mods-enabled/  
EXPOSE 80  
# EXPOSE 443  
WORKDIR /root  
  
COPY root/bin/runAll.sh /root/bin/runAll.sh  
COPY root/bin/registerAtOrion.py /root/bin/registerAtOrion.py  
COPY root/bin/registerAtOrion2.py /root/bin/registerAtOrion2.py  
RUN chmod +x /root/bin/*  
  
# CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
CMD ["/root/bin/runAll.sh"]  

