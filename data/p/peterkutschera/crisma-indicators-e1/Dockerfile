# 2014-11-04  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-indicator_e1 .  
# docker run -P -d peterkutschera/crisma-indicator_e1  
FROM debian:7.7  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
RUN apt-get update && apt-get install -y apache2 python python-magic python-
requests python-dateutil vim curl && apt-get clean  
  
# If pythoin-requests is to olg get the newer version instead:  
# RUN apt-get install python-pip  
# RUN pip install requests  
COPY var/www /var/www/  
RUN cd /var/www/js && \  
curl -O http://code.jquery.com/jquery-2.0.3.min.js && \  
curl -O http://code.jquery.com/jquery-2.0.3.min.map && \  
curl -O https://code.angularjs.org/1.2.13/angular.min.js && \  
curl -O https://code.angularjs.org/1.2.13/angular.min.js.map  
  
COPY usr/local/wps /usr/local/wps/  
ADD pywps-3.2.1.tgz /usr/local/  
  
RUN chmod 777 /usr/local/pywps-3.2.1/pywps/Templates/1_0_0  
  
COPY usr/lib/* /usr/lib/cgi-bin/  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
WORKDIR /root  
  
COPY root/bin/runAll.sh /root/bin/runAll.sh  
COPY root/bin/registerAtOrion.py /root/bin/registerAtOrion.py  
RUN chmod +x /root/bin/*  
  
# CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
CMD ["/root/bin/runAll.sh"]  

