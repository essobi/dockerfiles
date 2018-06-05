FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y mc wget build-essential netcat
libreadline6-dev zlib1g-dev liblzo2-dev mt-st mtx postfix libacl1-dev libssl-
dev postgresql-server-dev-9.5 postgresql-client-9.5 sudo python-setuptools &&
\  
wget -qO- http://bacula.us/741 | tar -xzvf - -C /usr/src && \  
cd /usr/src/bacula* && \  
./configure --with-readline=/usr/include/readline --disable-conio
--bindir=/usr/bin --sbindir=/usr/sbin \  
\--with-scriptdir=/etc/bacula/scripts --with-working-dir=/var/lib/bacula
--with-logdir=/var/log \  
\--enable-smartalloc --with-postgresql --with-archivedir=/mnt/backup && \  
make -j8 && make install && mkdir /var/log/supervisor/ &&
/usr/bin/easy_install supervisor && /usr/bin/easy_install supervisor-stdout &&
/usr/bin/easy_install supervisor-logging && \  
mkdir -p /var/run/bacula && mkdir -p /var/log/bacula && mkdir /bacula  
  
ADD create_postgresql_database /  
ADD make_postgresql_tables /  
ADD initialize /  
ADD supervisord.conf /etc/supervisord.conf  
  
VOLUME [ "/etc/bacula", "/bacula" ]  
  
EXPOSE 9101 9103  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

