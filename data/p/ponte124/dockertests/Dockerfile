FROM debian:wheezy  
MAINTAINER diego.souto@altia.es  
  
RUN apt-get -y update && apt-get -y install apache2 php5 libapache2-mod-php5
php5-mysql php5-gd php5-curl && rm -rf /var/lib/apt/lists/* && update-rc.d
apache2 disable && sed -i -E 's,(ErrorLog ).+,\1\/dev\/stderr,g'
/etc/apache2/sites-available/default && sed -i -E 's,(CustomLog
).+,\1\/dev\/stdout combined,g' /etc/apache2/sites-available/default  
  
ENTRYPOINT [ "/usr/sbin/apache2ctl" ]  
CMD [ "-D", "FOREGROUND" ]  
  
EXPOSE 80  
#docker run -d -p 80 --log-driver=syslog 4f1f26eccd64  

