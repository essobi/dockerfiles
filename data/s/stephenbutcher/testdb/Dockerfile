FROM centos:centos7  
MAINTAINER stephen.butcher@redhound.net  
  
# Copy only files required for the following RUN commands (leverage Docker
caching)  
COPY container-files/etc/yum.repos.d/* /etc/yum.repos.d/  
  
RUN \  
yum update -y && \  
yum install -y epel-release && \  
yum install -y MariaDB-server MariaDB-connect-engine MariaDB-compat hostname
net-tools pwgen freetds openssh-server openssh-clients && \  
yum clean all && \  
rm -rf /var/lib/mysql/*  
  
# Add all remaining files to the container  
COPY container-files /  
RUN chmod 755 /etc/my.cnf.d /etc/yum.repos.d  
RUN chmod 644 /etc/yum.repos.d/mariadb.repo /etc/my.cnf.d/*.cnf  
COPY oraclient.tar.gz /tmp/  
RUN cd /usr/lib64; tar xzf /tmp/oraclient.tar.gz  
RUN echo "[Oracle ODBC driver]" >> /etc/odbcinst.ini  
RUN echo "Description = ODBC for Oracle" >> /etc/odbcinst.ini  
RUN echo "Driver = /usr/lib64/libsqora.so.12.1">> /etc/odbcinst.ini  
RUN echo "">> /etc/odbcinst.ini  
RUN echo "[FreeTDS]">> /etc/odbcinst.ini  
RUN echo "Description=FreeTDS MSSQL Driver">> /etc/odbcinst.ini  
RUN echo "Driver=/usr/lib64/libtdsodbc.so.0">> /etc/odbcinst.ini  
RUN echo "Setup=/usr/lib64/libtdsS.so.2">> /etc/odbcinst.ini  
RUN echo "">> /etc/odbcinst.ini  
RUN odbcinst -i -d -f /etc/odbcinst.ini  
RUN rm /tmp/oraclient.tar.gz  
RUN /usr/sbin/useradd vagrant -u 500 -U -G wheel  
RUN echo 'root:RedH0und$' | chpasswd && echo 'vagrant:vagrant' | chpasswd  
  
# RUN /etc/rc.d/init.d/sshd start # -- use manually if required, works but
gives error message!  
# Add VOLUME to allow backup of data  
VOLUME ["/var/lib/mysql"]  
  
# Set TERM env to avoid mysql client error message "TERM environment variable
not set" when running from inside the container  
ENV TERM xterm  
# set ROVERMODE env to a default value of PROD - can be changed at run time  
ENV ROVERMODE PROD  
ENV DBNAME Rover  
  
EXPOSE 3306 22  
CMD ["/run.sh"]  

