FROM debian:jessie  
MAINTAINER Peter van Heusden <pvh@sanbi.ac.za>  
  
RUN apt-get update  
RUN apt-get install -y wget  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -O /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" \  
&& wget -O /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu  
  
# Install PostgreSQL 9.3.6 pre-requisites  
RUN apt-get install -y libc6 sudo libssl1.0.0 libfuse2 libjson-perl perl
python openssl python-psutil python-requests lsof python-jsonschema  
RUN apt-get install -y unixodbc odbc-postgresql postgresql-client super libc6
perl  
  
RUN wget ftp://ftp.renci.org/pub/irods/releases/4.1.8/ubuntu14/irods-
icat-4.1.8-ubuntu14-x86_64.deb  
RUN dpkg -i irods-icat-4.1.8-ubuntu14-x86_64.deb  
RUN wget ftp://ftp.renci.org/pub/irods/releases/4.1.8/ubuntu14/irods-database-
plugin-postgres-1.8-ubuntu14-x86_64.deb  
RUN dpkg -i irods-database-plugin-postgres-1.8-ubuntu14-x86_64.deb  
  
# Edit sudoers file  
# To avoid error: sudo: sorry, you must have a tty to run sudo  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
ADD scripts /scripts  
WORKDIR /scripts  
RUN chmod a+x *.sh  
  
ADD waitforit.sh /usr/local/bin/waitforit.sh  
RUN chmod a+x /usr/local/bin/waitforit.sh  
  
# Open firewall for iRODS  
EXPOSE 1247 1248 20000-20199  
ENTRYPOINT [ "/scripts/bootstrap.sh" ]  

