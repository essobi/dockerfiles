# Dockerfile BareOS client/file daemon  
FROM debian:stretch  
MAINTAINER Brightside <sweetdimensions@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y install curl software-properties-common gnupg
wget  
  
RUN curl -Ls
http://download.bareos.org/bareos/release/latest/Debian_9.0/Release.key | apt-
key --keyring /etc/apt/trusted.gpg.d/bareos-keyring.gpg add - && \  
curl -Ls http://download.bareos.org/bareos/contrib/Debian_9.0/Release.key |
apt-key --keyring /etc/apt/trusted.gpg.d/bareos-keyring.gpg add - && \  
curl -Ls https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
--keyring /etc/apt/trusted.gpg.d/postgres-keyring.gpg add - && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8 &&
\  
echo 'deb http://download.bareos.org/bareos/release/latest/Debian_9.0/ /' >
/etc/apt/sources.list.d/bareos.list && \  
echo 'deb http://download.bareos.org/bareos/contrib/Debian_9.0/ /' >>
/etc/apt/sources.list.d/bareos.list && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >>
/etc/apt/sources.list.d/postgres.list && \  
echo 'deb [arch=amd64,i386] http://mirror.klaus-
uwe.me/mariadb/repo/10.2/debian stretch main' >>
/etc/apt/sources.list.d/mysql.list && \  
apt-get update -qq && \  
apt-get install -qq -y bareos-client postgresql-client mysql-client && \  
apt-get clean && \  
curl -Lsk
https://github.com/bareos/bareos/blob/master/src/cats/make_catalog_backup.pl.in
-o /usr/lib/bareos/scripts/make_catalog_backup.pl  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod u+x /docker-entrypoint.sh  
RUN tar cfvz /bareos-fd.tgz /etc/bareos/bareos-fd.d  
  
RUN mkdir /etc/bareos/scripts  
COPY scripts/* /etc/bareos/scripts/  
  
RUN chmod u+x /etc/bareos/scripts/bpipe-pg-db  
RUN sed -i '/Plugin Directory/ s/# *//' /etc/bareos/bareos-
fd.d/client/myself.conf  
  
EXPOSE 9102  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/bareos-fd", "-u", "bareos", "-f"]

