FROM lolhens/baseimage:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
RUN apt-get update \  
&& cd "/tmp" \  
&& curl http://vestacp.com/pub/vst-install.sh | bash -s -- \  
-y no -f \  
\--password admin \  
\--nginx yes --apache yes --phpfpm no \  
\--vsftpd no --proftpd no \  
\--exim yes --dovecot yes --spamassassin yes --clamav yes \  
\--named yes \  
\--iptables no --fail2ban no \  
\--mysql no --postgresql yes \  
\--remi yes \  
\--quota yes \  
&& cleanimage  
  
ADD dovecot /etc/init.d/dovecot  
RUN chmod +x /etc/init.d/dovecot  
  
RUN cd /usr/local/vesta/data/ips && mv * 127.0.0.1 \  
&& cd /etc/apache2/conf.d && sed -i -- 's/172.*.*.*:80/127.0.0.1:80/g' * &&
sed -i -- 's/172.*.*.*:8443/127.0.0.1:8443/g' * \  
&& cd /etc/nginx/conf.d && sed -i -- 's/172.*.*.*:80;/80;/g' * && sed -i --
's/172.*.*.*:8080/127.0.0.1:8080/g' * \  
&& cd /home/admin/conf/web && sed -i -- 's/172.*.*.*:80;/80;/g' * && sed -i --
's/172.*.*.*:8080/127.0.0.1:8080/g' *  
  
ADD startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
CMD bash  
  
EXPOSE 80 8083 3306 443 25 993 110 53 54  

