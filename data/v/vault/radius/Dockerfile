FROM alpine:3.6  
  
RUN apk update && \  
apk add --update freeradius freeradius-mysql php5 php5-ctype mysql-client bash
coreutils && \  
chgrp radius /var/run/radius && chmod g+rwx /var/run/radius && \  
mkdir /opt && cd /opt && \  
wget http://download.multiotp.net/multiotp_5.0.4.8.zip -O multiotp.zip && \  
unzip multiotp.zip -q && \  
rm -rf windows sources raspberry multiotp.zip && \  
chmod +x /opt/linux/multiotp.php && \  
mv /opt/linux /opt/multiotp && \  
ln -s /usr/bin/php5 /usr/bin/php && \  
rm /etc/localtime && \  
rm /var/cache/apk/*  
  
EXPOSE 1812/udp 1813/udp  
  
CMD radiusd -f -l stdout  

