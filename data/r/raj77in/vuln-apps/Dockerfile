FROM fedora  
  
# Setup mysql server  
RUN dnf install -y mariadb-server httpd php openssh-server unzip wget
java-1.8.0-openjdk hostname && dnf clean all;  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL utils  
ADD create_mysql_admin_user.sh /root/bin/create_mysql_admin_user.sh  
  
#Enviornment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
# VOLUME ["/etc/mysql", "/var/lib/mysql" ]  
# install sshd and apache  
RUN useradd -c "Vuln User" -m guest  
RUN echo "guest:guest"|chpasswd  
RUN echo "root:password" |chpasswd  
  
# Add DVWA  
#  
RUN mkdir -p /var/www/html/dvwa  
ADD https://github.com/ethicalhack3r/DVWA/archive/master.tar.gz
/var/www/html/dvwa/  
  
# Deploy Mutillidae  
RUN \  
mkdir /root/mutillidae && \  
cd /root/mutillidae && \  
wget -O /root/mutillidae/mutillidae.zip
http://sourceforge.net/projects/mutillidae/files/latest/download && \  
unzip /root/mutillidae/mutillidae.zip && \  
cp -r /root/mutillidae/mutillidae /var/www/html/ && \  
rm -rf /root/mutillidae  
  
RUN \  
sed -i 's/static public \$mMySQLDatabaseUsername =.*/static public
\$mMySQLDatabaseUsername = "admin";/g'
/var/www/html/mutillidae/classes/MySQLHandler.php && \  
echo "sed -i 's/static public \$mMySQLDatabasePassword =.*/static public
\$mMySQLDatabasePassword = \\\\\"'\$PASS'\\\\\";/g'
/var/www/html/mutillidae/classes/MySQLHandler.php" >>
//root/bin/create_mysql_admin_user.sh  
  
# Add webgoat  
RUN mkdir /root/webgoat  
# RUN cd /root/webgoat; curl
'https://github.com/WebGoat/WebGoat/releases/download/7.1/webgoat-
container-7.1-exec.jar' -O -J -L  
RUN cd /root/webgoat; curl
'https://github.com/WebGoat/WebGoat/releases/download/v8.0.0.M5/webgoat-
server-8.0.0.M5.jar' -O -J -L  
RUN cd /root/webgoat; curl
'https://github.com/WebGoat/WebGoat/releases/download/v8.0.0.M5/webwolf-8.0.0.M5.jar'
-O -J -L  
  
# Run DVNA  
## <aka> ## ENV VERSION master  
## <aka> ## RUN dnf install -y tar npm ; dnf clean all;  
## <aka> ## WORKDIR /DVNA-$VERSION/  
## <aka> ## RUN useradd -d /DVNA-$VERSION/ dvna \  
## <aka> ## && chown dvna: /DVNA-$VERSION/  
## <aka> ## USER dvna  
## <aka> ## RUN curl -sSL
'https://github.com/raj77in/dvna-1/archive/master.tar.gz' \  
## <aka> ## | tar -vxz -C /DVNA-$VERSION/ \  
## <aka> ## && cd /DVNA-$VERSION/dvna-1-master \  
## <aka> ## && npm set progress=false \  
## <aka> ## && npm install  
# Add commix  
RUN mkdir /var/www/html/commix  
ADD https://github.com/commixproject/commix/archive/master.tar.gz
/var/www/html/commix  
  
# Fix mariadb issue  
RUN rm -rf /etc/my.cnf.d/auth_gssapi.cnf ; rm -rf /var/lib/mysql; echo -e
'innodb_buffer_pool_size=16M\ninnodb_additional_mem_pool_size=500K\ninnodb_log_buffer_size=500K\ninnodb_thread_concurrency=2'
>>/etc/my.cnf.d/mariadb-server.cnf  
RUN chown -R mysql /var/lib/mysql/ ; mysql_install_db --user=mysql
--ldata=/var/lib/mysql;  
# RUN mkdir -p /var/lib/mysql/; chown -R mysql /var/lib/mysql/ ; cd
/var/lib/mysql; /usr/libexec/mysqld --initialize-insecure --user=mysql
--datadir=/var/lib/mysql  
# Extract the tar files:  
## <aka> ## RUN dnf install -y tar python2 ; dnf clean all;  
## <aka> ## RUN cd /var/www/html/dvwa/; tar xvf master.tar.gz ; cd DVWA-
master; cp config/config.inc.php.dist config/config.inc.php  
## <aka> ## RUN cd /var/www/html/commix/; tar xvf master.tar.gz  
## OWASP Bricks  
RUN wget -O /var/www/html/bricks.zip
'http://sourceforge.net/projects/owaspbricks/files/Tuivai%20-%202.2/OWASP%20Bricks%20-%20Tuivai.zip/download'  
RUN mkdir /var/www/html/owasp-bricks; cd /var/www/html/owasp-bricks; unzip
/var/www/html/bricks.zip  
  
RUN dnf install -y php-mysqlnd php-gd  
RUN cd /var/www/html/dvwa; tar xvf master.tar.gz; cd DVWA-master/; mv
config/config.inc.php{.dist,}  
  
ADD start.sh /root/bin  
# Add index file  
ADD index.html /var/www/html  
  
RUN chmod +x /root/bin/*.sh  
  
EXPOSE 22 80 8080 3000 3306  
CMD "/root/bin/start.sh"  

