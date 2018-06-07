FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV DH_VERSION="2.0.11"  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
# Add PostgreSQL's repository. It contains the most recent stable release of
PostgreSQL, ``9.4``.  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# install java8 & postgres  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common unzip
curl openssh-server \  
supervisor psmisc procps postgresql-9.4 postgresql-client-9.4 postgresql-
contrib-9.4 && \  
/bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
/bin/echo debconf shared/accepted-oracle-license-v1-1 seen true |
/usr/bin/debconf-set-selections && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.3`` package when it was ``apt-get installed``  
USER postgres  
  
# Create a PostgreSQL role named ``dhadmin`` with ``dhadmin_#911`` as the
password and  
# then create a database `dh` owned by the ``dhadmin`` role.  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER dhadmin WITH SUPERUSER PASSWORD 'dhadmin_#911';"
&& \  
createdb -O dhadmin dh  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.4/main/postgresql.conf``  
RUN sed -i 's/^local.*all.*postgres.*peer$/local all postgres trust/'
/etc/postgresql/9.4/main/pg_hba.conf && \  
sed -i 's/^local.*all.*all.*peer$/local all all md5/'
/etc/postgresql/9.4/main/pg_hba.conf && \  
echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
# Return to root user  
USER root  
  
#zookeeper+kafka  
ENV KAFKA_PARTITIONS 1  
RUN mkdir -p /opt/kafka/config && \  
curl -L -s
http://mirror.reverse.net/pub/apache/kafka/0.8.2.0/kafka_2.10-0.8.2.0.tgz \  
| tar -xzC /tmp/ && \  
mv -f /tmp/kafka_2.10-0.8.2.0/* /opt/kafka && \  
ln -s /opt/kafka /opt/zookeeper && \  
echo num.partitions=$KAFKA_PARTITIONS >> /opt/kafka/config/kafka.properties  
COPY kafka.properties /opt/kafka/config/  
COPY zookeeper.properties /opt/kafka/config/  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/var/data/zk-data", "/var/data/kafka-data", "/var/log/zk",
"/var/log/kafka"]  
  
#supervisor sshd  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN mkdir /var/run/sshd  
#RUN /bin/bash -c "echo -e
\"\n[inet_http_server]\nport=*:9001\nusername=dhadmin\npassword={SHA}$(echo -n
'dhadmin_#911' | sha1sum | awk '{print $1}')\" >>
/etc/supervisor/supervisord.conf"  
VOLUME ["/var/log/sshd", "/var/log/supervisor"]  
  
#start script  
COPY devicehive-init.sh /devicehive-init.sh  
RUN chmod +x /devicehive-init.sh  
  
#user for ssh  
RUN useradd -m -s /bin/bash -G sudo dhadmin  
RUN usermod --password $(echo "dhadmin_#911" | openssl passwd -1 -stdin)
dhadmin  
  
#nginx  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
COPY nginx.conf /etc/nginx/nginx.conf  
VOLUME ["/var/cache/nginx", "/var/log/nginx/"]  
  
#installing devicehive server  
COPY devicehive-server.properties /home/devicehive/devicehive-
server.properties  
RUN mkdir -p /home/devicehive/admin && \  
curl -L -s https://github.com/devicehive/devicehive-java-
server/releases/download/${DH_VERSION}/devicehive-${DH_VERSION}-boot.jar >
/home/devicehive/devicehive-server.jar  
  
#installing devicehive admin console  
RUN curl -L -s https://github.com/devicehive/devicehive-admin-
console/archive/2.0.4.tar.gz \  
| tar -xzC /tmp && \  
cp -r /tmp/devicehive-admin-console-2.0.4/* /home/devicehive/admin/  
RUN sed -i -e 's/restEndpoint.*/restEndpoint: location.origin +
\"\/api\/rest\"\,/' /home/devicehive/admin/scripts/config.js  
  
VOLUME ["/var/log/devicehive"]  
  
CMD ["/devicehive-init.sh"]  
  
EXPOSE 80 22 2181 5432 9001 9092  

