FROM alpine  
  
RUN apk add --no-cache git nodejs mysql mysql-client python make g++  
  
RUN cd \  
&& git clone https://github.com/GladysProject/gladys gladys \  
&& cd gladys \  
&& npm install \  
&& npm install -g grunt-cli \  
&& grunt buildProd  
  
COPY .env /root/gladys/.env  
  
WORKDIR /root/gladys  
  
RUN /usr/bin/mysql_install_db --user=mysql  
RUN /usr/bin/mysqld_safe --datadir='/var/lib/mysql' & sleep 20 \  
&& /usr/bin/mysqladmin -u root password 'root' \  
&& mysql --user=root --password=root -e "CREATE DATABASE gladys ;" \  
&& node init.js  
  
EXPOSE 8080  
COPY run.sh /root/gladys/run.sh  
RUN chmod +x run.sh  
  
CMD ["/root/gladys/run.sh"]  

