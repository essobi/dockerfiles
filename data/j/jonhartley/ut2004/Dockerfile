FROM jonhartley/c7-systemd  
  
COPY configcreate.service /etc/systemd/system/configcreate.service  
COPY configcreate.sh /configcreate.sh  
COPY UT2004.ini /root/UT2004.ini  
COPY ut2004.service /etc/systemd/system/ut2004.service  
  
RUN mkdir -p /usr/local/ut2004; \  
yum -y install epel-release; \  
yum -y install unzip libstdc++ libstdc++.i686 compat-libstdc++-33.i686 compat-
libstdc++-33 tar bzip2 psmisc; \  
yum -y install httpd httpd-tools php php-mysql php-gd mariadb-server; \  
curl -o /root/ut2004.zip
http://ut2004.familyhartley.com/DedicatedServer3339-BonusPack.zip ; \  
curl -o /root/utstatsdb.tar.bz2
http://ut2004.familyhartley.com/utstatsdb-3.06.tar.bz2; \  
unzip -q /root/ut2004.zip -d /usr/local/ut2004; \  
tar -xjf /root/utstatsdb.tar.bz2 -C /var/www/html --strip 1; \  
yum clean all; \  
rm -rf /var/cache/yum; \  
rm -f /root/ut2004.zip; \  
usermod -s /bin/bash apache; \  
chown -R apache:apache /usr/local/ut2004/; \  
chown -R apache:apache /var/www/html/; \  
chmod +x /usr/local/ut2004/System/ucc-bin-linux-amd64; \  
cp -f /root/UT2004.ini /usr/local/ut2004/System/UT2004.ini; \  
ln -sf /usr/local/ut2004/UserLogs /var/www/html/Logs; \  
systemctl enable httpd; \  
systemctl daemon-reload; \  
systemctl enable ut2004.service; \  
systemctl enable configcreate.service  
  
EXPOSE 7777/udp 7778/udp 7787/udp 3306 80 8080  
  
ENTRYPOINT ["/usr/sbin/init"]  
  
  
  
  

